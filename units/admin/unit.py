from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource

from units.models.unit import Unit


class UnitResource(ModelResource):
    class Meta:
        model = Unit


@admin.register(Unit)
class UnitAdmin(ImportExportModelAdmin):
    resource_class = UnitResource
    list_display = ('id', 'name')
    list_filter = ('group',)
