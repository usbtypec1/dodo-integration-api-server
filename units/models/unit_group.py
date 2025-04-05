from django.db import models
from django.utils.translation import gettext_lazy as _


class UnitGroup(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name=_("Unit group name"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created at"),
    )

    class Meta:
        verbose_name = _("Unit group")
        verbose_name_plural = _("Unit groups")

    def __str__(self):
        return self.name
