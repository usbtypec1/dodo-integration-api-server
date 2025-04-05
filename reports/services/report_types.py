from reports.exceptions import ReportTypeNotFoundError
from reports.models.report_type import ReportType


def get_report_type_by_id(report_type_id: str) -> ReportType:
    try:
        return ReportType.objects.get(id=report_type_id)
    except ReportType.DoesNotExist:
        raise ReportTypeNotFoundError
