import random
import unittest
from typing import Dict, List
from unittest.mock import patch, Mock

import requests

from products.parse import Products
from products.request import ProductRequest


class MockResponse:

    def __init__(self):
        pass

    def get_product(
        self,
        current_price: float,
        title: str = 'layajia Water Bottle, 34oz Nonslip Gallon Water Bottle',
        image: str = 'https://m.media-amazon.com/images/I/71iTxQd3c6S._AC_UL320_.jpg'
    ) -> Dict:
        return {
            'asin': 'B092W1R4SD',
            'title': title,
            'image': image,
            'full_link': 'https://www.amazon.com/dp/B092W1R4SD/?psc=1',
            'prices':
                {
                    'current_price': current_price,
                    'previous_price': -1.0,
                    'currency': '$'
                },
            'reviews': {
                'total_reviews': 178,
                'stars': 4.5
            },
            'prime': True
        }

    def get_products(self, invalid_products: List) -> Mock:
        mock_response: Mock = Mock()
        mock_response.status_code = 200

        valid_products: List = [
            self.get_product(current_price=130.0) for _ in range(10)
        ]

        products = invalid_products + valid_products
        random.shuffle(products)

        mock_response.json.return_value = {
            'results': products
        }

        return mock_response

    def get_products_price_higher_than_minus_one(
        self,
        *args, **kwargs
    ) -> Mock:
        return self.get_products(
            invalid_products=[
                self.get_product(current_price=-1.0) for _ in range(10)
            ]
        )

    def get_products_valid_and_invalid_title(
        self,
        *args, **kwargs
    ) -> Mock:
        return self.get_products(
            invalid_products=[
                self.get_product(current_price=130.0, title='') for _ in
                range(10)
            ]
        )

    def get_products_valid_and_invalid_image(
        self,
        *args, **kwargs
    ) -> Mock:
        invalid_image_url: List = [
            self.get_product(current_price=130.0,
                             image='efhewiohvie') for _ in range(5)
        ]

        empty_image_url: List = [
            self.get_product(current_price=130.0,
                             image='') for _ in range(5)
        ]

        products = invalid_image_url + empty_image_url
        random.shuffle(products)

        return self.get_products(
            invalid_products=products
        )


class TestProducts(unittest.TestCase):

    def execute_request_and_get_products(self) -> List:
        request = ProductRequest()

        res: requests.Response = request.get(
            params={
                'country': 'US',
                'query': 'Water bottle'
            }
        )

        return Products(
            res.json(),
            amount=5
        ).get()

    @patch.object(
        target=requests,
        attribute='get',
        side_effect=MockResponse().get_products_price_higher_than_minus_one

    )
    def test_products_price_higher_than_minus_one(self, *args,
                                                  **kwargs):
        products: List = self.execute_request_and_get_products()
        assert MockResponse().get_products_price_higher_than_minus_one

    @patch.object(
        target=requests,
        attribute='get',
        side_effect=MockResponse().get_products_valid_and_invalid_title

    )
    def test_products_valid_title(self, *args, **kwargs):
        products: List = self.execute_request_and_get_products()

        for product in products:
            assert MockResponse().get_products_valid_and_invalid_title

    @patch.object(
        target=requests,
        attribute='get',
        side_effect=MockResponse().get_products_valid_and_invalid_image

    )
    def test_products_valid_title(self, *args, **kwargs):
        products: List = self.execute_request_and_get_products()

        for product in products:
            assert MockResponse().get_products_valid_and_invalid_image
