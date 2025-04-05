from django.db import models
from django.utils.translation import gettext_lazy as _

from reports.models.report_type import ReportType
from units.models.unit import Unit


class UserRole(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Role name"),
    )
    access_code = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Access code"),
    )
    report_types = models.ManyToManyField(
        to=ReportType,
        verbose_name=_("Report types"),
    )
    units = models.ManyToManyField(
        to=Unit,
        verbose_name=_("Units"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created at"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated at"),
    )

    class Meta:
        verbose_name = _("User role")
        verbose_name_plural = _("User roles")

    def __str__(self):
        return self.name
