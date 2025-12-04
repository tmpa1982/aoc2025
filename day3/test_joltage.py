from joltage import joltage, joltage_high, solve

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

def test_joltage_high():
    result = joltage_high("987654321111111")
    assert result == 987654321111

    result = joltage_high("811111111111119")
    assert result == 811111111119

    result = joltage_high("234234234234278")
    assert result == 434234234278

    result = joltage_high("818181911112111")
    assert result == 888911112111

    result = joltage_high("6417428721465223591487332938321284254443151533425567683625237482423323523215265251829988331453263337")
    assert result == 999988563337
