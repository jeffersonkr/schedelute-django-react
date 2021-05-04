from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import JSONField


class Schedule(models.Model):
    schedule_date = models.DateField()
    schedule_time = models.TimeField()
    title = models.CharField(max_length=100)
    doctor = models.ForeignKey(
        "Doctor",
        on_delete=models.CASCADE,
    )


class Doctor(models.Model):
    class Expertise(models.TextChoices):
        GENERAL = "Clínico Geral"
        PEDIATRICIAN = "Pediatra"
        CARDIOLOGIST = "Cardiologista"

    name = models.CharField(max_length=50)
    expertise = models.CharField(
        max_length=50,
        choices=Expertise.choices,
        default=Expertise.GENERAL,
    )
    schedule_work_time = JSONField()

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
