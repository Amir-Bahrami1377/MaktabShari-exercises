import sys


number = sys.argv[1:]
int_number = list(map(int, number))
average = sum(int_number)/len(int_number)
print(average)
