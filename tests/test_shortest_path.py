from typing import List
from typing import Tuple

import pytest

from src.shortest_path import Path
from src.shortest_path import ShortestPath
from src.station_reader import Subway


cases_neighbors: List[Tuple[Tuple[str, str, str], List[str]]] = [
    (("tests/cases/case_0.txt", "a", "g"), ["c"]),
    (("tests/cases/case_0.txt", "a", "r"), ["b"]),
    (("tests/cases/case_1.txt", "c", "r"), ["d", "h", "b"]),
    (("tests/cases/case_1.txt", "h", "r"), ["c", "f"]),
    (("tests/cases/case_1.txt", "c", ""), ["g", "d", "b"]),
]


@pytest.mark.parametrize("case, expected", cases_neighbors)
def test_neighbors(case: Tuple[str, str, str], expected: List[str]):
    path, st, color = case
    subway = Subway(path)

    neighbors = []
    for neighbor in subway.neighbor_stations(subway.stations[st], color):
        neighbors.append(neighbor.name)
        assert neighbor.name in expected

    assert len(neighbors) == len(expected)


cases_shortest_path: List[Tuple[Tuple[str, str, str, str], str]] = [
    (("tests/cases/case_0.txt", "a", "a", ""), "a"),
    (("tests/cases/case_0.txt", "a", "c", ""), "a -> c"),
    (("tests/cases/case_0.txt", "a", "c", "g"), "a -> c"),
    (("tests/cases/case_1.txt", "a", "f", "r"), "a -> b -> c -> h -> f"),
    (("tests/cases/case_1.txt", "a", "f", "g"), "a -> b -> c -> d -> e -> f"),
    (("tests/cases/case_1.txt", "a", "f", ""), "a -> b -> c -> d -> e -> f"),
]


@pytest.mark.parametrize("case, expected", cases_shortest_path)
def test_shortest_path(case: Tuple[str, str, str, str], expected: str) -> None:
    path, init_st, final_st, color = case

    shortest_path: Path = ShortestPath(path).find_shortest_path(
        init_st, final_st, color
    )

    assert str(shortest_path) == expected
