def add(x, y):
    return x + y


def sub(x, y):
    return x - y


class Account:

    def __init__(self, name: str, pin: int, phone_number: str):
        self.password = pin
        self.balance = 0
        self.name = name
        self.phone_number = phone_number

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be found")
        self.balance += amount

    def withdraw(self, amount, password):
        if password is not self.password:
            raise ValueError("your password is not correct")
        if amount < 0:
            raise ValueError("your cannot withdraw amount below the balance")
        if amount > self.balance:
            raise ValueError("cannot withdraw more than the available balance")
        self.balance -= amount

    def load_airtime(self, amount, phone_number):
        if phone_number is phone_number:
            if amount < 0:
                raise ValueError("your cannot withdraw more than balance")
        if amount > self.balance:
            raise ValueError("cannot withdraw more than tha available")
        self.balance -= amount

    def add_to_account(self):
        pass
