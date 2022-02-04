from django.db import models
from core.models import BaseModel
from services.models import Service


class Customer(BaseModel):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)


class Agent(BaseModel):
    name = models.CharField(max_length=30)
    is_available = models.BooleanField(default=True)
    expertise = models.ForeignKey(Service, on_delete=models.CASCADE)
