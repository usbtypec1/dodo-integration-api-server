from django.db import models
from django.utils.translation import gettext_lazy as _


class TelegramChat(models.Model):
    id = models.BigIntegerField(
        primary_key=True,
        editable=True,
        verbose_name=_('Telegram ID'),
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Telegram title'),
    )
    username = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Telegram username'),
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
        verbose_name = _('Telegram chat')
        verbose_name_plural = _('Telegram chats')

    def __str__(self):
        if self.username is not None:
            return f'@{self.username}'
        return self.title
