from typing import Callable
from coordinate_2d import Coordinate2D
from board import Board


def solve(coordinates: list[str]):
    parsed = [Coordinate2D.create(c) for c in coordinates]
    return solve_condition(parsed)

def solve_condition(coordinates: list[Coordinate2D], condition: Callable[[Coordinate2D, Coordinate2D], bool] = lambda x, y: True):
    c1 = coordinates[0]
    c2 = coordinates[1]
    max_area = area(c1, c2)
    for i in range(0, len(coordinates)-1):
        for j in range(i+1, len(coordinates)):
            a = area(coordinates[i], coordinates[j])
            if a > max_area and condition(coordinates[i], coordinates[j]):
                c1 = coordinates[i]
                c2 = coordinates[j]
                max_area = a
    return max_area

def area(c1: Coordinate2D, c2: Coordinate2D) -> int:
    return abs(c1.x - c2.x + 1) * abs(c1.y - c2.y + 1)

def solve2(coordinates: list[str]):
    parsed = [Coordinate2D.create(c) for c in coordinates]
    (max_x, max_y) = get_maximums(parsed)
    board = Board(max_x, max_y)
    for i in range(0, len(parsed)):
        c1 = parsed[i]
        c2 = parsed[(i+1) % len(parsed)]
        board.mark_line(c1, c2)
    board.fill_closed_area()
    
    return solve_condition(parsed, lambda x, y: is_within_enclosed_area(board, x, y))

def is_within_enclosed_area(board: Board, c1: Coordinate2D, c2: Coordinate2D) -> bool:
    min_x = min(c1.x, c2.x)
    max_x = max(c1.x, c2.x)
    min_y = min(c1.y, c2.y)
    max_y = max(c1.y, c2.y)
    
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if not board.is_marked(x, y):
                return False
    return True

def get_maximums(coordinates: list[Coordinate2D]) -> tuple[int, int]:
        max_x = coordinates[0].x
        max_y = coordinates[0].y
        for c in coordinates[1:]:
            if c.x > max_x:
                max_x = c.x
            if c.y > max_y:
                max_y = c.y
        return (max_x, max_y)
