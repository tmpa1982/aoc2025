from coordinate_2d import Coordinate2D


def solve(coordinates: list[str]):
    parsed = [Coordinate2D.create(c) for c in coordinates]
    
    c1 = parsed[0]
    c2 = parsed[1]
    max_area = area(c1, c2)
    for i in range(0, len(parsed)-1):
        for j in range(i+1, len(parsed)):
            a = area(parsed[i], parsed[j])
            if a > max_area:
                c1 = parsed[i]
                c2 = parsed[j]
                max_area = a
    return max_area

def area(c1: Coordinate2D, c2: Coordinate2D) -> int:
    return abs(c1.x - c2.x + 1) * abs(c1.y - c2.y + 1)
