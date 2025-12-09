from dataclasses import dataclass


@dataclass
class Coordinate2D:
    x: int
    y: int

    @staticmethod
    def create(s: str) -> Coordinate2D:
        [x, y] = [int(i) for i in s.split(",")]
        return Coordinate2D(x, y)

    def __key(self):
        return (self.x, self.y)

    def __hash__(self) -> int:
        return hash(self.__key())
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Coordinate2D):
            if self.x != value.x:
                return False
            if self.y != value.y:
                return False
            return True
