from coordinate import Coordinate


def test_distance_int():
    c1 = Coordinate(1, 2, 3)
    c2 = Coordinate(3, 5, 9)

    d = c1.distance(c2)
    assert d == 7

    d = c2.distance(c1)
    assert d == 7

def test_distance_float():
    c1 = Coordinate(1, 2, 3)
    c2 = Coordinate(4, 5, 6)

    d = c1.distance(c2)
    expected = 5.196152
    assert d - expected < 0.0001
