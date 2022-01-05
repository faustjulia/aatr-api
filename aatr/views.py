import json
import typing

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework import serializers
from rest_framework.decorators import api_view

from aatr.api.models import User
from aatr.api.serializers import SignupSerizlizer


@require_http_methods(['GET'])
def get_sample(r: HttpRequest) -> HttpResponse:
    return HttpResponse(status=200, content=b'sample content julia')


@api_view(['POST'])
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

    breakpoint()

    if users.exists() == True:
        raise serializers.ValidationError({
            "email": [
                "This email address is already being used."
            ]
        })

    user: User = User.objects.create_user(
        email=serializer.data['email']
    )

    return JsonResponse(
        status=201,
        data={
            'detail': 'success'
        }
    )
