from project.astronauts.base_astronaut import BaseAstronaut


class ScientistAstronaut(BaseAstronaut):
    SPECIALIZATION = "ScientistAstronaut"
    STAMINA = 70
    MAX_STAMINA = 100
    STAMINA_INCREASE_PER_CALL = 3

    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, specialization=self.SPECIALIZATION, stamina=self.STAMINA)

    def train(self):
        self.stamina = min(self.MAX_STAMINA, self.stamina + self.STAMINA_INCREASE_PER_CALL)
