from typing import Dict, Iterable, List, Optional

from src.subway_task.station_reader import Station, Subway


class Path:
    def __init__(self, stations: Iterable[Optional[Station]]):
        self.stations = list(filter(lambda st: st is not None, stations))

    def __str__(self):
        return " -> ".join([str(station) for station in self.stations])

    def __repr__(self):

        default: str = "Without Color"

        stations: List[str] = []

        for st in self.stations:
            assert st is not None
            stations.append(f"({st.name}, {st.type or default})")

        return " -> ".join(stations)


class ShortestPath:
    def __init__(self, path: str):
        """
        Parameters
        ----------
        path : str
            Path to the file containing the subway network.
        """
        self.subway = Subway(path)
        self.type_train = ""

    def find_shortest_path(
        self,
        src: str,
        dst: str,
        type_train: str,
    ) -> Path:
        """
        Find the shortest path between two nodes in a graph.

        Parameters
        ----------
        src : str
            Name of the initial station.
        dst : str
            Name of the final station.
        type_train : str
            Type of train.
        Returns
        -------
            Path
        """
        assert self.subway.stations is not None
        assert src in self.subway.stations.keys(), "Source station not found"
        assert dst in self.subway.stations.keys(), "Destination not found"

        if src == dst:
            return Path([self.subway.stations[src]])

        self.type_train = type_train

        dist: Dict[str, float] = {}
        pred: Dict[str, Optional[Station]] = {}

        if not self.bfs(
            self.subway.stations[src], self.subway.stations[dst], pred, dist
        ):
            raise ValueError(f"No path from {src} to {dst}")

        path: List[Optional[Station]] = []
        crawl: Optional[Station] = self.subway.stations[dst]
        path.append(crawl)
        while crawl is not None:
            path.append(pred[crawl.name])
            crawl = pred[crawl.name]

        path.reverse()

        return Path(path)

    def bfs(
        self,
        src: Station,
        dst: Station,
        pred: Dict[str, Optional[Station]],
        dist: Dict[str, float],
    ) -> bool:

        """
        Use the BFS algorithm to find the shortest path between two nodes

        Parameters
        ----------
        src: Station
            Source node.
        dst: Station
            Destination node.
        pred: Dict[str, Optional[Station]]
            Dictionary of predecessors.
        dist: Dict[str, Station]
            Dictionary of distances.
        Returns
        -------
            bool
        """

        assert self.subway.stations is not None

        queue: List[Station] = []
        visited: Dict[str, bool] = {st: False for st in self.subway.stations}

        for st in self.subway.stations.values():
            dist[st.name] = float("inf")
            pred[st.name] = None

        visited[src.name] = True
        dist[src.name] = 0
        queue.append(src)

        while len(queue) > 0:
            curr = queue.pop(0)

            for st in self.subway.neighbor_stations(curr, self.type_train):
                if not visited[st.name]:
                    visited[st.name] = True
                    dist[st.name] = dist[curr.name] + 1
                    pred[st.name] = curr

                    queue.append(st)

                    if st == dst:
                        return True

        return False
