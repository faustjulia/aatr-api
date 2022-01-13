import json
import typing

import requests
from django.db.transaction import atomic
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException

from aatr.api.models import User
from aatr.api.serializers import SignupSerizlizer
from aatr.settings import MAILGUN_API_KEY


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service Unavailable'
    default_code = 'service_unavailable'


@require_http_methods(['GET'])
def get_sample(r: HttpRequest) -> HttpResponse:
    return HttpResponse(status=200, content=b'sample content julia')


@api_view(['POST'])
@atomic()
def signup_endpoint(request: HttpRequest) -> JsonResponse:
    signup_data: typing.Dict = json.loads(request.body)

    serializer = SignupSerizlizer(data=signup_data)
    serializer.is_valid(raise_exception=True)

    terms: bool = serializer.data.get('terms')

    if terms == False:
        raise serializers.ValidationError({
            "terms": [
                "You must accept terms and conditions."
            ]
        })

    users = User.objects.filter(email=serializer.data['email'])

    if users.exists() == True:
        raise serializers.ValidationError({
            "email": [
                "This email address is already being used."
            ]
        })

    user: User = User.objects.create_user(
        email=serializer.data['email'],
        name=serializer.data['name'],
        terms=serializer.data['terms'],
        password=serializer.data['password']
    )

    try:
        res = requests.post(
            'https://api.mailgun.net/v3/yuliiamartynenko.com/messages',
            auth=('api', MAILGUN_API_KEY),
            data={'from': 'Mentoring <mail@yuliiamartynenko.com>',
                  'to': serializer.data['email'],
                  'subject': 'Alert, Your Payment Is Due',
                  'template': 'alert',
                  })

        res.raise_for_status()

        return JsonResponse(
            status=201,
            data={
                'id': '<20220113195830.0f9bc6de9b894717@yuliiamartynenko.com>',
                'message': 'Queued. Thank you.'}
        )

    except:
        raise ServiceUnavailable()
