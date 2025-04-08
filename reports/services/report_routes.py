from collections.abc import Iterable
from dataclasses import dataclass
from uuid import UUID

from django.core.exceptions import ValidationError

from reports.exceptions import (
    ReportRouteAlreadyExistsError,
    ReportRouteNotFoundError,
)
from reports.models import ReportRoute, ReportType
from telegram.models import TelegramChat
from units.models import Unit


@dataclass(frozen=True, slots=True, kw_only=True)
class ReportRouteListItemDto:
    report_type_id: str
    report_type_name: str
    unit_id: UUID
    chat_id: int


@dataclass(frozen=True, slots=True, kw_only=True)
class ReportRouteListDto:
    routes: list[ReportRouteListItemDto]
    is_end_of_list_reached: bool


def delete_report_route(
        *,
        report_type_id: str,
        unit_legacy_id: int,
        chat_id: int,
) -> None:
    deleted_count, _ = ReportRoute.objects.filter(
        unit__legacy_id=unit_legacy_id,
        report_type_id=report_type_id,
        chat_id=chat_id,
    ).delete()
    if deleted_count == 0:
        raise ReportRouteNotFoundError


def create_report_route(
        report_type: ReportType,
        unit: Unit,
        chat: TelegramChat,
) -> ReportRoute:
    route = ReportRoute(
        report_type=report_type,
        unit=unit,
        chat=chat,
    )
    try:
        route.full_clean()
    except ValidationError as error:
        if 'already exists' in error.messages[0]:
            raise ReportRouteAlreadyExistsError
        raise
    route.save()
    return route


def get_report_routes(
        *,
        report_type_id: str | None,
        unit_id: UUID | None,
        chat_ids: Iterable[int] | None,
        take: int,
        skip: int,
) -> ReportRouteListDto:
    routes = (
        ReportRoute.objects
        .order_by('-created_at')
        .select_related('report_type')
    )
    if report_type_id is not None:
        routes = routes.filter(report_type_id=report_type_id)
    if unit_id is not None:
        routes = routes.filter(unit_id=unit_id)
    if chat_ids is not None:
        routes = routes.filter(chat_id__in=chat_ids)

    routes = routes[skip:skip + take + 1]
    is_end_of_list_reached = len(routes) <= take
    routes = routes[:take]

    return ReportRouteListDto(
        routes=[
            ReportRouteListItemDto(
                report_type_id=route.report_type_id,
                report_type_name=route.report_type.name,
                unit_id=route.unit_id,
                chat_id=route.chat_id,
            )
            for route in routes
        ],
        is_end_of_list_reached=is_end_of_list_reached,
    )
