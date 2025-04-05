from django.db import models
from django.utils.translation import gettext_lazy as _


class AccountCookies(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=255,
        editable=True,
        verbose_name=_("Account cookies ID"),
    )
    account = models.ForeignKey(
        to="accounts.Account",
        on_delete=models.CASCADE,
        verbose_name=_("Account"),
    )
    encrypted_cookies = models.CharField(
        max_length=65535,
        verbose_name=_("Encrypted cookie"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated at"),
    )

    class Meta:
        verbose_name = _("Account cookies")
        verbose_name_plural = _("Account cookies")

    def __str__(self):
        return self.account.id
