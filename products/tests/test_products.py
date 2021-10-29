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
        title: str = 'Layajia Water Bottle, 34oz Nonslip Gallon Water Bottle',
        image: str = 'https://m.media-amazon.com/images/'
                     'I/71iTxQd3c6S._AC_UL320_.jpg',
        full_link: str = 'https://www.amazon.com/dp/B092W1R4SD/?psc=1',
        currency: str = '$'
    ) -> Dict:
        return {
            'asin': 'B092W1R4SD',
            'title': title,
            'image': image,
            'full_link': full_link,
            'prices':
                {
                    'current_price': current_price,
                    'previous_price': -1.0,
                    'currency': currency
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

    def get_products_price_higher_than_five(
        self,
        *args, **kwargs
    ) -> Mock:
        return self.get_products(
            invalid_products=[
                self.get_product(current_price=-2.0) for _ in range(10)
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
            self.get_product(
                current_price=130.0,
                image='efhewiohvie'
            ) for _ in range(5)
        ]

        empty_image_url: List = [
            self.get_product(
                current_price=130.0,
                image=''
            ) for _ in range(5)
        ]

        products = invalid_image_url + empty_image_url
        random.shuffle(products)

        return self.get_products(
            invalid_products=products
        )

    def get_products_valid_and_invalid_full_link(
        self,
        *args, **kwargs
    ) -> Mock:
        invalid_full_link: List = [
            self.get_product(
                current_price=130.0,
                full_link='efhewiohvie'
            ) for _ in range(5)
        ]

        empty_full_link: List = [
            self.get_product(
                current_price=130.0,
                full_link=''
            ) for _ in range(5)
        ]

        products = invalid_full_link + empty_full_link
        random.shuffle(products)

        return self.get_products(
            invalid_products=products
        )

    def get_products_valid_and_invalid_currency(
        self,
        *args, **kwargs
    ) -> Mock:
        invalid_currency: List = [
            self.get_product(
                current_price=130.0,
                currency='€'
            ) for _ in range(5)
        ]

        empty_currency: List = [
            self.get_product(
                current_price=130.0,
                currency=''
            ) for _ in range(5)
        ]

        products = invalid_currency + empty_currency
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

    def test_products_price_higher_than_minus_one(self):
        mocked_product_response = patch.object(
            target=requests,
            attribute='get',
            side_effect=MockResponse().get_products_price_higher_than_minus_one
        )

        with mocked_product_response:
            products: List = self.execute_request_and_get_products()

        for product in products:
            self.assertNotEqual(product['current_price'], -1.0)

    def test_products_valid_title(self):
        mocked_product_response = patch.object(
            target=requests,
            attribute='get',
            side_effect=MockResponse().get_products_valid_and_invalid_title
        )

        with mocked_product_response:
            products: List = self.execute_request_and_get_products()

        for product in products:
            self.assertEqual(
                product['title'],
                'Layajia Water Bottle, 34oz Nonslip Gallon Water Bottle'
            )

    def test_products_valid_image(self):
        mocked_product_response = patch.object(
            target=requests,
            attribute='get',
            side_effect=MockResponse().get_products_valid_and_invalid_image
        )

        with mocked_product_response:
            products: List = self.execute_request_and_get_products()

        for product in products:
            self.assertEqual(
                product['image'],
                'https://m.media-amazon.com/images/I/71iTxQd3c6S._AC_UL320_.jpg'
            )

    def test_products_valid_full_link(self):
        mocked_product_response = patch.object(
            target=requests,
            attribute='get',
            side_effect=MockResponse().get_products_valid_and_invalid_full_link
        )

        with mocked_product_response:
            products: List = self.execute_request_and_get_products()

        for product in products:
            self.assertEqual(
                product['full_link'],
                'https://www.amazon.com/dp/B092W1R4SD/?psc=1'
            )

    def test_products_valid_currency(self):
        mocked_product_response = patch.object(
            target=requests,
            attribute='get',
            side_effect=MockResponse().get_products_valid_and_invalid_currency
        )

        with mocked_product_response:
            products: List = self.execute_request_and_get_products()

        for product in products:
            self.assertEqual(product['currency'], '$')

    def test_products_price_higher_than_five(self):
        mocked_product_response = patch.object(
            target=requests,
            attribute='get',
            side_effect=MockResponse().get_products_price_higher_than_five
        )

        with mocked_product_response:
            products: List = self.execute_request_and_get_products()

        for product in products:
            self.assertEqual(product['current_price'], 130.0)
