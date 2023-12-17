import requests
import json

from typing import List

class Product:
    def __init__(self, name, price, image):
        self.name = name
        self.price = price
        self.image = image

    def __repr__(self):
        return f'Product({self.name}, {self.price}, {self.image})'


def countdown_search(search_term: str = "") -> List[Product]:
    headers = {
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'x-requested-with': 'OnlineShopping.WebApp'
    }

    params = {
        'target': 'search',
        'search': search_term,
        'inStockProductsOnly': 'false',
    }

    response = requests.get('https://www.countdown.co.nz/api/v1/products', params=params, cookies={}, headers=headers)

    j = response.json()

    j = j['products']['items']
    products = []

    for dict in j:
        products.append(
            Product(dict['name'], dict['price']['salePrice'], dict['images']['big'])
        )

    return products

def get_newworld_access_token():

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    response = requests.get('https://www.newworld.co.nz/CommonApi/Account/GetCurrentUser',
                            headers=headers)

    j = response.json()

    return j['access_token']

def newworld_search(search_term: str = "") -> List[Product]:
    access_token = get_newworld_access_token()

    headers = {
        'authorization': f'Bearer {access_token}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    params = {
        'q': search_term,
        's': 'price-asc',
        'pg': '1',
        'storeId': '60928d93-06fa-4d8f-92a6-8c359e7e846d',
        'publish': 'true',
        'ps': '9999',
    }

    response = requests.get('https://www.newworld.co.nz/next/api/products/search', params=params, cookies={},
                            headers=headers)

    j = response.json()


    j = j['data']['products']
    products = []

    for dict in j:
        api_image_string = dict['productId']
        product_id = api_image_string.split("-")[0]
        image_url = f"https://a.fsimg.co.nz/product/retail/fan/image/200x200/{product_id}.png"
        products.append(
            Product(dict['name'], dict['price']/100, image_url)
        )

    return products
def get_paknsave_access_token():

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    response = requests.get('https://www.paknsave.co.nz/CommonApi/Account/GetCurrentUser',
                            headers=headers)


    j = response.json()

    return j['access_token']

def paknsave_search(search_term: str = "") -> List[Product]:
    access_token = get_paknsave_access_token()

    headers = {
        'authorization': f'Bearer {access_token}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    params = {
        'q': search_term,
        's': 'price-asc',
        'pg': '1',
        'storeId': 'e1925ea7-01bc-4358-ae7c-c6502da5ab12',
        'publish': 'true',
        'ps': '9999',
    }

    response = requests.get('https://www.paknsave.co.nz/next/api/products/search', params=params, cookies={},
                            headers=headers)


    j = response.json()

    j = j['data']['products']
    products = []

    for dict in j:
        api_image_string = dict['productId']
        product_id = api_image_string.split("-")[0]
        image_url = f"https://a.fsimg.co.nz/product/retail/fan/image/200x200/{product_id}.png"
        products.append(
            Product(dict['name'], dict['price']/100, image_url)
        )

    return products


def perform_search(search_function, search_prompt):
    search_query = input(search_prompt)
    result = search_function(search_query)

    for product in result:
        print(product)


if __name__ == '__main__':
    perform_search(countdown_search, "Countdown Search:")
    perform_search(newworld_search, "New World Search:")
    perform_search(paknsave_search, "PaknSave Search:")
