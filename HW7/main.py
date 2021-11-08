import sys
from quiz import starting_menu


def main_menu(user_input):
#تابع شروع کننده برنامه
    if user_input == '1':
        starting_menu()
    elif user_input == '2':
        sys.exit("bye")
    else:
        print("Invalid option\n")
        main_menu()


print("welcome \n if you are ready enter 1 to start the exam \n or if you want to stop this enter 2 ")
user_input = input(">>>> ")

main_menu(user_input)
