# ==========================================
# Day 8 - DSA II
# Registry with Search & Sorting
# ==========================================

class Account:
    def __init__(self, number, owner, balance=0):
        self.number = number
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(amount)

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.history.append(-amount)

    def __str__(self):
        return f"{self.number} | {self.owner} | Balance: ${self.balance}"


# ==========================================
# Binary Search
# ==========================================

def binary_search(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2

        if items[mid] == target:
            return mid

        elif items[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# ==========================================
# Account Registry
# ==========================================

class AccountRegistry:

    def __init__(self):
        self.by_number = {}

    # O(1)
    def add(self, account):
        self.by_number[account.number] = account

    # O(1)
    def find(self, number):
        return self.by_number.get(number)

    # Ordered Accounts
    def list_all(self):
        accounts = sorted(
            self.by_number.values(),
            key=lambda a: a.number
        )

        for account in accounts:
            print(account)

    # Leaderboard
    def top_by_balance(self, n=5):
        return sorted(
            self.by_number.values(),
            key=lambda a: a.balance,
            reverse=True
        )[:n]

    # O(log n)
    def find_by_number(self, number):

        numbers = sorted(self.by_number.keys())

        index = binary_search(numbers, number)

        if index == -1:
            return None

        return self.by_number[numbers[index]]

    # Recursive Total
    def total_transactions(self, account):

        def total(history):

            if len(history) == 0:
                return 0

            return history[0] + total(history[1:])

        return total(account.history)


# ==========================================
# Testing
# ==========================================

registry = AccountRegistry()

a1 = Account(1001, "Milki", 1500)
a2 = Account(1002, "Abebe", 5000)
a3 = Account(1003, "Almaz", 2500)
a4 = Account(1004, "Dawit", 1000)
a5 = Account(1005, "Sara", 8000)

registry.add(a1)
registry.add(a2)
registry.add(a3)
registry.add(a4)
registry.add(a5)

a1.deposit(500)
a1.withdraw(200)

a2.deposit(1000)
a2.withdraw(500)

a3.deposit(300)
a3.withdraw(100)

print("========== ALL ACCOUNTS ==========")
registry.list_all()

print("\n========== TOP 3 BALANCES ==========")

for account in registry.top_by_balance(3):
    print(account)

print("\n========== BINARY SEARCH ==========")

account = registry.find_by_number(1003)

if account:
    print("Found:", account)
else:
    print("Not Found")

print("\n========== TOTAL TRANSACTIONS ==========")

print("Milki:", registry.total_transactions(a1))
print("Abebe:", registry.total_transactions(a2))
print("Almaz:", registry.total_transactions(a3))