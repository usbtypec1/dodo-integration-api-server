from django.db import models
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=255,
        editable=True,
        verbose_name=_("Account ID"),
    )
    login = models.CharField(
        max_length=255,
        verbose_name=_("Account login"),
    )
    encrypted_password = models.CharField(
        max_length=255,
        verbose_name=_("Encrypted password"),
    )

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    def __str__(self):
        return self.id
