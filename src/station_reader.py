import re
from dataclasses import dataclass
from typing import Dict, Generator, List, Optional, Set, Tuple


@dataclass
class Station:
    """
    Station class

    Attributes:
        name (str): name of the station
        type (str): type of the station
    """

    name: str
    type: str

    def __str__(self):
        return self.name


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
        """
        This is the constructor of the class Subway

        If no path is given

        Parameters
        ----------
        path : str
            Path of the file
        stations : Dict[str, Station]
            Dictionary of stations
        routes : List[Tuple[Station, Station]]
            List of routes
        """

        self._path = path
        self.stations = stations
        self.routes = routes

        self._type_station: Optional[List[str]] = []

        if self.stations is None or self.routes is None:
            self._read_stations()

    def num_station(self):
        return len(self.stations)

    def _read_stations(self) -> None:

        if not re.match(r"^.+\.txt$", self._path):
            raise FileNotFoundError("Invalid file")

        with open(self._path) as file:
            while line := file.readline():

                if re.match(r"^#\s*STATIONS", line):
                    self._parse_stations(file, line)
                elif re.match(r"^#\s*ROUTES", line):
                    self._parse_routes(file, line)

    def _parse_stations(self, file, current_line: str) -> None:

        assert re.match(r"^#\s*STATIONS", current_line)

        self.stations = {}
        self._type_station = []

        while current_line := file.readline():
            if re.match(r"^#\s*END STATIONS", current_line):
                break

            name, type_ = (
                current_line.split()
                if len(current_line.split()) == 2
                else (current_line.split()[0], "")
            )
            if type_ not in self._type_station:
                self._type_station.append(type_)
            self.stations[name] = Station(name, type_)

    def _parse_routes(self, file, current_line: str):

        assert self.stations is not None
        assert re.match(r"^#\s*ROUTES", current_line)

        self.routes = []

        while current_line := file.readline():
            if re.match(r"^#\s*END ROUTES", current_line):
                break
            station_1, station_2 = current_line.split()

            route: Tuple[Station, Station] = (
                self.stations[station_1],
                self.stations[station_2],
            )
            self.routes.append(route)

    def _get_neighbors(self, st):
        for s1, s2 in self.routes:
            if st in [s1, s2]:
                yield s1 if s1 != st else s2

    def neighbor_stations(
        self, curr_st: Station, type_train: str
    ) -> Generator[Station, None, None]:
        """
        It returns the neighbors of a station filteing the stations by type.

        Parameters
        ----------
        curr_st : Station
            Current station
        type_train : str
            Type of train

        Returns
        -------
        List[Station]
            List of neighbors
        """
        assert self.routes is not None

        queue: List[Station] = [curr_st]
        visited: Set[str] = {curr_st.name}

        while len(queue) > 0:
            st: Station = queue.pop(0)

            for neighbor in self._get_neighbors(st):
                if neighbor.name not in visited:
                    if (
                        type_train != ""
                        and neighbor.type != ""
                        and neighbor.type != type_train
                    ):
                        queue.append(neighbor)
                    else:
                        visited.add(neighbor.name)
                        yield neighbor
