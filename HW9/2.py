num = input("Enter a number: ")


def sum_gen(number):
    for item in range(len(number)):
        yield int(number[item]) ** 3


jam = 0
for i in sum_gen(num):
    jam += i
print(jam)

if int(num) == jam:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

"""
A positive integer is called an Armstrong number of order n if

abcd... = an + bn + cn + dn + ...
In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. For example:

153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.
"""
