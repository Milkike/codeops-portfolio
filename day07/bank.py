class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

        # Stack for transaction history
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(("deposit", amount))
            print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(("withdraw", amount))
            print(f"Withdrawn {amount}")
        else:
            print("Insufficient balance")

    def undo_last(self):
        if not self.history:
            print("No transaction to undo.")
            return

        action, amount = self.history.pop()

        if action == "deposit":
            self.balance -= amount
            print(f"Undo deposit of {amount}")

        elif action == "withdraw":
            self.balance += amount
            print(f"Undo withdrawal of {amount}")

    def statement(self):
        print("------------------------")
        print(f"Owner   : {self.owner}")
        print(f"Account : {self.account_number}")
        print(f"Balance : {self.balance}")
        print("------------------------")