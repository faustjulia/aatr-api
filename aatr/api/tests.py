import datetime
import json
import typing
from unittest.mock import patch, Mock

import requests
from django.conf import settings
from django.test import TestCase
from requests.exceptions import HTTPError
from rest_framework.response import Response
from rest_framework.test import APIClient

from aatr.api.models import User, Session


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


class TestSignin(TestCase):

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

    def test_successful_signin(self):
        client: APIClient = APIClient()

        User.objects.create_user(
            email='jules@gmail.com',
            password='NewPassword123'
        )

        signin_data = {
            'email': 'jules@gmail.com',
            'password': 'NewPassword123'
        }

        res: Response = client.post(
            '/api/signin/',
            data=json.dumps(signin_data),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            200
        )

        self.assertTrue(
            settings.SESSION_COOKIE_NAME in res.cookies
        )


class TestSignout(TestCase):

    def test_missing_token_cookie(self):
        client: APIClient = APIClient()

        res: Response = client.post(
            '/api/signout/',
        )

        self.assertEqual(
            res.status_code,
            401
        )

        self.assertEqual(
            res.json(),
            {
                "detail": "Authorization cookie missing."
            }
        )

    def test_session_does_not_exist(self):
        client: APIClient = APIClient()
        client.cookies[settings.SESSION_COOKIE_NAME] = 'test_cookie_token'

        res: Response = client.post(
            '/api/signout/',
        )

        self.assertEqual(
            res.status_code,
            401
        )

        self.assertEqual(
            res.json(),
            {
                "detail": "Invalid session or inactive user."
            }
        )

    def test_session_expired(self):
        test_user = User.objects.create_user(
            name='yuliia',
            email='jules@gmail.com',
            password='NewPassword123',
            terms=True,
        )

        session = Session.objects.create(
            user=test_user
        )

        session.last_active = datetime.datetime.now() - datetime.timedelta(
            days=2 * 365)
        session.save()

        client: APIClient = APIClient()
        client.cookies[settings.SESSION_COOKIE_NAME] = session.token

        res: Response = client.post(
            '/api/signout/',
        )

        self.assertEqual(
            res.status_code,
            401
        )

        self.assertEqual(
            res.json(),
            {
                "detail": "Invalid session or inactive user."
            }
        )

    def test_successful_signout(self):
        test_user = User.objects.create_user(
            name='yuliia',
            email='jules@gmail.com',
            password='NewPassword123',
            terms=True,
        )

        session = Session.objects.create(
            user=test_user,
            last_active=datetime.datetime.now()

        )

        client: APIClient = APIClient()
        client.cookies[settings.SESSION_COOKIE_NAME] = session.token

        res: Response = client.post(
            '/api/signout/',
        )

        self.assertEqual(
            res.status_code,
            200
        )
        breakpoint()

        self.assertEqual(
            res.cookies.get(settings.SESSION_COOKIE_NAME).value,
            ""
        )
