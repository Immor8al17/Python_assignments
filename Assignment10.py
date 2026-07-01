import math


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def diameter(self):
        return 2 * self.radius

    def area(self):
        return math.pi * (self.radius**2)

    def circumference(self):
        return 2 * math.pi * self.radius


class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


class BankAccount:

    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, input_password):
        return self.password == input_password


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(f"Rectangle Area: {rect.area()}")
    print(f"Rectangle Perimeter: {rect.perimeter()}\n")

    circ = Circle(7)
    print(f"Circle Diameter: {circ.diameter()}")
    print(f"Circle Area: {circ.area():.2f}")
    print(f"Circle Circumference: {circ.circumference():.2f}\n")

    prod = Product("Laptop", 1200, 5)
    print(f"Total Stock Value for {prod.name}: ${prod.total_value()}\n")

    acct = BankAccount(100.0)
    acct.deposit(50.0)
    print(f"Balance after deposit: ${acct.balance}")
    withdrawal_success = acct.withdraw(200.0)
    print(f"Withdrawal of $200 successful?: {withdrawal_success}")
    print(f"Final Balance: ${acct.balance}\n")

    user = User("john_doe", "secret123")
    print(f"Password correct?: {user.check_password('wrong_pass')}")
    print(f"Password correct?: {user.check_password('secret123')}")
