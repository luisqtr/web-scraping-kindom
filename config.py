# Activar esta variable reemplazando `False` por `True`.
#  Cuando está activa, se conecta con la base de datos y descarga toda la información existente.
DESCARGAR_BD_DESDE_GOOGLE = False

# Crear archivo de Excel que resembla la base de datos
CREAR_NUEVO_ARCHIVO_EXCEL = False

# Ejecutar webscrap en todos los websites basado en archivo de Excel
BUSCAR_PRECIOS_NUEVOS = True  

# CUIDADO!!!!!!!!!!!!!!!!!
#  Al activar esta variable modifica la BD final. 
#  Pruebe primero de manera local que los cambios que desea hacer sean los correctos. 
ACTUALIZAR_BD_A_GOOGLE = False

##################
###### DEV
##################

# Main Pandas DB filename
filename_excel_file = "./BASE_DE_DATOS"

# Connection to DB
path_local_db = './database/'
path_cache_db = path_local_db+'db_cache/'
filename_local_db = 'db_kindom'

# Database
# Name of the Collection (Table) in the database
COLLECTION_ID_PRODUCTS = 'productos'
cols_from_db = ["titulo","pesoLb", "precio", "variaciones", "notas"]
cols_analysis = ["websiteURL","selectorlib_plantilla","fechaUltimaActualizacion", "desactualizado", "precioNuevoEnWebsite", "ResultadoWebscrap"]

# Webscraping
time_secs_between_transactions = 5
path_selectorlib_templates = "./selectorlib_templates/"
