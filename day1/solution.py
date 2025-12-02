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
