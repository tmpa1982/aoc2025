from typing import Iterator
import networkx as nx

from networkx import Graph

from day8.coordinate import Coordinate
from day8.distance import calculate_distances


def solve2(input: list[str]) -> int:
    coordinates = [Coordinate.create(c) for c in input]
    distances = calculate_distances(coordinates)
    G: Graph[Coordinate] = Graph()
    G.add_edges_from([
        ((c1, c2, {"weight": d})) for ((c1, c2), d) in distances.items()
    ])
    spanning_edges: Iterator[tuple[Coordinate, Coordinate, float]] = nx.minimum_spanning_edges(G)
    max_edge = None
    for edge in spanning_edges:
        if not max_edge or edge[2]["weight"] > max_edge[2]["weight"]:
            max_edge = edge
    if not max_edge:
        raise ValueError("No edges found")

    c1 = max_edge[0]
    c2 = max_edge[1]
    return c1.x * c2.x
