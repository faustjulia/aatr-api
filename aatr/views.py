import json
import typing

# import requests
from django.conf import settings
from django.db.transaction import atomic
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.utils import timezone
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from aatr.api import models
from aatr.api.authentication.api import (
    get_authorized_session,
    PrivateAPIAuthentication
)
from aatr.api.exceptions.exceptions import AuthenticationFailed
# from aatr.api.exceptions.exceptions import ServiceUnavailable
from aatr.api.models import User
from aatr.api.models import User as UserData
from aatr.api.serializers.signin import SigninSerializer
from aatr.api.serializers.signup import SignupSerizlizer
from aatr.api.serializers.user import CurrentUserSerializer


# from aatr.settings import MAILGUN_API_KEY


@api_view(['POST'])
@atomic
def signup(request: HttpRequest) -> JsonResponse:
    signup_data: typing.Dict = json.loads(request.body)

    serializer = SignupSerizlizer(data=signup_data)
    serializer.is_valid(raise_exception=True)

    terms: bool = serializer.data.get('terms')

    if terms == False:
        raise serializers.ValidationError({
            'terms': [
                'You must accept terms and conditions.'
            ]
        })

    user_exists: bool = (
        UserData.objects.filter(
            email=serializer.data['email'].lower()
        ).exists()
    )

    if user_exists:
        raise serializers.ValidationError({
            'email': [
                'This email address is already being used.'
            ]
        })

    UserData.objects.create_user(
        email=serializer.data['email'].lower(),
        name=serializer.data['name'],
        terms=serializer.data['terms'],
        password=serializer.data['password']
    )

    # class MailgunAPI:
    #     url = 'https://api.mailgun.net/v3/yuliiamartynenko.com'
    #
    # class SignupTemplate:
    #     subject = 'Sign Up Confirmation'
    #     template = 'sign_up'
    #
    # try:
    #     res = requests.post(
    #         f'{MailgunAPI.url}/messages',
    #         auth=('api', MAILGUN_API_KEY),
    #         data={'from': 'Mentoring <mail@yuliiamartynenko.com>',
    #               'to': serializer.data['email'],
    #               'subject': SignupTemplate.subject,
    #               'template': SignupTemplate.template,
    #               })
    #
    #     res.raise_for_status()
    #     sent = True
    #
    #
    # except requests.HTTPError as e:
    #     print(f'Exception: {e}', flush=True)
    #     sent = False
    #
    # if not sent:
    #     raise ServiceUnavailable()

    return JsonResponse(
        status=201,
        data={
            'detail': 'success'
        }
    )


@api_view(['POST'])
def signin(request: HttpRequest) -> JsonResponse:
    signin_data: typing.Dict = json.loads(request.body)

    serializer = SigninSerializer(data=signin_data)
    serializer.is_valid(raise_exception=True)

    user_queryset = User.objects.filter(email=serializer.data['email'])
    user = user_queryset.first()

    if not user_queryset.exists():
        raise AuthenticationFailed()

    user_password: bool = user.check_password(
        raw_password=serializer.data['password']
    )

    if user_password == False:
        raise AuthenticationFailed()

    session: models.Session = models.Session.objects.create(user=user)

    response: Response = Response()
    response.set_cookie(
        key=settings.SESSION_COOKIE_NAME,
        expires=timezone.now() + settings.SESSION_DURATION,
        value=session.token,
        secure=True,
        httponly=True,
        samesite='Strict'
    )

    return response


@api_view(['POST'])
def signout(request: HttpRequest) -> JsonResponse:
    session: models.Session = get_authorized_session(
        request=request
    )

    session.last_active = timezone.now()
    session.is_active = False
    session.save()

    response: Response = Response()
    response.delete_cookie(
        key=settings.SESSION_COOKIE_NAME,
    )

    return response


class CurrentUserViewSet(viewsets.ViewSet):
    authentication_classes = [PrivateAPIAuthentication]

    def list(self, request: HttpRequest) -> Response:
        return Response(
            CurrentUserSerializer(instance=request.user).data
        )
