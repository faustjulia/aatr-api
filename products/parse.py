from typing import Dict, List


class Products:

    def __init__(self,
                 data: Dict,
                 amount: int = 5):

        self.data = data
        self.amount = amount

    def get(self) -> List:
        products: List = []

        for product in self.data['results']:

            if len(products) == self.amount:
                break

            if product['prices']['current_price'] == -1.0:
                continue
            if product['prices']['current_price'] < 5.0:
                continue

            if product['title'] == '':
                continue

            if product['image'] == '':
                continue
            elif product['image'].endswith('.jpg') == False:
                continue

            if product['full_link'] == '':
                continue
            elif 'www.amazon.com' not in product['full_link']:
                continue

            if product['prices']['currency'] == '':
                continue
            elif product['prices']['currency'] != '$':
                continue

            products.append({
                'title': product['title'],
                'image': product['image'],
                'full_link': product['full_link'],
                'current_price': product['prices']['current_price'],
                'currency': product['prices']['currency']
            })

        return products
