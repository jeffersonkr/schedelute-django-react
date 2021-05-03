from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import JSONField


class Schedelute(models.Model):
    date = models.DateField()
    schedule_time = models.TimeField()
    title = models.CharField(max_length=100)
    doctor = models.ForeignKey(
        "Doctor",
        on_delete=models.CASCADE,
    )


class Doctor(models.Model):
    class Expertise(models.TextChoices):
        GENERAL = "GNL", _("Clínico Geral")
        PEDIATRICIAN = "PDN", _("Pediatra")
        CARDIOLOGIST = "CDT", _("Cardiologista")

    name = models.CharField(max_length=50)
    expertise = models.CharField(
        max_length=3,
        choices=Expertise.choices,
        default=Expertise.GENERAL,
    )
    schedule_times = JSONField()
