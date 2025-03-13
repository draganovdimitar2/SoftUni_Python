from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def calculate_area(self):
        return math.pi * self.__radius * self.__radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius

    def __init__(self, radius):
        self.__radius = radius


class Rectangle(Shape):
    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)

    def __init__(self, height, width):
        self.__height = height
        self.__width = width
