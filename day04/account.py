class Account:

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient funds")

        self.__balance -= amount

    def statement(self):
        print("----- Account Statement -----")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.__balance} ETB")


acc1 = Account("Milki Kenasa", "1001", 1500)
acc2 = Account("Almaz Bekele", "1002", 500)

acc1.deposit(500)
acc1.withdraw(200)

acc1.statement()
acc2.statement()


acc1 = Account("Milki Kenasa", "1001", 1500)
acc2 = Account("Almaz Bekele", "1002", 500)

acc1.deposit(500)
acc1.withdraw(200)

acc1.statement()
acc2.statement()