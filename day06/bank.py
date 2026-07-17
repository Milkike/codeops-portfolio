class BankConfig:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000

        return cls._instance



class SMSAlert:

    def update(self, event):
        print(f"[SMS] {event}")



class AuditLog:

    def update(self, event):
        print(f"[LOG] {event}")



class Account:

    def __init__(self, owner, number, balance=0):

        self.owner = owner
        self.number = number
        self.__balance = balance
        self.observers = []


    @property
    def balance(self):
        return self.__balance


    def subscribe(self, observer):
        self.observers.append(observer)


    def _notify(self, event):

        for observer in self.observers:
            observer.update(event)


    def deposit(self, amount):

        self.__balance += amount
        self._notify(f"+{amount} ETB deposited")


    def withdraw(self, amount):

        self.__balance -= amount
        self._notify(f"-{amount} ETB withdrawn")



class SavingsAccount(Account):

    def add_interest(self):

        config = BankConfig()

        self.deposit(
            self.balance * config.interest_rate
        )



class CurrentAccount(Account):

    def withdraw(self, amount):

        config = BankConfig()

        if self.balance - amount < -config.overdraft_limit:
            raise ValueError("Overdraft exceeded")

        super().withdraw(amount)



class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance=0):

        if kind == "savings":
            return SavingsAccount(owner, number, balance)

        if kind == "current":
            return CurrentAccount(owner, number, balance)

        raise ValueError("Unknown account type")



acc = AccountFactory.create(
    "savings",
    "Milki",
    "1001",
    2000
)


acc.subscribe(SMSAlert())
acc.subscribe(AuditLog())


acc.deposit(500)
acc.withdraw(300)


config1 = BankConfig()
config2 = BankConfig()

print(config1 is config2)