from dataclasses import dataclass


ROLL = "@"
EMPTY = "."

@dataclass
class Coordinate:
    x: int
    y: int

class Board:
    def __init__(self, layout: list[str]):
        self.layout = layout

    def is_accessible(self, coordinate: Coordinate):
        if (self.layout[coordinate.y][coordinate.x] != ROLL):
            return False
        
        num_rolls = 0
        
        width = len(self.layout[0])
        min_x = max(0, coordinate.x - 1)
        min_y = max(0, coordinate.y - 1)
        max_x = min(coordinate.x + 2, len(self.layout))
        max_y = min(coordinate.y + 2, width)
        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                if (x == coordinate.x and y == coordinate.y):
                    continue
                if self.layout[y][x] == ROLL:
                    num_rolls = num_rolls + 1

                if num_rolls > 3:
                    return False

        return True

    def count_accessible(self):
        result = 0
        for y in range(len(self.layout)):
            for x in range(len(self.layout[y])):
                c = Coordinate(x, y)
                if (self.is_accessible(c)):
                    result = result + 1
        return result

    def remove_accessible(self):
        result = []
        for y in range(len(self.layout)):
            line = ""
            for x in range(len(self.layout[y])):
                c = Coordinate(x, y)
                if (self.is_accessible(c)):
                    line = line + EMPTY
                else:
                    line = line + self.layout[y][x]
            result.append(line)
        return result
