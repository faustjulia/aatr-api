from typing import Dict, List


class Products:

    def __init__(
        self,
        data: Dict,
        amount: int = 5
    ):

        self.data = data
        self.amount = amount

    def get(self) -> List:
        products: List = []

        for product in self.data['results']:

            if len(products) == self.amount:
                break

            if any([
                product['prices']['current_price'] == -1.0,
                product['prices']['current_price'] < 5.0,
                product['title'] == '',
                product['image'] == '',
                product['image'].endswith('.jpg') == False,
                product['full_link'] == '',
                'www.amazon.com' not in product['full_link'],
                product['prices']['currency'] == '',
                product['prices']['currency'] != '$'
            ]):
                continue

            products.append({
                'title': product['title'],
                'image': product['image'],
                'full_link': product['full_link'],
                'current_price': product['prices']['current_price'],
                'currency': product['prices']['currency']
            })

        return products
