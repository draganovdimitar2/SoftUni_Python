from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    CONSUMPTION_INCREASE = 0.9

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption + self.CONSUMPTION_INCREASE) * distance
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONSUMPTION_INCREASE = 1.6

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption + self.CONSUMPTION_INCREASE) * distance
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 95) / 100
