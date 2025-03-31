class BaseBattleship:
    def __init__(self, name: str, health: int, hit_strength: int, ammunition: int):
        if not name.isalpha():
            raise ValueError("Ship name must contain only letters!")
        self.name = name
        self.health = health
        self.hit_strength = hit_strength
        self.ammunition = ammunition
        self.is_attacking = False
        self.is_available = True

    def take_damage(self, enemy_battleship: 'BaseBattleship'):
        self.health -= enemy_battleship.hit_strength
        if self.health < 0:
            self.health = 0

    def attack(self):
        raise NotImplementedError("This method should be implemented by subclasses")