from day1.direction import Direction
from day1.rotate import rotate
from day1.rotation import Rotation

def rotate_series_with_detail(steps: list[str]):
    position = 50
    result = [(None, position)]
    for step in steps:
        rotation = Rotation.parse(step)
        position = rotate(position, rotation)
        result.append((rotation, position))
    return result

def rotate_series(steps: list[str]):
    result = rotate_series_with_detail(steps)
    return [i[1] for i in result]

def count_zeros(series: list[int]):
    return sum(1 for item in series if item == 0)

def solve(steps: list[str]):
    positions = rotate_series(steps)
    return count_zeros(positions)

def solve2(steps: list[str]):
    positions = rotate_series_with_detail(steps)
    result = 0
    for i in range(0, len(positions) - 1):
        this_pos = positions[i]
        next_pos = positions[i+1]
        rotation = next_pos[0]
        sub = count_zeros_2(this_pos[1], next_pos[1], rotation)
        result = result + sub
    return result

def count_zeros_2(position: int, next_pos: int, rotation: Rotation):
    result = rotation.size // 100
    if rotation.size % 100 == 0:
        return result
    if next_pos == 0:
        return result + 1
    if position == 0:
        return result
    match rotation.direction:
        case Direction.LEFT:
            if next_pos > position:
                return result + 1
        case Direction.RIGHT:
            if next_pos < position:
                return result + 1
    return result
