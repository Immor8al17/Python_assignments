class Temperature:

    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15


class InterestCalculator:

    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def simple_interest(self):
        return (self.principal * self.rate * self.time) / 100

    def compound_interest(self):
        return self.principal * ((1 + self.rate / 100) ** self.time) - self.principal


class CoffeeMachine:

    def __init__(self, water=300, coffee=100, milk=200):
        self.water = water
        self.coffee = coffee
        self.milk = milk

    def make_latte(self):
        req_water = 200
        req_coffee = 20g
        req_milk = 150

        if self.water < req_water:
            print("Sorry, not enough water.")
            return False
        if self.coffee < req_coffee:
            print("Sorry, not enough coffee.")
            return False
        if self.milk < req_milk:
            print("Sorry, not enough milk.")
            return False

        self.water -= req_water
        self.coffee -= req_coffee
        self.milk -= req_milk
        print("Latte is ready! Enjoy your coffee.")
        return True


class Vehicle:

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display(self):
        print(f"Vehicle Name: {self.name}, Max Speed: {self.max_speed} km/h")


class Bus(Vehicle):

    def __init__(self, name, max_speed, seating_capacity, total_reservations=0):
        super().__init__(name, max_speed)
        self.seating_capacity = seating_capacity
        self.total_reservations = total_reservations

    def display(self):
        super().display()
        print(
            f"Seating Capacity: {self.seating_capacity}, Reserved Seats: {self.total_reservations}"
        )


if __name__ == "__main__":
    t = Temperature(25)
    print(f"25C to Fahrenheit: {t.to_fahrenheit()}")
    print(f"25C to Kelvin: {t.to_kelvin()}\n")

    ic = InterestCalculator(1000, 5, 2)
    print(f"Simple Interest: {ic.simple_interest()}")
    print(f"Compound Interest: {ic.compound_interest():.2f}\n")

    cm = CoffeeMachine()
    cm.make_latte()
    cm.make_latte()

    b = Bus("City Express", 120, 50, 12)
    b.display()
