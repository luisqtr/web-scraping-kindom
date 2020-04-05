from src.setup import *

import firebase_admin
from firebase_admin import credentials








def main():
    # Connect to database
    cred = credentials.Certificate(get_firebase_db_key())
    firebase_admin.initialize_app(cred)


# Entry point
if __name__ == "__main__":
    main()
