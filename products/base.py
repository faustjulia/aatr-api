from typing import Dict

import requests


# Hiking shoes = 55
# Sunscreen = 60
# Beach towel = 60
# Sun glasses = 59
# Water bottle = 60

# data = response.json()
# print(data)
#
# print(response.json()['results'][0].get('title'))
# print(response.json()['results'][0].get('image'))
# print(response.json()['results'][0].get('full_link'))
# print(response.json()['results'][0].get('prices'))

# TODO: Exercise 1: A proper request following all the previous instructions
# 1. Add variable type to the 'response'
# 2. Instead of using separate 'url' variable,
#    move 'https://amazon-products1.p.rapidapi.com/search' in .get(url=...)
# 3. Instead of using separate 'headers' variable,
#    move {... headers_content ...} in .get(headers=...)
# 4. Instead of using separate 'querystring' variable,
#    move {... querystring_content ...} in .get(params=...)
# 5. Choose one either single or double quotes,
#    and stick with them - replace all of them with one type.

# TODO: Exercise 2: Create a 'ProductRequest' class
# 1. Create a new 'ProductRequest' class blueprint
# 2. Create a new method called 'def _request(self) -> requests.Response:'
# 3. Move the content of 'Exercise 1' to the new '_request' method (return the response)


# TODO: Exercise 3: Move parts that don't change to the __init__
# 1. Create a new 'self.url' variable in '__init__' method (and use it in code)
# 2. Create a new 'self.headers' variable in '__init__' method (and use it in code)

# TODO: Exercise 4: Add 'timeout' (in case we can't reach the API url)
# 1. Create a separate method called '.get()' in 'ProductRequest' class
# 2. Adjust '_request' method to use 'getattr()' and '**kwargs' (see the video)
# 3. Add new variable called 'self.timeout' to __init__ method (see the video)
# 4. Update 'kwargs' with 'self.timeout' in '_request' method (see the video)
# 5. Adjust '.get()' method to use '_request' method (see the video)

# TODO: Exercise 5: Data extraction for the first product
# 1. Use 'ProductRequest' to create a new request
# 2. Assign the result of .get() method execution to a new variable called 'res'
# 3. Create a new variable 'res_data: Dict = res.json()'
# 4. Get the first product from the 'results' key in 'res_data'
#    and assign it to a new variable called 'product'
# 5. Find out how to access product fields:
#    'title', 'image', 'full_link', 'current_price', 'currency'
#    using 'product' variable
# 6. Create a new empty 'List' variable called 'products'
# 7. Append a new item
#    (Dict with product 'title', 'image', 'full_link', 'current_price', 'currency')
#    to 'products'

# TODO: Exercise 6: Create 'get_products' function
# 1. Create a new function called 'get_products'
# 2. 'get_products' function takes 1 argument 'res_data'
# 3. The goal of the function is to return a list of 5 products
# 4. Each product should be appended to the 'products' list
#    as a Dict with with product 'title', 'image', 'full_link', 'current_price', 'currency'
# 5. Use 'for loop' to with 'break' statement to end the 'for loop' once you have collected 5 products
# 6. Use if statement to only add products with current_price higher than -1.0 (float)
# 7. The function should return a list of products (add a return type to the function)

class ProductRequest:

    def __init__(self):
        self.url = 'https://amazon-products1.p.rapidapi.com/search'
        self.headers = {
            'x-rapidapi-host': 'amazon-products1.p.rapidapi.com',
            'x-rapidapi-key': '053e00a14fmsh0a56e00fbabbe95p1438bajsn8d4c446bdd86'
        }
        self.timeout = 20

    def _request(self,
                 method: str,
                 **kwargs) -> requests.Response:
        kwargs.update({
            'timeout': self.timeout
        })
        return getattr(requests, method)(**kwargs)

    def get(self,
            params: Dict) -> requests.Response:
        return self._request(
            method='get',
            url=self.url,
            headers=self.headers,
            params=params
        )


data: Dict = {
    'country': 'US',
    'query': 'Water bottle',
    'page': '1'
}

request = ProductRequest()
res: requests.Response = request.get(params=data)
res_data: Dict = res.json()
# print(res)
print(res_data)

res_data_copy = res_data.copy()
print(res_data_copy)


# product: Dict = res_data['results'][0]
#
# title: str = product.get('title')
# print(type(title))
#
# image: str = product.get('image')
# full_link: str = product.get('full_link')
# current_price: str = product.get('prices')['current_price']
# currency: str = product.get('prices')['currency']
#
# products: List = []
#
# new_dict: Dict = {
#     'title': product.get('title'),
#     'image': product.get('image'),
#     'full_link': product.get('full_link'),
#     'current_price': product.get('prices')['current_price'],
#     'currency': product.get('prices')['currency']
# }
#
# products.append(new_dict)


# print(products)


def get_products(res_data):
    new_dictionary = {}
    products = []

    for product in res_data:

        title: str = product.get('title')
        image: str = product.get('image')
        full_link: str = product.get('full_link')
        current_price: str = product.get('prices')['current_price']
        currency: str = product.get('prices')['currency']

        if float(current_price) > -1.0:
            new_dictionary: Dict = {
                'title': title,
                'image': image,
                # 'full_link': product.get('full_link'),
                # 'current_price': product.get('prices')['current_price'],
                # 'currency': product.get('prices')['currency']
            }

        products.append(new_dictionary)

    print(products)


get_products(res_data)
