from dataclasses import dataclass

from reports.services.report_routes import create_report_route
from reports.services.report_types import get_report_type_by_id
from telegram.services.chats import get_telegram_chat_by_id
from units.services.units import get_unit_by_legacy_id


@dataclass(frozen=True, slots=True, kw_only=True)
class ReportRouteCreateUseCase:
    report_type_id: str
    unit_legacy_id: int
    chat_id: int

    def execute(self) -> None:
        report_type = get_report_type_by_id(self.report_type_id)
        chat = get_telegram_chat_by_id(self.chat_id)
        unit = get_unit_by_legacy_id(self.unit_legacy_id)
        create_report_route(
            report_type=report_type,
            chat=chat,
            unit=unit,
        )
