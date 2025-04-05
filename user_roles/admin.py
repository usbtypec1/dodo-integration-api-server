from django.contrib import admin

from user_roles.models import UserRole


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    filter_horizontal = ('units', 'report_types')
