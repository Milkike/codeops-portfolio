class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        print(f"{self.title} by {self.author} - {self.pages} pages")


book1 = Book("Python Basics", "John", 250)
book2 = Book("Clean Code", "Robert Martin", 464)

book1.describe()
book2.describe()


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def restock(self, n):
        if n <= 0:
            raise ValueError("Amount must be positive")
        self.__quantity += n

    def sell(self, n):
        if n <= 0:
            raise ValueError("Amount must be positive")

        if n > self.__quantity:
            raise ValueError("Not enough stock")

        self.__quantity -= n


p1 = Product("Phone", 30000, 10)
p2 = Product("Laptop", 70000, 20)
p3 = Product("Tablet", 25000, 15)

p1.sell(5)

print(p1.quantity)
print(p2.quantity)
print(p3.quantity)