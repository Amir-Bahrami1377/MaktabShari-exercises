import sys

from quiz import starting_menu
from models import User


user = None


def main_menu(user_input, user: User = user):
    """
    initial method
    """
    if user_input == '1':
        user = starting_menu(user)
    elif user_input == '2':
        if user:
            print(user.__str__())
        else:
            print("please take the test first")
    else:
        sys.exit()
    print("\n1)Take the test\n2)See your score\n3)Exit\n")
    main_menu(input(), user)


user_input = input("Welcome...\n1)Take the test\n2)See your score\n3)Exit\n")
main_menu(user_input, user)