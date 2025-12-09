from circuit import Circuit, solve
from coordinate import Coordinate

def test_find_shortest_edge_trivial():
    c1 = Coordinate(0, 0, 0)
    c2 = Coordinate(1, 1, 1)
    exec_find_shortest_edge(c1, c2)

def test_find_shortest_edge_extra():
    c1 = Coordinate(0, 0, 0)
    c2 = Coordinate(1, 1, 1)
    exec_find_shortest_edge(c1, c2, Coordinate(100, 100, 100))

def test_find_shortest_edge_extra_after_one_iteration():
    c1 = Coordinate(0, 0, 0)
    c2 = Coordinate(1, 1, 1)
    c3 = Coordinate(100, 100, 100)
    c4 = Coordinate(110, 110, 110)
    coordinates = [c1, c2, c3, c4]
    circuit = Circuit(coordinates)
    
    circuit.mark_edge(2)
    
    assert circuit.get_circuit_id(c1) == 1
    assert circuit.get_circuit_id(c2) == 1
    assert circuit.get_circuit_id(c3) == 2
    assert circuit.get_circuit_id(c4) == 2

def test_find_shortest_edge_connecting():
    c1 = Coordinate(0, 0, 0)
    c2 = Coordinate(0, 0, 1)
    c3 = Coordinate(1, 1, 1)
    coordinates = [c1, c2, c3]
    circuit = Circuit(coordinates)

    circuit.mark_edge(2)
    
    assert circuit.get_circuit_id(c1) == 1
    assert circuit.get_circuit_id(c2) == 1
    assert circuit.get_circuit_id(c3) == 1

def exec_find_shortest_edge(c1: Coordinate, c2: Coordinate, *args: Coordinate):
    coordinates = list(args) + [c1, c2]
    circuit = Circuit(coordinates)
    
    circuit.mark_edge(1)
    
    assert circuit.get_circuit_id(c1) == 1
    assert circuit.get_circuit_id(c2) == 1

def test_solve_sample():
    with open("day8/input_sample.txt", 'r') as file:
        input = file.readlines()
        
        result = solve(input, 10)
        
        assert result == 40

def test_162_425_distance():
    c1 = Coordinate.create("162,817,812")
    c2 = Coordinate.create("425,690,689")
    
    distance = c1.distance(c2)
    
    assert distance - 316.9 < 0.1

def test_941_425_distance():
    c1 = Coordinate.create("162,817,812")
    c2 = Coordinate.create("941,993,340")
    
    distance = c1.distance(c2)
    
    assert distance - 927.686 < 0.1
