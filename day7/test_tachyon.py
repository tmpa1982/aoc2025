from step_result import StepResult
from tachyon import count_total_split, evaluate


def test_step():
    prev_row = "|"
    next_row = "."
    result = evaluate(prev_row, next_row)
    assert result == StepResult("|", 0)

def test_empty_step():
    prev_row = "."
    next_row = "."
    result = evaluate(prev_row, next_row)
    assert result == StepResult(".", 0)

def test_step_from_start():
    prev_row = "S"
    next_row = "."
    result = evaluate(prev_row, next_row)
    assert result == StepResult("|", 0)

def test_split():
    prev_row = ".|."
    next_row = ".^."
    result = evaluate(prev_row, next_row)
    assert result == StepResult("|^|", 1)

def test_split_right():
    prev_row = "|."
    next_row = "^."
    result = evaluate(prev_row, next_row)
    assert result == StepResult("^|", 0)

def test_split_left():
    prev_row = ".|"
    next_row = ".^"
    result = evaluate(prev_row, next_row)
    assert result == StepResult("|^", 0)

def test_beam_merge():
    prev_row = ".|.|."
    next_row = ".^.^."
    result = evaluate(prev_row, next_row)
    assert result == StepResult("|^|^|", 2)

def test_count_total_split():
    input = [
        "..S..",
        "..^..",
        ".^.^.",
    ]
    
    result = count_total_split(input)
    assert result == 3

def test_sample():
    input = [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
    ]
    
    result = count_total_split(input)
    assert result == 21
