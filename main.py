import re

# Local libs
from src.setup import *
# Google Firebase
import firebase_admin
from firebase_admin import credentials, firestore

# Name of the Collection (Table) in the database
COLLECTION_ID_PRODUCTS = 'productos'

# Name of the property
FIELD_ID_WEBSITE   = 'notas'
FIELD_ID_PRICE     = 'precio'
FIELD_ID_WEIGHT    = 'pesoLb'

"""
The rule of thumb here is to have 1 proxy or IP address make not more than 5 requests to Amazon in a minute. 
If you are scraping about 100 pages per minute, we need about 100/5 = 20 Proxies.
How to: https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/
"""

# Entry point
if __name__ == "__main__":
    pass