from dataclasses import dataclass

from direction import Direction

@dataclass
class Rotation:
    direction: Direction
    size: int

    @staticmethod
    def parse(s: str):
        if not s:
            raise ValueError("Value is empty")
        direction = Rotation.__parse_direction(s[0])
        size = Rotation.__parse_size(s[1:])
        return Rotation(direction, size)

    @staticmethod
    def __parse_direction(s: str):
        match s:            
            case "L":
                return Direction.LEFT
            case "R":
                return Direction.RIGHT
            case _:
                raise ValueError(f"Invalid direction: {s}")
    
    @staticmethod
    def __parse_size(s: str):
        try:
            return int(s)
        except (ValueError):
            raise ValueError(f"Invalid size: {s}")
