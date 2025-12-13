from day8.circuit_element import CircuitElement
from day8.coordinate import Coordinate
from day8.distance import calculate_distances


class Circuit:
    distances: dict[tuple[Coordinate, Coordinate], float]
    coordinate_map: dict[Coordinate, CircuitElement]
    
    def __init__(self, coordinates: list[Coordinate]):
        if len(coordinates) < 2:
            raise ValueError("There must be at least two coordinates")

        self.distances = {}
        self.coordinate_map = {}
        for c in coordinates:
            self.coordinate_map[c] = CircuitElement(c)
        self.sort_by_distance()

    def sort_by_distance(self):
        coordinates = list(self.coordinate_map.keys())
        self.distances = calculate_distances(coordinates)
        self.sorted_distances = sorted(self.distances.items(), key=lambda x: x[1])

    def get_circuit_id(self, coordinate: Coordinate) -> int | None:
        return self.coordinate_map[coordinate].circuit_id

    def mark_edge(self, num_iteration: int = 10):
        max_iteration = min(len(self.sorted_distances), num_iteration)
        cnt = 0
        for ((c1, c2), _) in self.sorted_distances:
            if cnt == max_iteration:
                break
            e1 = self.coordinate_map[c1]
            e2 = self.coordinate_map[c2]
            if e1.circuit_id and e2.circuit_id:
                self.update_all_circuit_id(e1.circuit_id, e2.circuit_id)
            elif not e1.circuit_id and not e2.circuit_id:
                iteration_id = self.next_circuit_id()
                e1.set_circuit(iteration_id)
                e2.set_circuit(iteration_id)
            elif e1.circuit_id:
                e2.set_circuit(e1.circuit_id)
            elif e2.circuit_id:
                e1.set_circuit(e2.circuit_id)
            cnt = cnt + 1

    def update_all_circuit_id(self, old_id: int, new_id: int):
        for e in self.coordinate_map.values():
            if e.circuit_id == old_id:
                e.set_circuit(new_id)

    def next_circuit_id(self) -> int:
        result = 0
        for e in self.coordinate_map.values():
            if e.circuit_id and e.circuit_id > result:
                result = e.circuit_id
        return result + 1
    
    def count_circuit_sizes(self) -> list[int]:
        counter: dict[int, int] = {}
        for e in self.coordinate_map.values():
            if e.circuit_id:
                current = counter[e.circuit_id] if e.circuit_id in counter else 0
                counter[e.circuit_id] = current + 1
        return list(counter.values())
    
    def solve(self, num_iteration: int) -> int:
        self.mark_edge(num_iteration)
        counter = self.count_circuit_sizes()
        counter.sort(reverse=True)
        result = 1
        for n in counter[:3]:
            if n > 0:
                result = result * n
        return result

def solve(coordinates: list[str], num_iteration: int) -> int:
    parsed = [Coordinate.create(c) for c in coordinates]
    circuit = Circuit(parsed)
    return circuit.solve(num_iteration)
