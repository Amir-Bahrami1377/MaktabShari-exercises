from datetime import datetime
from random import randint
from enum import Enum


class User:
    def __init__(
            self,
            full_name: str,
            phone: str,
            balance: int = 0,
            password: str = None,
            is_admin: bool = False,
            cart=None
    ):
        self.full_name = full_name
        self.phone = phone
        self.id = full_name + str(randint(10000, 99999))
        self.is_admin = is_admin
        self.balance = balance
        self.password = password
        self.cart = cart

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        if self.balance < amount:
            raise ValueError
        self.balance -= amount

    def __str__(self):
        return f"{self.id} | {self.full_name} | {self.balance} | {self.is_admin}"


class Trip:
    def __init__(self, destination, cost, duration, origin_station):
        self.destination = destination
        self.cost = cost
        self.duration = duration
        self.origin_station = origin_station


class TicketType(str, Enum):
    TAK_SAFARE = 'tak_safare'
    CREDIT = 'credit'
    CREDIT_DATE = 'credit_date'


class Ticket:
    def __init__(self, cart_type: TicketType = TicketType.TAK_SAFARE, expire_date: datetime = None, balance: int = None, ticket_id: int=None):
        self.cart_type = cart_type
        self.expire_date = expire_date
        self.balance = balance
        if not ticket_id:
            self.id = randint(1000000, 9999999)
        else:
            self.id = ticket_id

    def charge_cart(self, amount: int):
        self.balance += amount

    def trip_cost_calculation(self, cost):
        if self.balance < cost:
            raise ValueError
        self.balance -= cost
