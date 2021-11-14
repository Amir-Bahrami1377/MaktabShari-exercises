class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class BankAccount:

    def __init__(self, owner, balance, account_id):
        self.owner = owner
        self.balance = balance
        self.account_id = account_id

    def __str__(self):
        return f'Hi {self.owner} welcome. your account balance is {self.balance}'

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
