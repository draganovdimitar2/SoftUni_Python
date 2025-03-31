class BaseZone:
    def __init__(self, code: str, volume: int):
        if not code.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self.code = code
        self.volume = volume
        self.ships = []

    def get_ships(self):
        return sorted(self.ships, key=lambda ship: (-ship.hit_strength, ship.name))

    def zone_info(self):
        raise NotImplementedError("This method should be implemented by subclasses")