from typing import Dict, List


class Products:

    def __init__(self,
                 data: Dict,
                 amount: int):

        self.data = data
        self.amount = amount

    def get(self):
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
