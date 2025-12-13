from day8.coordinate import Coordinate


class CircuitElement:
    coordinate: Coordinate
    circuit_id: int | None
    
    def __init__(self, coordinate: Coordinate):
        self.coordinate = coordinate
        self.circuit_id = None

    def set_circuit(self, id: int):
        self.circuit_id = id

    def __repr__(self) -> str:
        return f"{self.coordinate} {self.circuit_id}"
    