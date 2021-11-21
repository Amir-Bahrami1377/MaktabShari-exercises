#!/usr/bin/env python

import sys
from models import User

# TODO save user as pickled object in users
if "createsuperuser" in sys.argv:
    fullname = input("Enter Fullname : ")
    password = input("Enter Password : ")
    admin = User(full_name=fullname, password=password, phone="15151961", is_admin=True)