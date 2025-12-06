from cephalopod import solve


def test_solve_multiplication():
    input = [
        "2",
        "3",
        "4",
        "*",
    ]
    
    result = solve(input)
    assert result == 24

def test_solve_addition():
    input = [
        "2",
        "3",
        "4",
        "+",
    ]
    
    result = solve(input)
    assert result == 9

def test_solve_multiple():
    input = [
        "2 2",
        "3 3",
        "4 4",
        "+ *",
    ]
    
    result = solve(input)
    assert result == 33

def test_solve_parses_extra_spaces():
    input = [
        " 2  2 ",
        " 2  3 ",
        " +  * ",
    ]
    
    result = solve(input)
    assert result == 10

def test_solve_sample():
    input = [
        "123 328  51 64",
        "45 64  387 23",
        "6 98  215 314",
        "*   +   *   +",
    ]
    
    result = solve(input)
    assert result == 4277556
