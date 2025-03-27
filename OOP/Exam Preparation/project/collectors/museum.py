from .base_collector import BaseCollector


class Museum(BaseCollector):
    INITIAL_MONEY = 15000
    INITIAL_SPACE = 2000

    def __init__(self, name: str):
        super().__init__(name, available_money=self.INITIAL_MONEY, available_space=self.INITIAL_SPACE)

    def increase_money(self):
        self.available_money += 1000
