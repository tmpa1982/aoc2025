from solution9 import solve


def test_solve_sample():
    with open("day9/input_sample.txt", 'r') as file:
        input = file.readlines()
        
        result = solve(input)
        
        assert result == 50
