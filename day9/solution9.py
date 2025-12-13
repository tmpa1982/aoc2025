from day9.coordinate_2d import Coordinate2D


def solve(coordinates: list[str]) -> int:
    parsed = [Coordinate2D.create(c) for c in coordinates]
    sorted_areas = sort_areas(parsed)
    return sorted_areas[0][2]

def area(c1: Coordinate2D, c2: Coordinate2D) -> int:
    return (abs(c1.x - c2.x) + 1) * (abs(c1.y - c2.y) + 1)

def solve2(coordinates: list[str]) -> int:
    parsed = [Coordinate2D.create(c) for c in coordinates]
    sorted_areas = sort_areas(parsed)
    for (c1, c2, a) in sorted_areas:
        if not check_line_inside(c1, c2, parsed):
            return a
    return NotImplemented

def sort_areas(parsed: list[Coordinate2D]) -> list[tuple[Coordinate2D, Coordinate2D, int]]:
    areas = calculate_areas(parsed)
    sorted_areas = sorted(areas, key=lambda t: t[2], reverse=True)
    return sorted_areas

def calculate_areas(coordinates: list[Coordinate2D]) -> list[tuple[Coordinate2D, Coordinate2D, int]]:
    areas: list[tuple[Coordinate2D, Coordinate2D, int]] = []
    for i in range(0, len(coordinates)-1):
        for j in range(i+1, len(coordinates)):
            c1 = coordinates[i]
            c2 = coordinates[j]
            a = area(c1, c2)
            areas.append((c1, c2, a))
    return areas

def check_line_inside(c1: Coordinate2D, c2: Coordinate2D, coordinates: list[Coordinate2D]) -> bool:
    min_x = min(c1.x, c2.x)
    max_x = max(c1.x, c2.x)
    min_y = min(c1.y, c2.y)
    max_y = max(c1.y, c2.y)
    
    for i in range(len(coordinates)):
        co1 = coordinates[i]
        co2 = coordinates[(i+1) % len(coordinates)]
        if co1.x == co2.x:
            x = co1.x
            if min_x < x < max_x:
                y1 = min(co1.y, co2.y)
                y2 = max(co1.y, co2.y)
                if min_y < y1 < max_y or min_y < y2 < max_y:
                    return True
                if y1 <= min_y and y2 >= max_y:
                    return True
        elif co1.y == co2.y:
            y = co1.y
            if min_y < y < max_y:
                x1 = min(co1.x, co2.x)
                x2 = max(co1.x, co2.x)
                if min_x < x1 < max_x or min_x < x2 < max_x:
                    return True
                if x1 <= min_x and x2 >= max_x:
                    return True
        else:
            raise ValueError(f"Invalid line: {co1} {co2}")
    return False
