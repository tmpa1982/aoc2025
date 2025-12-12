from day1.solution import count_zeros, rotate_series, solve

def test_empty_steps_returns_initial_state():
    result = rotate_series([])
    assert result == [50]

def test_single_step():
    result = rotate_series(["L68"])
    assert result == [50, 82]

def test_multiple_steps():
    result = rotate_series(["L68", "L30"])
    assert result == [50, 82, 52]

def test_count_no_zeros():
    result = count_zeros([1, 2, 3])
    assert result == 0

def test_count_one_zero():
    result = count_zeros([1, 0, 3])
    assert result == 1

def test_count_multiple_zeros():
    result = count_zeros([1, 0, 3, 0, 0, 7, 0])
    assert result == 4

def test_sample_solution():
    result = solve([
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ])
    assert result == 3
