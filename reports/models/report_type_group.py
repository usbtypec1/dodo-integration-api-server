from django.db import models
from django.utils.translation import gettext_lazy as _


class ReportTypeGroup(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Report type group name"),
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
        verbose_name = _("Report type group")
        verbose_name_plural = _("Report type groups")

    def __str__(self):
        return self.name
