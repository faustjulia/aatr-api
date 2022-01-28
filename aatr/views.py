import json
import typing

from django.http.request import HttpRequest
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException

from aatr.api.models import User as UserData
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

    users = UserData.objects.filter(email=serializer.data['email'])

    if users.exists() == False:
        raise AuthenticationFailed()

    return JsonResponse(
        status=201,
        data={
            'detail': 'success'
        }
    )

    # user: models.User = User.objects.create_user(
    #     email=serializer.data['email']
    # )
    #
    # try:
    #
    #     send_email = requests.post(
    #         "https://api.mailgun.net/v3/yuliiamartynenko.com/messages",
    #         auth=("api", MAILGUN_API_KEY),
    #         data={"from": "Mentoring <mail@yuliiamartynenko.com>",
    #               "to": user.email,
    #               "subject": "Hello Yuliia Martynenko",
    #               "template": "sign_up"
    #               })
    #
    #     breakpoint()
    #
    #     if send_email.status_code == 200:
    #         return JsonResponse(
    #             data={
    #                 "detail": f"Signup was successful, registration email was sent to {user.email}"
    #             }
    #         )
    #
    # except:
    #     raise ServiceUnavailable()
