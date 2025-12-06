from cephalopod2 import solve

def test_solve_multiplication():
    input = [
        "2",
        "3",
        "4",
        "*",
    ]

    result = solve(input)
    assert result == 234

def test_solve_addition():
    input = [
        "2",
        "3",
        "4",
        "+",
    ]

    result = solve(input)
    assert result == 234

def test_solve_multiplication_left_aligned():
    input = [
        "12",
        "3 ",
        "* ",
    ]

    result = solve(input)
    assert result == 26

def test_solve_addition_right_aligned():
    input = [
        "21",
        " 3",
        "+ ",
    ]

    result = solve(input)
    assert result == 15

def test_solve_addition_from_non_first_line():
    input = [
        " 1 ",
        "132",
        " 51",
        "+  ",
    ]

    result = solve(input)
    assert result == 1 + 135 + 21


def test_solve_multiple_columns():
    input = [
        "12 21",
        "3   4",
        "*  + ",
    ]

    result = solve(input)
    assert result == 42
