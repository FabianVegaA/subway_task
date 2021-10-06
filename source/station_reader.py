from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from pprint import pprint
import re


@dataclass
class Station:
    """
    Station class
    """

    name: str
    type: str


class Subway:
    """
    Subway class
    """

    def __init__(
        self,
        path: str = "",
        stations: Optional[Dict[str, Station]] = None,
        routes: Optional[List[Tuple[Station, Station]]] = None,
    ) -> None:
        self._path = path
        self.stations = stations
        self.routes = routes

        self._type_station: Optional[List[str]] = []

        if self.stations is None or self.routes is None:
            self._read_stations()

    def _read_stations(self) -> None:
        """
        Read stations from file
        """

        with open(self._path, "r") as file:
            while (line := file.readline()) != "":

                if re.match(r"^#STATIONS", line):
                    self._parse_stations(file, line)
                elif re.match(r"^#ROUTES", line):
                    self._parse_routes(file, line)

    def _parse_stations(self, file, current_line):
        """
        Parse stations from file
        """
        assert current_line == "#STATIONS\n"

        self.stations = {}
        self._type_station = []

        while re.match(r"^#END STATIONS", line := file.readline()):
            name, type_ = line.split()
            if not type_ in self._type_station:
                self._type_station.append(type_)
            self.stations[name] = Station(name, type_)

    def _parse_routes(self, file, current_line):
        """ "
        Parse routes from file
        """
        assert current_line == "#ROUTES\n"

        self.routes = []

        while re.match(r"^#END ROUTES", line := file.readline()):
            station_1, station_2 = line.split()
            self.routes.append(self.station[station_1], self.station[station_2])

    def __str__(self):
        return str(self.routes)
