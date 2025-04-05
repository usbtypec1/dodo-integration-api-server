from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import status


class UnitNotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = "unit_not_found"
    default_detail = _("Unit not found.")
