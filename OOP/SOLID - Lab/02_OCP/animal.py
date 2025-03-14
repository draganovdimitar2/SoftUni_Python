from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass


class Dog(Animal):
    def make_sound(self):
        return 'woof-woof'


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Pig(Animal):
    def make_sound(self):
        return 'some pig sound'


def animal_sound(animals: list[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat(), Pig()]
animal_sound(animals)
