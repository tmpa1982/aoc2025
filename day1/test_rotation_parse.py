import pytest

from day1.direction import Direction
from day1.rotation import Rotation

def test_parse_left():
    result = Rotation.parse("L7")
    assert result == Rotation(Direction.LEFT, 7)

def test_parse_right():
    result = Rotation.parse("R5")
    assert result == Rotation(Direction.RIGHT, 5)

def test_invalid_direction():
    with pytest.raises(ValueError, match="Invalid direction: A"):
        Rotation.parse("A1")

def test_invalid_size():
    with pytest.raises(ValueError, match="Invalid size: x"):
        Rotation.parse("Rx")

def test_empty_value():
    with pytest.raises(ValueError, match="Value is empty"):
        Rotation.parse("")

def test_empty_size():
    with pytest.raises(ValueError, match="Invalid size: "):
        Rotation.parse("R")
