# ------------------
# --- NOT WORKING
# ------------------

import bottlenose ## Connection with Amazon API not possible

# Amazon
#from amazonproduct import API, ResultPaginator, AWSError

AMAZON_DB_KEY_EXT = ".csv"
AMAZON_KEYS_LIST = ["AWSAccessKeyId", "AWSSecretKey"]

def get_amazon_keys(return_dict = False):
    """
    Returns the dict of the 
    """
    dict_file = None
    for file in os.listdir(DB_KEY_FOLDER):
        # Open files that are Json
        if file.endswith(AMAZON_DB_KEY_EXT):
            #try:          
                with open(DB_KEY_FOLDER+file) as f:
                    reader = csv.reader(f, delimiter = "=")
                    dict_file = {row[0]:row[1] for row in reader }
                    print(dict_file)
                # If the dictionary is the same than the expected keys
                if (AMAZON_KEYS_LIST == list(dict_file.keys())):
                    print("Dictionary for Amazon was found from:", DB_KEY_FOLDER+file)
                    if (return_dict):
                        return dict_file
                    else:
                        return DB_KEY_FOLDER+file
            #except:
            #    continue

    print("Firebase database private key not found")
    return 1

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

def connect_amazon():
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
    cd_aws = get_amazon_keys(return_dict=True) #credentials amazon web services
    AWS_ACCESS_KEY_ID       = cd_aws["AWSAccessKeyId"]
    AWS_SECRET_ACCESS_KEY   = cd_aws["AWSSecretKey"]
    AWS_ASSOCIATE_TAG       = "grandcloser93"
    amazon = bottlenose.Amazon(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG, Region='US')

    # Test product
    product_asin = "B084T5HTLB"
    # TODO: Returns HTTP 400 because the AWS_ASSOCIATE_TAG is not available in advertising.amazon.com
    # https://github.com/lionheart/bottlenose

    # Scraping Pytho
    ## https://www.youtube.com/watch?v=Bg9r_yLk7VY
    ## https://www.scrapehero.com/tutorial-how-to-scrape-amazon-product-details-using-python-and-selectorlib/
    response = amazon.ItemLookup(ItemId=product_asin)
    
    
# Entry point
if __name__ == "__main__":
    #main()

    cd_aws = get_amazon_keys(return_dict=True) #credentials amazon web services
    AWS_ACCESS_KEY_ID       = cd_aws["AWSAccessKeyId"]
    AWS_SECRET_ACCESS_KEY   = cd_aws["AWSSecretKey"]
    AWS_ASSOCIATE_TAG       = "grandcloser93"
    amazon = bottlenose.Amazon(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG, Region='US')

    # Test product
    product_asin = "B084T5HTLB"
    # TODO: Returns HTTP 400 because the AWS_ASSOCIATE_TAG is not available in advertising.amazon.com
    # https://github.com/lionheart/bottlenose

    # Scraping Pytho
    ## https://www.youtube.com/watch?v=Bg9r_yLk7VY
    ## https://www.scrapehero.com/tutorial-how-to-scrape-amazon-product-details-using-python-and-selectorlib/
    response = amazon.ItemLookup(ItemId=product_asin)
    print(response)