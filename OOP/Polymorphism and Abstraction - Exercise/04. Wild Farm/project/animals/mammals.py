from project.animals.animal import Mammal
from project.food import Meat, Fruit, Vegetable, Food
from typing import List, Type


class Mouse(Mammal):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Fruit, Vegetable]

    @property
    def weight_coefficient(self) -> float:
        return 0.10

    @staticmethod
    def make_sound() -> str:
        return "Squeak"


class Dog(Mammal):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_coefficient(self) -> float:
        return 0.4

    @staticmethod
    def make_sound() -> str:
        return "Woof!"


class Cat(Mammal):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat, Vegetable]

    @property
    def weight_coefficient(self) -> float:
        return 0.3

    @staticmethod
    def make_sound() -> str:
        return "Meow"


class Tiger(Mammal):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_coefficient(self) -> float:
        return 1.00

    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"
