from .zones.base_zone import BaseZone
from .zones.royal_zone import RoyalZone
from .zones.pirate_zone import PirateZone
from .battleships.base_battleship import BaseBattleship
from .battleships.pirate_battleship import PirateBattleship
from .battleships.royal_battleship import RoyalBattleship
from typing import List, Type


class BattleManager:
    VALID_TYPES_ZONES: List[Type[BaseZone]] = [RoyalZone, PirateZone]
    VALID_TYPES_SHIPS: List[Type[BaseBattleship]] = [PirateBattleship, RoyalBattleship]

    def __init__(self):
        self.zones: List[BaseZone] = []
        self.ships: List[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in ["RoyalZone", "PirateZone"]:
            raise Exception("Invalid zone type!")

        if any(z.code == zone_code for z in self.zones):
            raise Exception("Zone already exists!")
        zone_class = next((z for z in self.VALID_TYPES_ZONES if z.__name__ == zone_type), None)
        zone = zone_class(zone_code)
        self.zones.append(zone)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in ["RoyalBattleship", "PirateBattleship"]:
            raise Exception(f"{ship_type} is an invalid type of ship!")
        ship_class = next((s for s in self.VALID_TYPES_SHIPS if s.__name__ == ship_type), None)
        ship = ship_class(name, health, hit_strength)
        self.ships.append(ship)
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if zone.volume == 0:
            return f"Zone {zone.code} does not allow more participants!"
        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"
        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if (isinstance(ship, RoyalBattleship)
                and isinstance(zone, PirateZone)
                or isinstance(ship, PirateBattleship)
                and isinstance(zone, RoyalZone)):
            ship.is_attacking = False
        else:
            ship.is_attacking = True

        ship.is_available = False
        zone.ships.append(ship)
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        ship_obj = next((s for s in self.ships if s.name == ship_name), None)
        if ship_obj is None:
            return f"No ship with this name!"
        if not ship_obj.is_available:
            return "The ship participates in zone battles! Removal is impossible!"
        self.ships.remove(ship_obj)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        attackers = [ship for ship in zone.ships if ship.is_attacking]
        targets = [ship for ship in zone.ships if not ship.is_attacking]
        if len(attackers) < 1 or len(targets) < 1:
            return "Not enough participants. The battle is canceled."
        attacker = max(attackers, key=lambda ship: ship.hit_strength)
        target = max(targets, key=lambda ship: ship.health)
        attacker.attack()
        target.take_damage(attacker)
        if target.health == 0:
            zone.ships.remove(target)
            self.ships.remove(target)
            return f"{target.name} lost the battle and was sunk."
        if attacker.ammunition == 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."
        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = [ship for ship in self.ships if ship.is_available]
        available_ship_names = ", ".join(ship.name for ship in available_ships)
        if available_ship_names:
            available_ship_names = f"#{available_ship_names}#"
        zones_info = "\n".join(zone.zone_info() for zone in sorted(self.zones, key=lambda z: z.code))
        return f"Available Battleships: {len(available_ships)}\n{available_ship_names}\n***Zones Statistics:***\nTotal Zones: {len(self.zones)}\n{zones_info}"