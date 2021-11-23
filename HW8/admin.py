#!/usr/bin/env python

import sys
import pickle
from models import User


if "createsuperuser" in sys.argv:
    fullname = input("Enter Fullname : ")
    password = input("Enter Password : ")
    phone = input("enter your phone number: ")
    admin = User(full_name=fullname, password=password, phone=phone, is_admin=True)

with open('users.pk', 'ab') as f:
    pickle.dump(admin, f)
