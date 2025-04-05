from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class UserRoleNotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = 'user_role_not_found'
    default_detail = _('User role is not found.')
