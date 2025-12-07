from step_result import StepResult


EMPTY = "."
BEAM = "|"
SPLIT = "^"
START = "S"
INVALID = "X"

def evaluate(prev_row: str, next_row: str) -> StepResult:
    prev_row = "".join([BEAM if i == START else i for i in prev_row])
    result_acc: list[str] = []
    for i in range(0, len(prev_row)):
        prev_section = get_section(prev_row, i)
        next_section = get_section(next_row, i)
        eval_char = evaluate_char(prev_section, next_section)
        result_acc.append(eval_char)
    result_row = "".join(result_acc)
    return StepResult(result_row, count_split(prev_row, result_row))

def get_section(row: str, index: int) -> str:
    result: list[str] = []
    result.append(row[index-1] if index > 0 else INVALID)
    result.append(row[index])
    result.append(row[index+1] if index < len(row) - 1 else INVALID)
    return "".join(result)

def evaluate_char(prev_char: str, next_char: str) -> str:
    if len(prev_char) != 3:
        raise ValueError(f"prev_char must be 3 in length, actual {prev_char}")
    if len(next_char) != 3:
        raise ValueError(f"next_char must be 3 in length, actual {next_char}")

    if next_char[1] == SPLIT:
        return SPLIT
    if prev_char[1] == BEAM and next_char[1] == EMPTY:
        return BEAM
    if prev_char[2] == BEAM and next_char[2] == SPLIT:
        return BEAM
    if prev_char[0] == BEAM and next_char[0] == SPLIT:
        return BEAM
    return EMPTY

def count_split(prev_row: str, result_row: str) -> int:
    result = 0
    for i in range(0, len(prev_row)):
        prev_section = get_section(prev_row, i)
        next_section = get_section(result_row, i)
        if is_split(prev_section, next_section):
            result = result + 1
    return result

def is_split(prev_section: str, next_section: str):
    if prev_section[0] == INVALID:
        return False
    if prev_section[2] == INVALID:
        return False
    return prev_section[1] == BEAM and next_section[1] == SPLIT

def count_total_split(rows: list[str]) -> int:
    result = 0
    evaluated_row = rows[0]
    for i in range(0, len(rows) - 1):
        next_row = rows[i+1]
        sub = evaluate(evaluated_row, next_row)
        evaluated_row = sub.row
        result = result + sub.num_split
    return result
