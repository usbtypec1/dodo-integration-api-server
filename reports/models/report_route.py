from django.db import models
from django.utils.translation import gettext_lazy as _

from reports.models.report_type import ReportType
from telegram.models.telegram_chat import TelegramChat
from units.models import Unit


class ReportRoute(models.Model):
    chat = models.ForeignKey(
        to=TelegramChat,
        on_delete=models.CASCADE,
        verbose_name=_("Telegram chat"),
        related_name="report_routes",
    )
    unit = models.ForeignKey(
        to=Unit,
        on_delete=models.CASCADE,
        verbose_name=_("Unit"),
        related_name="report_routes",
    )
    report_type = models.ForeignKey(
        to=ReportType,
        on_delete=models.CASCADE,
        verbose_name=_("Report type"),
        related_name="report_routes",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created at"),
    )

    class Meta:
        verbose_name = _("Report route")
        verbose_name_plural = _("Report routes")
        constraints = (
            models.UniqueConstraint(
                fields=["chat", "unit", "report_type"],
                name="unique_report_route",
            ),
        )
