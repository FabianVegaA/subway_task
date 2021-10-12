import argparse
import os

from src.shortest_path import ShortestPath


def main():
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

    args = parser.parse_args()

    print(f"{args.filename}")
    if os.path.isfile(args.filename):

        sp = ShortestPath(args.filename).find_shortest_path(
            args.source, args.destination, args.color
        )

        if args.verbosity == 0:
            print(str(sp))

        if args.verbosity == 1:
            print(
                "The shortest path is: \n"
                + str(sp)
                + "\n"
                + f"The total distance is: {len(sp.stations)}"
            )

        if args.verbosity >= 2:
            print(
                "The shortest path is: \n"
                + repr(sp)
                + "\n"
                + f"The total distance is: {len(sp.stations)}"
            )
    raise FileNotFoundError(f"File {args.filename} not found")


if __name__ == "__main__":
    main()
