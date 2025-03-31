from project.zones.base_zone import BaseZone
from project.battleships.royal_battleship import RoyalBattleship
from project.battleships.pirate_battleship import PirateBattleship


class RoyalZone(BaseZone):
    def __init__(self, code: str):
        super().__init__(code, 10)

    def zone_info(self):
        ships = self.get_ships()
        pirate_ships = [ship for ship in ships if isinstance(ship, PirateBattleship)]
        ship_names = ", ".join(ship.name for ship in ships)
        if ship_names:
            ship_names = f"#{ship_names}#"
        info = [
            "@Royal Zone Statistics@",
            f"Code: {self.code}; Volume: {self.volume}",
            f"Battleships currently in the Royal Zone: {len(ships)}, {len(pirate_ships)} out of them are Pirate Battleships.",
            ship_names if ship_names else ""
        ]
        return "\n".join(info)