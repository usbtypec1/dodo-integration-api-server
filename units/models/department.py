from django.db import models
from django.utils.translation import gettext_lazy as _


class Department(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=True,
        verbose_name=_("Department ID"),
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name=_("Department name")
    )
    legacy_id = models.PositiveIntegerField(
        verbose_name=_("Department legacy ID"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created at"),
    )

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")

    def __str__(self):
        return self.name
