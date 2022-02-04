from django.db import models
from core.models import BaseModel


class Weekend(models.Model):
    off_days = models.CharField()
    open_at = models.TimeField()
    close_at = models.TimeField()


class Service(BaseModel):
    name = models.CharField()
    cost = models.IntegerField()
    duration = models.TimeField()

