import re


def check_user(user):
    regular_expression = r'\w{4,14}$'
    res = re.match(regular_expression, user)
    if res:
        return True
    else:
        return False


def check_email(email):
    regular_expression = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.][a-z]{2,5}$'
    res = re.match(regular_expression, email)
    if res:
        return True
    else:
        return False


def check_phone(phone):
    regular_expression = r'^((\+989)|(09))(\d{9})$'
    if re.match(regular_expression, phone):
        return True
    else:
        return False


#print(check_user('amirB'), check_email('amir.bk@gmail.com'), check_phone('09351234567'))
