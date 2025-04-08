from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from reports.models import ReportType, ReportTypeGroup, ReportRoute


@admin.register(ReportType)
class ReportTypeAdmin(ImportExportModelAdmin):
    pass


@admin.register(ReportRoute)
class ReportRouteAdmin(ImportExportModelAdmin):
    pass


@admin.register(ReportTypeGroup)
class ReportTypeGroupAdmin(ImportExportModelAdmin):
    pass
