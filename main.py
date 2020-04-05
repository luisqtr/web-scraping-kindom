import firebase_admin
from firebase_admin import credentials

# Array of original keys in the file
FIREBASE_DB_KEY_FOLDER  = "db_key/"
FIREBASE_DB_KEY_EXT     = ".json" 
FIREBASE_KEYS_LIST = ["type", "project_id", "private_key_id", "private_key", 
                "client_email", "client_id", "auth_uri", "token_uri", 
                "auth_provider_x509_cert_url", "client_x509_cert_url"]



cred = credentials.Certificate("db_key/luisquintero-67246-firebase-adminsdk-3mkhk-7dbd7ab130.json")
firebase_admin.initialize_app(cred)

