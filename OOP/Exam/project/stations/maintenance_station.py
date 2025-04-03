from project.stations.base_station import BaseStation


class MaintenanceStation(BaseStation):
    INITIAL_AVAILABLE_CAPACITY = 3
    UPDATE_SALARY_ASTRONAUTS_TYPES = "engineer"
    SALARY_INCREASE = 3000.0

    def __init__(self, name: str):
        super().__init__(name, capacity=self.INITIAL_AVAILABLE_CAPACITY)

    def update_salaries(self, min_value: float):
        scientist_astronauts = [a for a in self.astronauts if
                                self.UPDATE_SALARY_ASTRONAUTS_TYPES in a.specialization.lower()]
        for a in scientist_astronauts:
            if a.salary <= min_value:
                a.salary += self.SALARY_INCREASE

