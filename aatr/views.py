import datetime
import json
import typing

from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from aatr import settings
from aatr.api import models
from aatr.api.models import User
from aatr.serializers import SigninSerializer


class AuthenticationFailed(APIException):
    status_code = 401
    default_detail = 'Incorrect authentication credentials.'
    default_code = 'authentication_failed'


@api_view(['POST'])
def signin_endpoint(request: HttpRequest) -> JsonResponse:
    signin_data: typing.Dict = json.loads(request.body)

    serializer = SigninSerializer(data=signin_data)
    serializer.is_valid(raise_exception=True)

    user_queryset = User.objects.filter(email=serializer.data['email'])
    user = user_queryset.first()

    if not user_queryset.exists():
        raise AuthenticationFailed()

    # AttributeError: 'NoneType' object has no attribute 'check_password'
    user_password: bool = user.check_password(
        raw_password=serializer.data['password']
    )

    if user_password == False:
        raise AuthenticationFailed()

    session: models.Session = models.Session.objects.create(user=user)

    response: Response = Response()
    response.set_cookie(
        key=settings.SESSION_COOKIE_NAME,
        expires=timezone.now() + datetime.timedelta(days=365 * 100),
        value=session.token,
        secure=True,
        httponly=True,
        samesite='Strict'
    )

    return response
