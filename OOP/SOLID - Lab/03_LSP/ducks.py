from abc import abstractmethod, ABC


class SqueezableToy:
    @abstractmethod
    def make_sound(self):
        pass


class Duck(ABC):
    @staticmethod
    def quack():
        pass

    @staticmethod
    def walk():
        pass

    @staticmethod
    def fly():
        pass


class RubberDuck(SqueezableToy):
    def make_sound(self):
        return "squick"


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0
