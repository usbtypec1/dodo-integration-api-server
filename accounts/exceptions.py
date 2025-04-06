from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import status


class AccountTokenNotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = "account_token_not_found"
    default_detail = _("Account token is not found.")
