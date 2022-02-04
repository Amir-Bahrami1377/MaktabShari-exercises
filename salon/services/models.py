from django.db import models
from core.models import BaseModel


class Weekend(models.Model):
    off_days = models.CharField(max_length=50)
    open_at = models.TimeField()
    close_at = models.TimeField()


class Service(BaseModel):
    name = models.CharField(max_length=30)
    cost = models.IntegerField()
    duration = models.TimeField()

