from direction import Direction
from rotate import rotate

def test_rotate_right_single():
    result = rotate_right(0, 1)
    assert result == 1

def test_rotate_right_multiple():
    result = rotate_right(0, 5)
    assert result == 5

def test_rotate_right_from_nonzero_position():
    result = rotate_right(50, 7)
    assert result == 57

def test_rotate_right_edge():
    result = rotate_right(99, 1)
    assert result == 0

def test_rotate_right_overflow():
    result = rotate_right(99, 4)
    assert result == 3

def test_rotate_left_single():
    result = rotate_left(7, 1)
    assert result == 6

def test_rotate_left_multiple():
    result = rotate_left(13, 5)
    assert result == 8

def test_rotate_left_from_zero_position():
    result = rotate_left(0, 7)
    assert result == 93

def test_rotate_left_edge():
    result = rotate_left(1, 1)
    assert result == 0

def test_rotate_left_overflow():
    result = rotate_left(2, 4)
    assert result == 98

def rotate_right(position: int, size: int):
    return rotate(position, size, Direction.RIGHT)

def rotate_left(position: int, size: int):
    return rotate(position, size, Direction.LEFT)
