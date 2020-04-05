import re
import bottlenose

# Local libs
from src.setup import *
# Google Firebase
import firebase_admin
from firebase_admin import credentials, firestore

# Amazon
#from amazonproduct import API, ResultPaginator, AWSError

# Name of the Collection (Table) in the database
COLLECTION_ID_PRODUCTS = 'productos'

# Name of the property
FIELD_ID_WEBSITE   = 'notas'
FIELD_ID_PRICE     = 'precio'
FIELD_ID_WEIGHT    = 'pesoLb'


# Read price from amazon product

def get_amazon_asin_from_url(url):
    url = "http://www.amazon.com/Kindle-Wireless-Reading-Display-Generation/dp/B0015T963C"
    regex = "http://www.amazon.com/([\\w-]+/)?(dp|gp/product)/(\\w+/)?(\\w{10})"
    m = re.search(regex, url)
    if (m is not None):
        print(m)
    return 1


def price_offers(asin):
    pass
    """
    from config import AWS_KEY, SECRET_KEY
    api = API(AWS_KEY, SECRET_KEY, 'de')
    str_asin = str(asin)
    node = api.item_lookup(id=str_asin, ResponseGroup='Offers', Condition='All', MerchantId='All')
    for a in node.Items.Item.Offers.Offer:
        print a.OfferListing.Price.FormattedPrice
    """

def main():
    ### FIREBASE CONNECTION
    database_key_filepath = get_firebase_db_key()

    # Connect to database
    cd = credentials.Certificate(database_key_filepath)
    firebase_admin.initialize_app(cd)

    # App instance
    db = firestore.client()

    # Get specified collection
    products_collection = db.collection(COLLECTION_ID_PRODUCTS)
    docs = products_collection.stream()
    for doc in docs:
        print('{} : {}'.format(doc.id,doc.to_dict()))

    ### AMAZON CONNECTION
    cd_aws = get_amazon_keys() #credentials amazon web services
    AWS_ACCESS_KEY_ID       = cd_aws["AWSAccessKeyId"]
    AWS_SECRET_ACCESS_KEY   = cd_aws["AWSSecretKey"]
    AWS_ASSOCIATE_TAG       = "luiseduve"
    amazon = bottlenose.Amazon(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG, Region='US')

    # Test product
    product_asin = "B084T5HTLB"
    # TODO: Returns HTTP 400 because the AWS_ASSOCIATE_TAG is not available in advertising.amazon.com
    # https://github.com/lionheart/bottlenose

    # Scraping Pytho
    ## https://www.youtube.com/watch?v=Bg9r_yLk7VY
    ## https://www.scrapehero.com/tutorial-how-to-scrape-amazon-product-details-using-python-and-selectorlib/
    response.ItemLookup(ItemId=product_asin)
    
    
    
    

# Entry point
if __name__ == "__main__":
    main()

    
