from collections.abc import Iterable
from dataclasses import dataclass
from uuid import UUID

from reports.models import ReportType
from telegram.models import TelegramUser
from telegram.services.users import get_telegram_user_by_id
from units.models import Unit
from user_roles.services import (
    get_telegram_user_report_types,
    get_telegram_user_units,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class UnitDto:
    id: UUID
    name: str
    legacy_id: int


@dataclass(frozen=True, slots=True, kw_only=True)
class ReportType:
    id: str
    name: str


@dataclass(frozen=True, slots=True, kw_only=True)
class RoleDto:
    name: str
    units: list[UnitDto]
    report_types: list[ReportType]


@dataclass(frozen=True, slots=True, kw_only=True)
class TelegramUserRetrieveResultDto:
    id: int
    full_name: str
    username: str | None
    role: RoleDto | None


def map_to_dto(
        *,
        user: TelegramUser,
        units: Iterable[Unit],
        report_types: Iterable[ReportType],
) -> TelegramUserRetrieveResultDto:
    role = None
    if user.role is not None:
        role = RoleDto(
            name=user.role.name,
            units=[
                UnitDto(
                    id=unit.id,
                    name=unit.name,
                    legacy_id=unit.legacy_id,
                )
                for unit in units
            ],
            report_types=[
                ReportType(
                    id=report_type.id,
                    name=report_type.name,
                )
                for report_type in report_types
            ],
        )
    return TelegramUserRetrieveResultDto(
        id=user.id,
        full_name=user.full_name,
        username=user.username,
        role=role,
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class TelegramUserRetrieveUseCase:
    user_id: int

    def execute(self):
        user = get_telegram_user_by_id(self.user_id)
        units = get_telegram_user_units(user)
        report_types = get_telegram_user_report_types(user)
        return map_to_dto(
            user=user,
            units=units,
            report_types=report_types,
        )
