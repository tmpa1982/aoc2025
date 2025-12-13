from day8.coordinate import Coordinate


def calculate_distances(coordinates: list[Coordinate]) -> dict[tuple[Coordinate, Coordinate], float]:
    distances: dict[tuple[Coordinate, Coordinate], float] = {}
    for i in range(0, len(coordinates)-1):
        for j in range(i+1, len(coordinates)):
            c1 = coordinates[i]
            c2 = coordinates[j]
            d = c1.distance(c2)
            distances[(c1, c2)] = d
    return distances
