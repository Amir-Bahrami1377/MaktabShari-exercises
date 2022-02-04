from django.db import models
from core.models import BaseModel
from services.models import Service


class Customer(BaseModel):
    username = models.CharField()
    email = models.EmailField()
    password = models.CharField()


class Agent(BaseModel):
    name = models.CharField()
    is_available = models.BooleanField(default=True)
    expertise = models.ForeignKey(Service, on_delete=models.CASCADE)
