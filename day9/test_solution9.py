from day9.solution9 import solve, solve2


def test_solve_sample():
    with open("day9/input_sample.txt", 'r') as file:
        input = file.readlines()
        
        result = solve(input)
        
        assert result == 50

def test_solve2_sample():
    with open("day9/input_sample.txt", 'r') as file:
        input = file.readlines()
        
        result = solve2(input)
        
        assert result == 24
