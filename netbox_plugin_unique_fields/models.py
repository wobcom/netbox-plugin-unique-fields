from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from utilities.querysets import RestrictedQuerySet
from netbox.models import ChangeLoggedModel

__all__ = (
    'SID',
)


class SID(ChangeLoggedModel):

    sid = models.PositiveIntegerField(
        blank=False,
        null=False,
        unique=True,
        verbose_name="SID",
        validators=[
            MinValueValidator(524288),
            MaxValueValidator(526336),
        ],

    )


    device = models.OneToOneField(
        to='dcim.Device',
        on_delete=models.CASCADE,
        related_name='sid',
        blank=True,
        null=True,
    )

    objects = RestrictedQuerySet.as_manager()

    class Meta:
        verbose_name = 'SID'
        verbose_name_plural = 'SIDs'

    def __str__(self):
        return str(self.sid)
