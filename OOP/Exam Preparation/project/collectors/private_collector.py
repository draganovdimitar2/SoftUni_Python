from .base_collector import BaseCollector


class PrivateCollector(BaseCollector):
    INITIAL_MONEY = 25000
    INITIAL_SPACE = 3000

    def __init__(self, name: str):
        super().__init__(name, available_money=self.INITIAL_MONEY, available_space=self.INITIAL_SPACE)

    def increase_money(self):
        self.available_money += 5000
