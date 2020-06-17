### REFERENCE DEV: https://googleapis.dev/python/firestore/latest/index.html

# Local libs
import config
from src.setup import *
import src.utils as utils

# Libs
import time
from datetime import datetime
import pandas as pd
import requests
from selectorlib import Extractor

# Google Firebase
import firebase_admin
from firebase_admin import credentials, firestore, db


TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M")

"""
The rule of thumb here is to have 1 proxy or IP address make not more than 5 requests to Amazon in a minute. 
If you are scraping about 100 pages per minute, we need about 100/5 = 20 Proxies.
How to: https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/
"""

def create_local_copy_db():
    """
    Returns dictionary with the whole database
    """
    data_dictionary = {}
    database_key_filepath = get_firebase_db_key(return_dict=False)
    api_connection = get_firebase_google_services(return_dict = True)

    # Connect to database
    cd = credentials.Certificate(database_key_filepath)
    firebase_admin.initialize_app(cd)

    # App instance
    db = firestore.client()

    # Get specified collection
    products_collection = db.collection(config.COLLECTION_ID_PRODUCTS)
    docs = products_collection.stream()
    for doc in docs:
        data_dictionary[doc.id] = doc.to_dict()
        print('{} : {}'.format(doc.id,doc.to_dict()))
    return data_dictionary

def load_db_local_file(filename):
    try:
        print('Loading data from local file', filename)
        return utils.load_json(filename)
    except Exception as e:
        print('No se encuentra en la ruta especificada', filename)
        print('Error:', e)
        return -1

def create_excel_from_dictionary(data):
    # Create Pandas DataFrame from dictionary
    cols = ['uid']+config.cols_from_db+config.cols_analysis
    df = pd.DataFrame()
    for uid,document in data.items():
        data_to_append = {}
        data_to_append["uid"] = uid
        for field,vals in document.items():
            if field=="variaciones":
                continue
            if type(vals) == int:
                data_to_append[field] = [vals]
            else:
                data_to_append[field] = vals
        # Add data for processing
        website = data[uid]["notas"]
        data_to_append["websiteURL"] = website
        data_to_append["selectorlib_plantilla"] = website[website.find('www.')+4 : website.find('.',website.find('www.')+4)] # Find website name, template must be the same name .txt
        data_to_append["fechaUltimaActualizacion"] = datetime.now()
        data_to_append["desactualizado"] = True

        # Add variaciones multiple times at the end
        if len(data[uid]["variaciones"])>0:
            for variacion in data[uid]["variaciones"][0]:
                data_to_append["variaciones"] = variacion
                df = df.append(pd.DataFrame.from_dict(data_to_append), ignore_index=True)#print(data_to_append)
        else:
            data_to_append["variaciones"] = "No"
            df = df.append(pd.DataFrame.from_dict(data_to_append), ignore_index=True)#print(data_to_append)
    # Attach all the columns
    df = pd.DataFrame(data = df, columns=cols)
    df.to_excel(config.filename_excel_file+".xlsx", index=False)
    # cache copy of db
    df.to_excel(config.path_cache_db+"BD_COPY_"+TIMESTAMP+".xlsx", index=False)
    return config.filename_excel_file+".xlsx"
    

def search_new_prices_webscrap(filename, only_outdated_entries=True, colOutdated="desactualizado"):
    """
    Iterates a dataframe and webscraps it based on conditions
    """
    # Load file
    df = pd.read_excel(filename, engine="openpyxl")

    # Go through all the websites
    total_to_process = df.shape[0]
    for i in range(total_to_process):    
        print("(", str(i+1),"|", str(total_to_process),") Procesando artículo: ", df.loc[i,"titulo"], "con Variacion:", df.loc[i,"variaciones"])
        # Filter only the entries to be updated
        if (df.loc[i,'desactualizado'] == False):
            print('\tDesactualizado=False, no se descargará info...')
            continue

        # Extract data from URL
        website = df.loc[i,'websiteURL']
        plantilla = df.loc[i,'selectorlib_plantilla']
        r = requests.get(website)
        e = Extractor.from_yaml_file(config.path_selectorlib_templates+plantilla+".txt")
        if (r.status_code == requests.codes.ok):
            # Success response from requests
            result = e.extract(r.text)
            price = None
            try:
                price = result["price"]
                if(result["price"] is not None):
                    df.loc[i,"precioNuevoEnWebsite"] = price
                df.loc[i,"ResultadoWebscrap"] = str(result)
            except Exception as e:
                df.loc[i,"precioNuevoEnWebsite"] = ""
                df.loc[i,"ResultadoWebscrap"] = e.message
        else:
            df.loc[i,"ResultadoWebscrap"] = r.text
        df.loc[i,"fechaUltimaActualizacion"] = datetime.now()
        df.loc[i,"desactualizado"] = False
        print("\tResultado:",df.loc[i,"ResultadoWebscrap"])

        # Grabar cambios del archivo a procesar nuevamente los datos
        df.to_excel(config.filename_excel_file+".xlsx", index=False)

        # SLEEP TO AVOID BAN FROM SERVERS
        print("\tEsperando para evitar ban:",str(config.time_secs_between_transactions),"segundos...")
        time.sleep(config.time_secs_between_transactions)
    print("Terminado!")


def main():
    ## DATA ANALYSIS
    data = None
    
    # Download from server or load from file
    if(config.DESCARGAR_BD_DESDE_GOOGLE):
        data = create_local_copy_db()
        utils.create_json(data, json_path=config.path_local_db+config.filename_local_db+".json", indent=3)
        # Create a copy of the databse with timestamp
        utils.create_json(data, json_path=config.path_cache_db+config.filename_local_db+TIMESTAMP+".json")
    else:
        data = load_db_local_file(config.path_local_db+config.filename_local_db+".json")

    if(config.CREAR_NUEVO_ARCHIVO_EXCEL):
        create_excel_from_dictionary(data)
    
    if(config.BUSCAR_PRECIOS_NUEVOS):
        search_new_prices_webscrap(config.filename_excel_file+".xlsx")


# Entry point
if __name__ == "__main__":
    main()