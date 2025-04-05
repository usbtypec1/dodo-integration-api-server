from django.db import models
from django.utils.translation import gettext_lazy as _

from user_roles.models import UserRole


class TelegramUser(models.Model):
    id = models.BigIntegerField(
        primary_key=True,
        editable=True,
        verbose_name=_('Telegram ID'),
    )
    full_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Telegram full name'),
    )
    username = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Telegram username'),
    )
    role = models.ForeignKey(
        to=UserRole,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_('User role'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at'),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated at'),
    )

    class Meta:
        verbose_name = _('Telegram user')
        verbose_name_plural = _('Telegram users')

    def __str__(self):
        if self.username is not None:
            return f'@{self.username}'
        return self.full_name
