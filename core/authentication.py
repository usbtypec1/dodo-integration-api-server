from django.http import HttpRequest
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings


class SpecificTokenAuthentication(BaseAuthentication):

    def authenticate(self, request: HttpRequest):
        token = request.headers.get('Authorization')

        if not token:
            return None

        if token != f'Bearer {settings.AUTHORIZATION_TOKEN}':
            raise AuthenticationFailed('Invalid or missing token')

        return None, None
