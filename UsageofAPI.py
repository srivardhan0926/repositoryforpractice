import os
from dotenv import load_dotenv
import requests
import json
from woocommerce import API
#load_dotenv: Reads the key,value pair from .env and adds them to environment variable. It is great of managing app settings during development and in production using 12-factor principles.


load_dotenv()
product_id=1000
regular_price=10
raised_price=12
lowered_price=08

def change_price(idProduct,price):
  
    wcapi = API(
        url= os.getenv('DOMAIN'), 
        consumer_key= os.getenv('CONSUMER_KEY'), 
        consumer_secret= os.getenv('CONSUMER_SECRET'), 
        wp_api=True, 
        version="wc/v3" 
    )

    data = {
        "regular_price": price
    }

    wcapi.put("products/" + idProduct, data).json()
    
    print("New price set to " + data["regular_price"])
    
    
    
    
def getWeather():

    url = os.getenv('API_BASEURL')

    headers = {
    "Accept": "application/json"
    }
    
    payload = {
    "key": os.getenv('API_KEY'),
    "city": os.getenv('API_CITY'),
    "country": os.getenv('API_COUNTRY')
    }
    

    response = requests.request(
    "GET",
    url,
    params=payload,
    headers=headers  
    )

    data = response.text

    parse_json = json.loads(data)

    getWeather()
    
    get_parse_result = parse_json["data"][0]["weather"]["code"]
    
    match get_parse_result:
        case 502:
            changePrice(raised_price, product_id)

        case 800:
            changePrice(lowered_price, product_id)

        case _:
            changePrice(regular_price, product_id)
    
