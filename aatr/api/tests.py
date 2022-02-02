import json

from django.test import TestCase
from rest_framework.response import Response
from rest_framework.test import APIClient

from aatr.api.models import User


class TestSignin(TestCase):

    def test_signin_success(self):
        client: APIClient = APIClient()

        signin_data = {
            'email': 'jules@gmail.com',
            'password': 'CoolBeans123!'
        }

        res: Response = client.post(
            '/api/signin/',
            data=json.dumps(signin_data),
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

    def test_empty_email_field(self):
        client: APIClient = APIClient()

        signin_data = {
            'email': '',
            'password': 'CoolBeans123!'
        }

        res: Response = client.post(
            '/api/signin/',
            data=json.dumps(signin_data),
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
                    "This field may not be blank."
                ]
            }
        )

    def test_invalid_email_field(self):
        client: APIClient = APIClient()

        signin_data = {
            'email': 'invalidemail',
            'password': 'CoolBeans123!'
        }

        res: Response = client.post(
            '/api/signin/',
            data=json.dumps(signin_data),
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

    def test_empty_password_field(self):
        client: APIClient = APIClient()

        signin_data = {
            'email': 'jules@gmail.com',
            'password': ''
        }

        res: Response = client.post(
            '/api/signin/',
            data=json.dumps(signin_data),
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
                    "This field may not be blank."
                ]
            }
        )

    def test_user_does_not_exist(self):
        client: APIClient = APIClient()

        signin_data = {
            'email': 'jules@gmail.com',
            'password': 'CoolStuffYo'
        }

        res: Response = client.post(
            '/api/signin/',
            data=json.dumps(signin_data),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            401
        )

        self.assertEqual(
            res.json(),
            {
                "detail": "Incorrect authentication credentials."
            }
        )

    def test_user_exists_wrong_password(self):
        client: APIClient = APIClient()

        User.objects.create_user(
            email='jules@gmail.com',
            password='NewPassword123'
        )

        signin_data = {
            'email': 'jules@gmail.com',
            'password': 'NeverUsed'
        }

        res: Response = client.post(
            '/api/signin/',
            data=json.dumps(signin_data),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            401
        )

        self.assertEqual(
            res.json(),
            {
                "detail": "Incorrect authentication credentials."
            }
        )
