from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import AccountCookies, AccountTokens
from units.models.department import Department
from units.models.unit_group import UnitGroup


class Unit(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=True,
        verbose_name=_("Unit ID"),
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name=_("Unit name")
    )
    legacy_id = models.PositiveIntegerField(verbose_name=_("Unit legacy ID"))
    group = models.ForeignKey(
        to=UnitGroup,
        on_delete=models.CASCADE,
        related_name="report_types",
        verbose_name=_("Unit group"),
    )
    dodo_is_api_account_tokens = models.ForeignKey(
        to=AccountTokens,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="report_types",
        verbose_name=_("Dodo IS API account tokens"),
    )
    office_manager_account_cookies = models.ForeignKey(
        to=AccountCookies,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="office_manager_units",
        verbose_name=_("Office manager account cookies"),
    )
    shift_manager_account_cookies = models.ForeignKey(
        to=AccountCookies,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="shift_manager_units",
        verbose_name=_("Shift manager account cookies"),
    )
    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
        related_name="report_types",
        verbose_name=_("Department"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created at"),
    )

    class Meta:
        verbose_name = _("Unit")
        verbose_name_plural = _("Units")

    def __str__(self):
        return self.name
