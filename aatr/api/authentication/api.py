import typing

from django.http.request import HttpRequest
from django.utils import timezone
from rest_framework import authentication

from aatr import settings
from aatr.api import models
from aatr.api.exceptions.exceptions import AuthorizationFailed, SessionFailed


class NoAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request: HttpRequest):
        return None, None

    def authenticate_header(self, request: HttpRequest):
        return 'Cookie'


def get_authorized_session(request: HttpRequest) -> models.Session:
    token: typing.Union[str, None] = request.COOKIES.get(
        settings.SESSION_COOKIE_NAME
    )

    if token is None:
        raise AuthorizationFailed()

    try:

        return (
            models
                .Session
                .objects
                .select_related('user')
                .get(
                token=token,
                is_active=True,
                last_active__gte=timezone.now() - settings.SESSION_DURATION,
            )
        )

    except models.Session.DoesNotExist:
        raise SessionFailed()


class PrivateAPIAuthentication(authentication.BaseAuthentication):

    def authenticate(
        self,
        request: HttpRequest
    ) -> typing.Tuple[models.User, models.Session]:
        session: models.Session = get_authorized_session(
            request=request
        )
        return session.user, session
