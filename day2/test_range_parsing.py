import pytest

from range import Range
from range_parsing import parse, split, take_half, trim_bottom, trim_top

def test_split_range():
    result = split("11-22,95-115,998-1012")
    assert result == ["11-22", "95-115", "998-1012"]

def test_split_empty_range():
    result = split("")
    assert result == []

def test_split_none():
    result = split(None)
    assert result == []

def test_parse():
    result = parse("11-22")
    assert result == Range.create("11", "22")

def test_parse_invalid():
    with pytest.raises(ValueError):
        parse("1122")

def test_parse_non_numeric_first():
    with pytest.raises(ValueError):
        parse("x-1")

def test_parse_non_numeric_second():
    with pytest.raises(ValueError):
        parse("1-x")

def test_trim_bottom_small():
    result = trim_bottom(7)
    assert result == 11

def test_trim_bottom_11():
    result = trim_bottom(11)
    assert result == 11

def test_trim_bottom_12():
    result = trim_bottom(12)
    assert result == 22

def test_trim_bottom_21():
    result = trim_bottom(21)
    assert result == 22

def test_trim_bottom_22():
    result = trim_bottom(22)
    assert result == 22

def test_trim_bottom_100():
    result = trim_bottom(100)
    assert result == 1010

def test_trim_bottom_3534():
    result = trim_bottom(3534)
    assert result == 3535

def test_trim_bottom_3536():
    result = trim_bottom(3536)
    assert result == 3636

def test_trim_top_odd():
    result = trim_top(365)
    assert result == 99

def test_trim_top_odd_long():
    result = trim_top(36591)
    assert result == 9999

def test_trim_top_4567():
    result = trim_top(4567)
    assert result == 4545

def test_trim_top_7654():
    result = trim_top(7654)
    assert result == 7575

def test_trim_top_7676():
    result = trim_top(7676)
    assert result == 7676

def test_trim_top_83():
    result = trim_top(83)
    assert result == 77

def test_trim_top_small():
    result = trim_top(10)
    assert result == 0

def test_take_half():
    result = take_half(123123)
    assert result == 123
