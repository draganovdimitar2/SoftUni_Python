class Vehicle:

    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if money >= self.price and self.owner is None:
            self.owner = owner
            change = money - self.price
            return f"Successfully bought a {self.type}. Change: {change:.2f}"
        elif money < self.price:
            return "Sorry, not enough money"
        else:
            return "Car already sold"

    def sell(self):
        if self.owner:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:  # without else
            return f"{self.model} {self.type} is on sale: {self.price}"