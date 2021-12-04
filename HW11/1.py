import re


def check_user(user):
    regular_expression = r'\w{4,14}$'
    res = re.match(regular_expression, user)
    return True if res else False


def check_email(email):
    regular_expression = r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.][a-z]{2,5}$'
    res = re.match(regular_expression, email)
    return True if res else False


def check_phone(phone):
    regular_expression = r'((\+989)|(09))(\d{9})$'
    res = re.match(regular_expression, phone)
    return True if res else False


#print(check_user('amirB'), check_email('amir.bk@gmail.com'), check_phone('09351234567'))
