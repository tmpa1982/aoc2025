import pytest

from range import Range
from range_parsing import count_invalid, parse, solve, split, take_repeating_pattern, trim_bottom, trim_top

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
    result = trim_bottom_2(7)
    assert result == 11

def test_trim_bottom_11():
    result = trim_bottom_2(11)
    assert result == 11

def test_trim_bottom_12():
    result = trim_bottom_2(12)
    assert result == 22

def test_trim_bottom_21():
    result = trim_bottom_2(21)
    assert result == 22

def test_trim_bottom_22():
    result = trim_bottom_2(22)
    assert result == 22

def test_trim_bottom_100():
    result = trim_bottom_2(100)
    assert result == 1010

def test_trim_bottom_3534():
    result = trim_bottom_2(3534)
    assert result == 3535

def test_trim_bottom_3536():
    result = trim_bottom_2(3536)
    assert result == 3636

def trim_bottom_2(n: int):
    return trim_bottom(n, 2)

def test_trim_top_odd():
    result = trim_top_2(365)
    assert result == 99

def test_trim_top_odd_long():
    result = trim_top_2(36591)
    assert result == 9999

def test_trim_top_4567():
    result = trim_top_2(4567)
    assert result == 4545

def test_trim_top_7654():
    result = trim_top_2(7654)
    assert result == 7575

def test_trim_top_7676():
    result = trim_top_2(7676)
    assert result == 7676

def test_trim_top_83():
    result = trim_top_2(83)
    assert result == 77

def test_trim_top_small():
    result = trim_top_2(10)
    assert result == 0

def trim_top_2(n: int):
    return trim_top(n, 2)

def test_take_repeating_pattern():
    result = take_repeating_pattern(123123, 2)
    assert result == 123

def test_empty_range_has_no_invalid():
    range = Range(1698522, 1698528)
    result = count_invalid(range)
    assert result == []

def test_single_invalid():
    range = Range(446443, 446449)
    result = count_invalid(range)
    assert result == [446446]

def test_multiple_invalid():
    range = Range(11, 22)
    result = count_invalid(range)
    assert result == [11, 22]

def test_998_1012():
    range = Range(998, 1012)
    result = count_invalid(range)
    assert result == [1010]

def test_solve_sample():
    result = solve("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124")
    assert result == 1227775554
