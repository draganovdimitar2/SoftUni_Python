from project.astronauts.base_astronaut import BaseAstronaut
from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation
from project.stations.research_station import ResearchStation
from project.stations.maintenance_station import MaintenanceStation
from typing import Type, List


class SpaceAgency:
    VALID_ASTRONAUT_TYPES: List[Type[BaseAstronaut]] = [EngineerAstronaut, ScientistAstronaut]
    VALID_STATION_TYPES: List[Type[BaseStation]] = [ResearchStation, MaintenanceStation]

    def __init__(self):
        self.astronauts: List[Type[BaseAstronaut]] = []
        self.stations: List[Type[BaseStation]] = []

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        astronaut_class = next((a for a in self.VALID_ASTRONAUT_TYPES if a.__name__ == astronaut_type), None)

        if astronaut_class is None:
            raise ValueError("Invalid astronaut type!")
        if any(a.id_number == astronaut_id_number for a in self.astronauts):
            raise ValueError(f"{astronaut_id_number} has been already added!")
        astronaut_obj = astronaut_class(astronaut_id_number, astronaut_salary)
        self.astronauts.append(astronaut_obj)
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    def add_station(self, station_type: str, station_name: str):
        station_class = next((s for s in self.VALID_STATION_TYPES if s.__name__ == station_type), None)

        if station_class is None:
            raise ValueError("Invalid station type!")
        if any(s.name == station_name for s in self.stations):
            raise ValueError(f"{station_name} has been already added!")
        station_obj = station_class(station_name)
        self.stations.append(station_obj)
        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self, station_name: str, astronaut_type: str):
        station_obj = next((s for s in self.stations if s.name == station_name), None)
        if station_obj is None:
            raise ValueError(f"Station {station_name} does not exist!")

        astronaut_obj = next((a for a in self.astronauts if a.SPECIALIZATION == astronaut_type), None)
        if astronaut_obj is None:
            raise ValueError("No available astronauts of the type!")

        if station_obj.capacity < 1:
            return "This station has no available capacity."
        self.astronauts.remove(astronaut_obj)
        station_obj.astronauts.append(astronaut_obj)
        station_obj.capacity -= 1

        return f"{astronaut_obj.id_number} was assigned to {station_name}."

    def train_astronauts(self, station: BaseStation, sessions_number: int):  # TODO
        station_obj = next((s for s in self.stations if s == station), None)

        for session in range(sessions_number):
            for astronaut in station_obj.astronauts:
                astronaut.train()

        total_stamina = sum([a.stamina for a in station_obj.astronauts])

        return f"{station.name} astronauts have {total_stamina} total stamina after {sessions_number} training session/s."

    def retire_astronaut(self, station: BaseStation, astronaut_id_number: str):  # TODO
        station_obj = next((s for s in self.stations if s == station), None)
        astronaut_obj = next((a for a in station_obj.astronauts if a.id_number == astronaut_id_number), None)

        if astronaut_obj is None or astronaut_obj.stamina == 100:
            return "The retirement process was canceled."
        station_obj.astronauts.remove(astronaut_obj)
        station_obj.capacity += 1

        return f"Retired astronaut {astronaut_id_number}."

    def agency_update(self, min_value: float):
        for station in self.stations:
            station.update_salaries(min_value)

        sorted_stations = sorted(self.stations, key=lambda s: (-len(s.astronauts), s.name))
        total_available_astronauts = len(self.astronauts)
        total_available_capacity = sum(station.capacity for station in self.stations)
        stations_info = "\n".join(station.status() for station in sorted_stations)

        return (f"*Space Agency Up-to-Date Report*\n"
                f"Total number of available astronauts: {total_available_astronauts}\n"
                f"**Stations count: {len(self.stations)}; Total available capacity: {total_available_capacity}**\n"
                f"{stations_info}")
