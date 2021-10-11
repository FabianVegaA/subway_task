import re
from dataclasses import dataclass
from typing import Dict
from typing import Generator
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple


@dataclass
class Station:
    """
    Station class
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
        self._path = path
        self.stations = stations
        self.routes = routes

        self._type_station: Optional[List[str]] = []

        if self.stations is None or self.routes is None:
            self._read_stations()

    def num_station(self):
        return len(self.stations)

    def _read_stations(self) -> None:
        """
        Read stations from file
        """

        with open(self._path) as file:
            while (line := file.readline()) != "":

                if re.match(r"^#\s*STATIONS", line):
                    self._parse_stations(file, line)
                elif re.match(r"^#\s*ROUTES", line):
                    self._parse_routes(file, line)

    def _parse_stations(self, file, current_line: str) -> None:
        """
        Parse stations from file
        """
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
        """ "
        Parse routes from file
        """
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

    def neighbor_stations(
        self, curr_st: Station, type_train: str
    ) -> Generator[Station, None, None]:
        """
        It returns the neighbors of a station

        Parameters
        ----------
        curr_st : Station
            Current stationtation
        type_train : str
            Type of train

        Returns
        -------
        List[Station]
            List of neighbors

        """
        assert self.routes is not None

        queuqe: List[Station] = [curr_st]
        visited: Set[str] = {curr_st.name}

        while len(queuqe) > 0:
            st: Station = queuqe.pop(0)

            for s1, s2 in self.routes:
                if st in [s1, s2]:
                    adj: Station = s1 if s1 != st else s2
                    if adj.name not in visited:
                        if (
                            type_train != ""
                            and adj.type != ""
                            and adj.type != type_train
                        ):
                            queuqe.append(adj)
                        else:
                            visited.add(adj.name)
                            yield adj
