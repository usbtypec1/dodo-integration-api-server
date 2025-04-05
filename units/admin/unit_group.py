from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource

from units.models.unit_group import UnitGroup


class UnitGroupResource(ModelResource):
    class Meta:
        model = UnitGroup


@admin.register(UnitGroup)
class UnitGroupAdmin(ImportExportModelAdmin):
    resource_class = UnitGroupResource
    list_filter = ('name',)
