from database_manager.manager import DBModel, DBManager
from datetime import datetime
from random import randint
from enum import Enum
from abc import ABC


class Users(DBModel):
    def __init__(self, full_name: str, phone: str, balance: int = 0):
        self.full_name = full_name
        self.username = full_name + str(randint(10000, 99999))
        self.phone = phone
        self.balance = balance

    TABLE = "users"
    PK = "username"

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        if self.balance < amount:
            raise ValueError
        self.balance -= amount

    def __str__(self):
        return f"username: {self.username} | name: {self.full_name} | balance: {self.balance}"


class SuperUser(Users, DBModel):
    def __init__(self, full_name: str, phone: str, password: str, balance: int = 0):
        super().__init__(full_name, phone, balance)
        self._password = password

    TABLE = "superuser"
    PK = "username"


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
    def __init__(self, card_type: TicketType = TicketType.TAK_SAFARE, expire_date: datetime = None, balance: int = None, id=None):
        self.cart_type = card_type
        self.expire_date = expire_date
        self.balance = balance
        if id:
            self.id = id

    def charge_cart(self, amount: int):
        self.balance += amount

    def trip_cost_calculation(self, cost):
        if self.balance < cost:
            raise ValueError
        self.balance -= cost


dbmanager = DBManager()
amir = Users("amirhosein", "09354468749", 5000)
dbmanager.create(amir)
