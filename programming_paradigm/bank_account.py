class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance


    def deposit(self, amount):
        current_balance = self.account_balance + amount
        print(current_balance)

    def withdraw(self, amount):
        if amount > self.account_balance:
            raise ValueError("Insufficient funds")
        curent_balance = self.account_balance - amount
        print(curent_balance)

    def display_balance(self):
        return self.account_balance