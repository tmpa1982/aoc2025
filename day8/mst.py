import networkx as nx

from day8.coordinate import Coordinate


def solve2(input: list[str]) -> int:
    coordinates = [Coordinate.create(c) for c in input]
    G = nx.Graph()

    return 0
