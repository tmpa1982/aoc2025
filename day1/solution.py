from rotate import rotate
from rotation import Rotation

def rotate_series(steps: list[str]):
    position = 50
    result = [position]
    for step in steps:
        rotation = Rotation.parse(step)
        position = rotate(position, rotation)
        result.append(position)
    return result

def count_zeros(series: list[int]):
    return sum(1 for item in series if item == 0)
