from project.astronauts.base_astronaut import BaseAstronaut
from abc import ABC, abstractmethod
from typing import List, Type
import re


class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts: List[Type[BaseAstronaut]] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not re.match(r'^[a-zA-Z0-9-]+$', value):  # only letters, numbers, and hyphens
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value

    def calculate_total_salaries(self):
        total_salaries = sum([a.salary for a in self.astronauts])
        return f"{total_salaries:.2f}"

    def status(self):  # TODO
        astronaut_ids = " #".join(sorted(astronaut.id_number for astronaut in self.astronauts)) or "N/A"
        total_salaries = self.calculate_total_salaries()
        return f"Station name: {self.name}; Astronauts: {astronaut_ids}; Total salaries: {total_salaries}"

    @abstractmethod
    def update_salaries(self, min_value: float):  # TODO
        pass
