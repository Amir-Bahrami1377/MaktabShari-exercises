from django.db import models
from core.models import BaseModel
from users.models import Agent, Customer


class Booking(BaseModel):
    person_counts = models.IntegerField()
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    total_cost = models.IntegerField()
    is_paid = models.BooleanField()
    agent_id = models.ForeignKey(Agent, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
