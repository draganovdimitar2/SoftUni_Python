from typing import List, Union
from project.worker import Worker
from project.animals import Animal


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price) -> str:
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animals"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name) -> str:
        w = next((w for w in self.workers if w.name == worker_name), None)
        if w:
            self.workers.remove(w)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries = sum(worker.salary for worker in self.workers)

        if total_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        total_price = sum(a.money_for_care for a in self.animals)
        if total_price > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_price
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        # tigers = []
        # lions = []
        # cheetahs = []
        #
        # for animals in self.animals:
        #     if animals.__class__.__name__ == "Tiger":
        #         tigers.append(repr(animals))
        #     elif animals.__class__.__name__ == "Lion"
        #         lions.append(repr(animals))
        #     else:
        #         cheetahs.append(repr(animals))
        #
        # result = [f"You have {len(tigers) + len(lions) + len(cheetahs)} animals", f"----- {len(lions)} Lions:"]
        # result.extend(lions)
        # result.append(f"----- {len(tigers)} Tigers:")
        # result.extend(tigers)
        # result.append(f"----- {len(cheetahs)} Cheetahs:")
        # result.extend(cheetahs)
        #
        # return "\n".join(result)
        return self.__print_status(self.animals, "Lion", "Tiger", "Cheetah")

    def workers_status(self):
        return self.__print_status(self.workers, "Keeper", "Caretaker", "Vet")

    @staticmethod
    def __print_status(category: List[Union[Animal, Worker]], *args) -> str:
        elements = {arg: [] for arg in args}
        for element in category:
            elements[element.__class__.__name__].append(repr(element))
        result = [f"You have {len(category)} {str(category[0].__class__.__bases__[0].__name__).lower()}s"]
        for key in args:
            value = elements[key]
            result.append(f"----- {len(value)} {key}s:")
            result.extend(value)
        return "\n".join(result)
