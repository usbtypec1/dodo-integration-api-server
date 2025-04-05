from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models.account import Account


class AccountTokens(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=255,
        editable=True,
        verbose_name=_("Account tokens ID"),
    )
    account = models.ForeignKey(
        to=Account,
        on_delete=models.CASCADE,
        verbose_name=_("Account"),
    )
    encrypted_access_token = models.CharField(
        max_length=255,
        verbose_name=_("Encrypted access token"),
    )
    encrypted_refresh_token = models.CharField(
        max_length=255,
        verbose_name=_("Encrypted refresh token"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated at"),
    )

    class Meta:
        verbose_name = _("Account token")
        verbose_name_plural = _("Account tokens")

    def __str__(self):
        return self.account.id
