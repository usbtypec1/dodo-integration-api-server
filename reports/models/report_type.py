from django.db import models
from django.utils.translation import gettext_lazy as _

from reports.models.report_type_group import ReportTypeGroup


class ReportType(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=255,
        verbose_name=_("Report type ID"),
    )
    name = models.CharField(max_length=255, verbose_name=_("Report type name"))
    group = models.ForeignKey(
        to=ReportTypeGroup,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="report_types",
        verbose_name=_("Report type group"),
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
        verbose_name = _("Report type")
        verbose_name_plural = _("Report types")

    def __str__(self):
        return self.name
