from project.zones.base_zone import BaseZone
from project.battleships.royal_battleship import RoyalBattleship


class PirateZone(BaseZone):
    def __init__(self, code: str):
        super().__init__(code, 8)

    def zone_info(self):
        ships = self.get_ships()
        royal_ships = [ship for ship in ships if isinstance(ship, RoyalBattleship)]
        ship_names = ", ".join(ship.name for ship in ships)
        if ship_names:
            ship_names = f"#{ship_names}#"
        info = [
            "@Pirate Zone Statistics@",
            f"Code: {self.code}; Volume: {self.volume}",
            f"Battleships currently in the Pirate Zone: {len(ships)}, {len(royal_ships)} out of them are Royal Battleships.",
            ship_names if ship_names else ""
        ]
        return "\n".join(info)