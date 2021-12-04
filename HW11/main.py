import re

user = '09351234567'
regular_expression = r'^((\+989)|(09))(\d{9})$'
res = re.match(regular_expression, user)
print(res)
