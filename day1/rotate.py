from day1.rotation import Rotation
from day1.direction import Direction

def rotate(position: int, rotation: Rotation):
    return __calculate(position, rotation.size, rotation.direction) % 100

def __calculate(position: int, size: int, direction: Direction):
    match direction:
        case Direction.LEFT:
            return (position - size)
        case Direction.RIGHT:
            return (position + size)
