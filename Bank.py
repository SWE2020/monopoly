class Bank:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance


"""
Test Cases:
bank1 = Bank(100)
print(bank1.get_balance() == 100)
bank1.withdraw(20)
print(bank1.get_balance() == 80)
bank1.deposit(20)
print(bank1.get_balance() == 100)
"""
