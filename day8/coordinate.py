import math

from dataclasses import dataclass


@dataclass
class Coordinate:
    x: int
    y: int
    z: int

    @staticmethod
    def create(s: str) -> Coordinate:
        [x, y, z] = [int(i) for i in s.split(",")]
        return Coordinate(x, y, z)

    def distance(self, other: Coordinate) -> float:
        xx = (self.x - other.x) ** 2
        yy = (self.y - other.y) ** 2
        zz = (self.z - other.z) ** 2
        
        return math.sqrt(xx + yy + zz)

    def __key(self):
        return (self.x, self.y, self.z)

    def __hash__(self) -> int:
        return hash(self.__key())
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Coordinate):
            if self.x != value.x:
                return False
            if self.y != value.y:
                return False
            if self.z != value.z:
                return False
            return True
