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
        print(f"[Account] {self.owner}: {self.balance} ETB")



class SavingsAccount(Account):

    def __init__(self, owner, number, balance=0, rate=0.05):
        super().__init__(owner, number, balance)
        self.rate = rate


    def add_interest(self):
        self.deposit(self.balance * self.rate)


    def statement(self):
        print(f"[Savings] {self.owner}: {self.balance} ETB")



class CurrentAccount(Account):

    def __init__(self, owner, number, balance=0, overdraft=1000):
        super().__init__(owner, number, balance)
        self.overdraft = overdraft


    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive")

        if self.balance - amount < -self.overdraft:
            raise ValueError("Overdraft limit exceeded")

        self._Account__balance -= amount


    def statement(self):
        print(f"[Current] {self.owner}: {self.balance} ETB")



accounts = [
    Account("Milki", "1001", 1500),
    SavingsAccount("Almaz", "1002", 2000),
    CurrentAccount("Dawit", "1003", 500)
]


for acc in accounts:
    acc.statement()