### REFERENCE DEV: https://googleapis.dev/python/firestore/latest/index.html

from datetime import datetime

# Local libs
import config
from src.setup import *
import src.utils as utils

# Google Firebase
import firebase_admin
from firebase_admin import credentials, firestore, db

# Name of the Collection (Table) in the database
COLLECTION_ID_PRODUCTS = 'productos'

# Name of the property
FIELD_ID_WEBSITE   = 'notas'
FIELD_ID_PRICE     = 'precio'
FIELD_ID_WEIGHT    = 'pesoLb'

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
    products_collection = db.collection(COLLECTION_ID_PRODUCTS)
    docs = products_collection.stream()
    for doc in docs:
        data_dictionary[doc.id] = doc.to_dict()
        print('{} : {}'.format(doc.id,doc.to_dict()))
    return data_dictionary

def load_db_local_file(filename):
    try:
        utils.load_json(filename)
    except Exception as e:
        print(filename,'no se encuentra en la ruta especificada.')
        print('Error:', e)
        return -1

def main():
    if(config.DESCARGAR_BD_DESDE_GOOGLE):
        data = create_local_copy_db()
        utils.create_json(data, json_path=config.path_local_db+config.filename_local_db+".json", indent=3)
        # Create a copy of the databse with timestamp
        utils.create_json(data, json_path=config.path_cache_db+config.filename_local_db+TIMESTAMP+".json")
    else:
        load_db_local_file(config.path_local_db+config.filename_local_db+".json")
    
    

# Entry point
if __name__ == "__main__":
    main()