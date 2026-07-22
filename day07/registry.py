from bank import Account


class AccountRegistry:

    def __init__(self):
        self.accounts = {}

    def add(self, account):
        self.accounts[account.account_number] = account

    def find(self, account_number):
        return self.accounts.get(account_number)

    def list_all(self):
        return list(self.accounts.values())


# -----------------------
# Testing
# -----------------------

registry = AccountRegistry()

acc1 = Account("Almaz", "CBE-001", 1500)
acc2 = Account("Dawit", "CBE-002", 2500)
acc3 = Account("Tigist", "CBE-003", 1000)

registry.add(acc1)
registry.add(acc2)
registry.add(acc3)

print("Finding account CBE-002")

account = registry.find("CBE-002")

if account:
    account.statement()

print()

print("Depositing and withdrawing...")

acc1.deposit(500)
acc1.withdraw(200)

print()

print("Transaction History")

print(acc1.history)

print()

print("Undo Last Transaction")

acc1.undo_last()

print()

acc1.statement()

print()

print("All Accounts")

for account in registry.list_all():
    account.statement()