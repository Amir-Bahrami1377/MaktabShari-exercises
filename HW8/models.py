from typing import NoReturn


class BankAccount:

    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def __str__(self):
        return f'Hi your account balance is {self.balance}'

    def deposit(self, amount: float):
        self.balance += amount
        print(f'Job done \nYour new balance is: {self.balance}')

    def withdraw(self, amount: float):
        if amount > self.balance:
            print('Insufficient Balance!')
        else:
            self.balance -= amount
            if self.balance < 10:
                self.balance += amount
                print('Sorry, minimum amount in your account have to be 10$')
            else:
                print(f'Job done \nYour remaining balance is: {self.balance}')


class MetroCard:
    pass


class CreditCard(MetroCard):
    pass


class DisposableCard(MetroCard):
    pass


class CreditCardWithExpireDate(CreditCard):
    pass


class Travel:
    def __init__(self, beginning, destination, time, price):
        self.beginning_location = beginning
        self.destination_location = destination
        self.travel_time = time
        self.price = price


class User:
    user_id: str

    def __init__(self, name: str, phone: str) -> NoReturn:
        self.name = name
        self.phone = phone
        self.user_id = name.lower() + phone[8:11]
        self.bank_account = None

    def get_id(self):
        return f"your id in our system is {self.user_id} \n please try to remember it"

    def set_bank_account(self, balance):
        self.bank_account = BankAccount(self.user_id, balance)
        return self.bank_account

    def buy_ticket(self):
        pass