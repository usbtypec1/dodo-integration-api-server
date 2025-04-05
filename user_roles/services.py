from collections.abc import Iterable
from uuid import UUID

from reports.models import ReportType
from telegram.models import TelegramUser
from units.models import Unit
from user_roles.exceptions import UserRoleNotFoundError
from user_roles.models import UserRole


def get_user_role_by_access_code(access_code: str) -> UserRole:
    try:
        return UserRole.objects.get(access_code=access_code)
    except UserRole.DoesNotExist:
        raise UserRoleNotFoundError


def get_telegram_user_units(user: TelegramUser) -> list[Unit]:
    if user.role is None:
        return []
    return list(
        user.role.units
        .select_related('group')
        .only('id', 'name', 'group__id', 'group__name')
    )


def get_telegram_user_report_types(user: TelegramUser) -> list[ReportType]:
    if user.role is None:
        return []
    return list(
        user.role.report_types
        .select_related('group')
        .only('id', 'name', 'group__id', 'group__name')
    )
