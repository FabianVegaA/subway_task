from typing import Tuple
import pytest

from typing import List

from source.station_reader import Station, Subway


cases: List[Tuple[str, Subway]] = [
    (
        "tests/cases_test/case_0.txt",
        Subway(
            stations={
                "a": Station("a", "white"),
                "b": Station("b", "white"),
                "c": Station("c", "green"),
            },
            routes=[("a", "b"), ("b", "c"), ("c", "a")],
        ),
    )
]


@pytest.mark.parametrize("path, expected", cases)
def test_station_reader(path: str, expected: Station):
    subway = Subway(path)

    for station, expected_station in zip(
        subway.stations.values(), expected.stations.values()
    ):
        assert station.name == expected_station.name
        assert station.type == expected_station.type

    for (sta_1, sta_2), (exp_sta_1, exp_sta_2) in zip(subway.routes, expected.routes):
        assert sta_1 == exp_sta_1 and sta_2 == exp_sta_2


test_station_reader(*cases[0])