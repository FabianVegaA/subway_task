import argparse
import os
import sys

from src.subway_task.shortest_path import ShortestPath


def main(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=str, help="Source station")
    parser.add_argument("destination", type=str, help="Destination station")
    parser.add_argument(
        "filename", type=str, help="Path file with the routes and stations"
    )
    parser.add_argument(
        "-c",
        "--color",
        type=str,
        help='Color of train, por default "" (without color)',
        default="",
    )
    parser.add_argument("-v", "--verbosity", action="count", default=0)

    args_ = parser.parse_args(*args)

    if os.path.isfile(args_.filename):

        sp = ShortestPath(args_.filename).find_shortest_path(
            args_.source, args_.destination, args_.color
        )

        if args_.verbosity == 0:
            print(str(sp))

        if args_.verbosity == 1:
            print(
                "The shortest path is: \n"
                + str(sp)
                + "\n"
                + f"The total distance is: {len(sp.stations)}"
            )

        if args_.verbosity >= 2:
            print(
                "The shortest path is: \n"
                + repr(sp)
                + "\n"
                + f"The total distance is: {len(sp.stations)}"
            )
    raise FileNotFoundError(f"File {args_.filename} not found")


if __name__ == "__main__":
    main(sys.argv[1:])
