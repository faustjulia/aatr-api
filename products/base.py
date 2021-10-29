from typing import Dict, List

import requests

from products.response import res_data



class ProductRequest:

    def __init__(self):
        self.url = 'https://amazon-products1.p.rapidapi.com/search'
        self.headers = {
            'x-rapidapi-host': 'amazon-products1.p.rapidapi.com',
            'x-rapidapi-key': '053e00a14fmsh0a56e00fbabbe95p1438bajsn8d4c446bdd86'
        }
        self.timeout = 20

    def _request(
        self,
        method: str,
        **kwargs
    ) -> requests.Response:
        kwargs.update({
            'timeout': self.timeout
        })
        return getattr(requests, method)(**kwargs)

    def get(
        self,
        params: Dict
    ) -> requests.Response:
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

DEBUG = True

if not DEBUG:
    request = ProductRequest()
    res: requests.Response = request.get(params=data)
    res_data: Dict = res.json()
    print(res)

# request = ProductRequest()
# res: requests.Response = request.get(params=data)
# res_data: Dict = res.json()
# print(res)
# print(res_data)

class Products:

    def __init__(
        self,
        data: Dict,
        amount: int
    ):

        self.data = data
        self.amount = amount

    def get(self) -> List:
        products: List = []

        for product in self.data['results']:
            title: str = product.get('title')
            image: str = product.get('image')
            full_link: str = product.get('full_link')
            current_price: float = product.get('prices')['current_price']
            currency: str = product.get('prices')['currency']

            if current_price > -1.0:

                new_dict: Dict = {
                    'title': title,
                    'image': image,
                    'full_link': full_link,
                    'current_price': current_price,
                    'currency': currency
                }

                products.append(new_dict)

                if len(products) >= self.amount:
                    break

        return products


products: List = Products(data=res_data, amount=5).get()

with open('products.txt', 'w') as f:
    for key, item in enumerate(products):
        title: str = item['title']
        currency: str = item['currency']
        current_price: float = item['current_price']
        link: str = item['full_link']
        f.write(
            f'Product #{key + 1}:\n'
            f'  {title}\n'
            f'  Price: {currency}{current_price}\n'
            f'  Link: {link}\n'
        )
    f.close()
