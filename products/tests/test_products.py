import json
import random
import typing
import unittest
from typing import Dict, List
from unittest.mock import patch, Mock

import requests
from django.test import TestCase
from requests.exceptions import HTTPError
from rest_framework.response import Response
from rest_framework.test import APIClient

from aatr.api.models import User
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


class TestSignUpEndpoint(TestCase):

    def test_signup_success(self):
        client: APIClient = APIClient()

        res: Response = client.post(
            path='/api/signup/',
            data=json.dumps({
                'name': 'Yuliia Martynenko',
                'email': 'jules@gmail.com',
                'password': 'eegwrgewgwe',
                'terms': True
            }),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            201
        )

        self.assertEqual(
            res.json(),
            {
                'detail': 'success'
            }
        )

    def test_invalid_email(self):
        client: APIClient = APIClient()

        res: Response = client.post(
            path='/api/signup/',
            data=json.dumps({
                'name': 'Yuliia Martynenko',
                'email': 'invalidemail',
                'password': 'eegwrgewgwe',
                'terms': True
            }),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            400
        )

        self.assertEqual(
            res.json(),
            {
                "email": [
                    "Enter a valid email address."
                ]
            }
        )

    def test_password_less_than_min_length(self):
        client: APIClient = APIClient()

        res: Response = client.post(
            path='/api/signup/',
            data=json.dumps({
                'name': 'Yuliia Martynenko',
                'email': 'jules@gmail.com',
                'password': '123',
                'terms': True
            }),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            400
        )

        self.assertEqual(
            res.json(),
            {
                "password": [
                    "Ensure this field has at least 8 characters."
                ]
            }
        )

    def test_password_more_than_max_length(self):
        client: APIClient = APIClient()

        res: Response = client.post(
            path='/api/signup/',
            data=json.dumps({
                'name': 'Yuliia Martynenko',
                'email': 'jules@gmail.com',
                'password': '123jwefwegfouheifhbvuhguw',
                'terms': True
            }),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            400
        )

        self.assertEqual(
            res.json(),
            {
                "password": [
                    "Ensure this field has no more than 16 characters."
                ]
            }

        )

    def test_unaccepted_terms_checkbox(self):
        client: APIClient = APIClient()

        res: Response = client.post(
            path='/api/signup/',
            data=json.dumps({
                'name': 'Yuliia Martynenko',
                'email': 'jules@gmail.com',
                'password': '123jwefwegfow',
                'terms': False
            }),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            400
        )

        self.assertEqual(
            res.json(),
            {
                "terms": [
                    "You must accept terms and conditions."
                ]
            }

        )

    def test_email_already_exists(self):
        user: User = User.objects.create_user(
            email='jules@gmail.com'
        )

        client: APIClient = APIClient()

        res: Response = client.post(
            path='/api/signup/',
            data=json.dumps({
                'name': 'Yuliia Martynenko',
                'email': 'jules@gmail.com',
                'password': '123jwefwegfow',
                'terms': True
            }),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            400
        )

        self.assertEqual(
            res.json(),
            {
                "email": [
                    "This email address is already being used."
                ]
            }
        )

    def test_failed_to_send_email(self):
        client: APIClient = APIClient()

        mocked_response = patch.object(
            target=requests,
            attribute='post',
            side_effect=HTTPError
        )

        with mocked_response:
            res: Response = client.post(
                path='/api/signup/',
                data=json.dumps({
                    'name': 'Yuliia Martynenko',
                    'email': 'jules@gmail.com',
                    'password': '123jwefwegfow',
                    'terms': True
                }),
                content_type='application/json'
            )

        self.assertEqual(
            res.status_code,
            503
        )

        self.assertEqual(
            res.json(),
            {
                "detail": "Service Unavailable"
            }
        )

        was_user_created: bool = User.objects.filter(
            name='Yuliia Martynenko',
            email='jules@gmail.com',
            password='123jwefwegfow',
            terms=True
        ).exists()

        self.assertEqual(
            was_user_created,
            False
        )

    def test_successful_signup(self):
        client: APIClient = APIClient()

        mocked_response = patch.object(
            target=requests,
            attribute='post',
            side_effect=[
                Mock(
                    **{
                        'status_code': 200,
                        'json.return_value': {
                            'id': '<20220113195830.0f9bc6de9b894717@yuliiamartynenko.com>',
                            'message': 'Queued. Thank you.'}

                    }
                )
            ]
        )

        sign_up_data: typing.Dict = {
            'name': 'Yuliia Martynenko',
            'email': 'julia.faust1103@gmail.com',
            'password': '123jwefwegfow',
            'terms': True
        }

        with mocked_response:
            res: Response = client.post(
                path='/api/signup/',
                data=json.dumps(sign_up_data),
                content_type='application/json'
            )

        self.assertEqual(
            res.status_code,
            201
        )

        was_user_created: bool = User.objects.filter(
            email=sign_up_data['email'],
        ).exists()

        self.assertEqual(
            was_user_created,
            True
        )

        self.assertEqual(
            res.json(),
            {
                'id': '<20220113195830.0f9bc6de9b894717@yuliiamartynenko.com>',
                'message': 'Queued. Thank you.'
            }

        )
