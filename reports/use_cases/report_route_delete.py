from dataclasses import dataclass

from reports.services.report_routes import delete_report_route


@dataclass(frozen=True, slots=True, kw_only=True)
class ReportRouteDeleteUseCase:
    report_type_id: str
    unit_legacy_id: int
    chat_id: int

    def execute(self) -> None:
        delete_report_route(
            report_type_id=self.report_type_id,
            unit_legacy_id=self.unit_legacy_id,
            chat_id=self.chat_id,
        )
