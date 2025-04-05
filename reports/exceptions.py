from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import status


class ReportTypeNotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = "report_type_not_found"
    default_detail = _("Report type not found.")


class ReportRouteAlreadyExistsError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_code = "report_route_already_exists"
    default_detail = _("Report route already exists.")


class ReportRouteNotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = "report_route_not_found"
    default_detail = _("Report route not found.")
