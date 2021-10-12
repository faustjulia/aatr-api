from typing import Dict, List


class Products:

    def __init__(self,
                 data: Dict,
                 amount: int):

        self.data = data
        self.amount = amount

    def get(self) -> List:
        products: List = []

        for product in self.data['results']:

            if len(products) == self.amount:
                break

            if product['prices']['current_price'] == -1.0:
                continue

            if product['title'] == '':
                continue

            if product['image'] == '':
                continue
            elif product['image'].split('.')[-1] != 'jpg':
                continue

            products.append({
                'title': product.get('title'),
                'image': product.get('image'),
                'full_link': product.get('full_link'),
                'current_price': product.get('prices')['current_price'],
                'currency': product.get('prices')['currency']
            })

        return products
