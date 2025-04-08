from collections.abc import Iterable
from dataclasses import dataclass
from uuid import UUID

from reports.services.report_routes import (
    get_report_routes,
    ReportRouteListDto,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class ReportRouteListUseCase:
    report_type_id: str | None
    unit_id: UUID | None
    chat_ids: Iterable[int] | None
    take: int
    skip: int

    def execute(self) -> ReportRouteListDto:
        return get_report_routes(
            report_type_id=self.report_type_id,
            unit_id=self.unit_id,
            chat_ids=self.chat_ids,
            take=self.take,
            skip=self.skip,
        )
