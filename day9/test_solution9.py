from day9.coordinate_2d import Coordinate2D
from day9.solution9 import check_line_inside, solve, solve2


def test_solve_sample():
    with open("day9/input_sample.txt", 'r') as file:
        input = file.readlines()
        
        result = solve(input)
        
        assert result == 50

def test_solve2_sample():
    with open("day9/input_sample.txt", 'r') as file:
        input = file.readlines()
        
        result = solve2(input)
        
        assert result == 24

def test_line_inside_left_outside_in():
    c1 = Coordinate2D(1, 1)
    c2 = Coordinate2D(4, 4)
    coordinates = [
        Coordinate2D(0, 2),
        Coordinate2D(2, 2),
    ]
    exec_test_line_inside(c1, c2, coordinates)

def test_line_inside_right_outside_in():
    c1 = Coordinate2D(1, 1)
    c2 = Coordinate2D(4, 4)
    coordinates = [
        Coordinate2D(5, 2),
        Coordinate2D(2, 2),
    ]
    exec_test_line_inside(c1, c2, coordinates)

def test_line_inside_top_outside_in():
    c1 = Coordinate2D(1, 1)
    c2 = Coordinate2D(4, 4)
    coordinates = [
        Coordinate2D(2, 0),
        Coordinate2D(2, 2),
    ]
    exec_test_line_inside(c1, c2, coordinates)

def test_line_inside_bottom_outside_in():
    c1 = Coordinate2D(1, 1)
    c2 = Coordinate2D(4, 4)
    coordinates = [
        Coordinate2D(2, 5),
        Coordinate2D(2, 2),
    ]
    exec_test_line_inside(c1, c2, coordinates)

def test_line_inside_horizontal():
    c1 = Coordinate2D(1, 1)
    c2 = Coordinate2D(4, 4)
    coordinates = [
        Coordinate2D(2, 2),
        Coordinate2D(3, 2),
    ]
    exec_test_line_inside(c1, c2, coordinates)

def test_line_inside_vertical():
    c1 = Coordinate2D(1, 1)
    c2 = Coordinate2D(4, 4)
    coordinates = [
        Coordinate2D(2, 2),
        Coordinate2D(2, 3),
    ]
    exec_test_line_inside(c1, c2, coordinates)

def test_line_crossing_horizontal():
    c1 = Coordinate2D(1, 1)
    c2 = Coordinate2D(4, 4)
    coordinates = [
        Coordinate2D(0, 2),
        Coordinate2D(5, 2),
    ]
    exec_test_line_inside(c1, c2, coordinates)

def test_line_crossing_vertical():
    c1 = Coordinate2D(1, 1)
    c2 = Coordinate2D(4, 4)
    coordinates = [
        Coordinate2D(2, 0),
        Coordinate2D(2, 5),
    ]
    exec_test_line_inside(c1, c2, coordinates)

def exec_test_line_inside(c1: Coordinate2D, c2: Coordinate2D, coordinates: list[Coordinate2D]):
    assert check_line_inside(c1, c2, coordinates)
    assert check_line_inside(c2, c1, coordinates)
    coordinates.reverse()
    assert check_line_inside(c1, c2, coordinates)
    assert check_line_inside(c2, c1, coordinates)

def test_line_touching_top():
    c1 = Coordinate2D(1, 1)
    c2 = Coordinate2D(4, 4)
    coordinates = [
        Coordinate2D(1, 1),
        Coordinate2D(4, 1),
    ]
    exec_test_line_not_inside(c1, c2, coordinates)

def test_line_touching_bottom():
    c1 = Coordinate2D(1, 1)
    c2 = Coordinate2D(4, 4)
    coordinates = [
        Coordinate2D(1, 4),
        Coordinate2D(4, 4),
    ]
    exec_test_line_not_inside(c1, c2, coordinates)

def test_line_touching_left():
    c1 = Coordinate2D(1, 1)
    c2 = Coordinate2D(4, 4)
    coordinates = [
        Coordinate2D(1, 1),
        Coordinate2D(1, 4),
    ]
    exec_test_line_not_inside(c1, c2, coordinates)

def test_line_touching_right():
    c1 = Coordinate2D(1, 1)
    c2 = Coordinate2D(4, 4)
    coordinates = [
        Coordinate2D(4, 1),
        Coordinate2D(4, 4),
    ]
    exec_test_line_not_inside(c1, c2, coordinates)

def exec_test_line_not_inside(c1: Coordinate2D, c2: Coordinate2D, coordinates: list[Coordinate2D]):
    assert not check_line_inside(c1, c2, coordinates)
    assert not check_line_inside(c2, c1, coordinates)
    coordinates.reverse()
    assert not check_line_inside(c1, c2, coordinates)
    assert not check_line_inside(c2, c1, coordinates)
