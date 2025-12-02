from solution import rotate_series

def test_empty_steps_returns_initial_state():
    result = rotate_series([])
    assert result == [50]

def test_single_step():
    result = rotate_series(["L68"])
    assert result == [50, 82]

def test_multiple_steps():
    result = rotate_series(["L68", "L30"])
    assert result == [50, 82, 52]
