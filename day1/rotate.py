from direction import Direction

def rotate(position: int, size: int, direction: Direction):
    return __calculate(position, size, direction) % 100

def __calculate(position: int, size: int, direction: Direction):
    match direction:
        case Direction.LEFT:
            return (position - size)
        case Direction.RIGHT:
            return (position + size)
