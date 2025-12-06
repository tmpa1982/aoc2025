import pytest
from fresh_range import FreshRange, count_fresh, count_spoiled, parse_input, parse_range, solve, solve2


def test_in_range():
    range = FreshRange(3, 5)
    assert range.contains(4) == True

def test_start_in_range():
    range = FreshRange(3, 5)
    assert range.contains(3) == True

def test_end_in_range():
    range = FreshRange(3, 5)
    assert range.contains(5) == True

def test_small_out_of_range():
    range = FreshRange(3, 5)
    assert range.contains(2) == False

def test_large_out_of_range():
    range = FreshRange(3, 5)
    assert range.contains(6) == False

def test_parses_range():
    result = parse_range("3-5")
    assert result == FreshRange(3, 5)

def test_parse_input():
    input = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]
    
    (ranges, ingredients) = parse_input(input)
    
    assert ranges == [FreshRange(3, 5), FreshRange(10, 14), FreshRange(16, 20), FreshRange(12, 18)]
    assert ingredients == [1, 5, 8, 11, 17, 32]

def test_count_in_range():
    result = count_spoiled([FreshRange(3, 5)], [4])
    assert result == 1

def test_count_multiple_in_range():
    result = count_spoiled([FreshRange(3, 5)], [3, 4, 5])
    assert result == 3

def test_count_in_multiple_ranges():
    result = count_spoiled([FreshRange(3, 5), FreshRange(2, 6)], [4])
    assert result == 1

def test_sample_solution():
    input = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]

    result = solve(input)
    assert result == 3

def test_count_fresh_ingredients():
    result = count_fresh([FreshRange(3, 5)])
    assert result == 3

def test_count_fresh_ingredients_multiple_ranges():
    result = count_fresh([FreshRange(3, 5), FreshRange(8, 9)])
    assert result == 5

def test_count_fresh_ingredients_overlapping_ranges():
    result = count_fresh([FreshRange(3, 5), FreshRange(4, 6)])
    assert result == 4

def test_count_fresh_sample():
    input = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]

    result = solve2(input)
    assert result == 14

def test_overlap_other_start():
    range = FreshRange(3, 5)
    other = FreshRange(4, 6)

    assert range.has_overlap(other) == True
    assert other.has_overlap(range) == True

def test_overlap_other_end():
    range = FreshRange(3, 5)
    other = FreshRange(2, 4)

    assert range.has_overlap(other) == True
    assert other.has_overlap(range) == True

def test_overlap_edge():
    range = FreshRange(3, 5)
    other = FreshRange(5, 7)

    assert range.has_overlap(other) == True
    assert other.has_overlap(range) == True

def test_no_overlap():
    range = FreshRange(3, 5)
    other = FreshRange(6, 7)

    assert range.has_overlap(other) == False
    assert other.has_overlap(range) == False

def test_merge_right():
    range = FreshRange(3, 5)
    other = FreshRange(4, 6)

    result = range.assemble(other)

    assert result == FreshRange(3, 6)

def test_merge_left():
    range = FreshRange(3, 5)
    other = FreshRange(2, 4)

    result = range.assemble(other)

    assert result == FreshRange(2, 5)

def test_no_merge():
    range = FreshRange(3, 5)
    other = FreshRange(7, 9)

    with pytest.raises(ValueError):
        range.assemble(other)
