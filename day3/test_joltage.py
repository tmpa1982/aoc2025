from joltage import joltage, solve

def test_joltage_first_two_digits():
    result = joltage("987654321111111")
    assert result == 98

def test_joltage_last_digit_largest():
    result = joltage("811111111111119")
    assert result == 89

def test_joltage_last_two_digits():
    result = joltage("234234234234278")
    assert result == 78

def test_joltage_middle():
    result = joltage("818181911112111")
    assert result == 92

def test_sample_solution():
    input = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]
    result = solve(input)
    assert result == 357
