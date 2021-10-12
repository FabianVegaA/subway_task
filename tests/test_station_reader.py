from typing import List, Tuple

import pytest

from src.subway_task.station_reader import Station, Subway

cases: List[Tuple[str, Subway]] = [
    (
        "tests/cases/case_0.txt",
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


@pytest.mark.parametrize("path, expected", cases)
def test_stations(path: str, expected: Station) -> None:
    subway = Subway(path)

    assert len(subway.routes) > 0
    assert len(subway.stations) > 0

    for (st_1, st_2), (est_1, est_2) in zip(subway.routes, expected.routes):
        assert st_1.name == est_1 and st_2.name == est_2


cases_invalid_path: List[Tuple[str, str]] = [
    ("invalid_path.txt", "File not found"),
    ("invalid_path.png", "Invalid file"),
    ("", "Invalid file"),
]


@pytest.mark.parametrize("path, msg_expected", cases_invalid_path)
def test_station_reader_invalid_path(path: str, msg_expected: str) -> None:
    with pytest.raises(FileNotFoundError) as excinfo:
        Subway(path)
        assert msg_expected in str(excinfo.value)
