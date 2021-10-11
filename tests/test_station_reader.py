from typing import List
from typing import Tuple

import pytest

from src.station_reader import Station
from src.station_reader import Subway


cases: List[Tuple[str, Subway]] = [
    (
        "tests/cases_test/case_0.txt",
        Subway(
            stations={
                "a": Station("a", ""),
                "b": Station("b", "r"),
                "c": Station("c", "g"),
            },
            routes=[("a", "b"), ("b", "c"), ("c", "a")],
        ),
    )
]


@pytest.mark.parametrize("path, expected", cases)
def test_station_reader(path: str, expected: Station) -> None:
    subway = Subway(path)

    assert len(subway.routes) > 0
    assert len(subway.stations) > 0

    for station, expected_station in zip(
        subway.stations.values(), expected.stations.values()
    ):
        assert station.name == expected_station.name
        assert station.type == expected_station.type

    for (st_1, st_2), (est_1, est_2) in zip(subway.routes, expected.routes):
        assert st_1.name == est_1 and st_2.name == est_2
