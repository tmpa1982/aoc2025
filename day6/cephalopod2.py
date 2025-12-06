from calc import calculate


def solve(input: list[str]):
    parsed_numbers = []
    for row in input[:-1]:
        parsed = parse_number_row(row)
        parsed_numbers.append(parsed)

    operation = input[-1]

    result = 0
    index = 0
    while True:
        op = operation[index]
        next_index = find_next_index(parsed_numbers, index)
        numbers = get_numbers(parsed_numbers, index, next_index)
        col_result = calculate(numbers, op)
        result = result + col_result
        index = next_index + 1
        if (next_index >= len(operation)):
            return result

def find_next_index(parsed_numbers: list[list[int | None]], index: int):
    result = index + 1
    is_complete = False
    while True:
        if is_empty_at_column_index(parsed_numbers, result):
            return result
        else:
            result = result + 1

def is_empty_at_column_index(parsed_numbers: list[list[int | None]], index: int):
    for row in parsed_numbers:
        if index < len(row) and row[index]:
            return False
    return True

def parse_number_row(s: str):
    return [None if not i or i == " " else int(i) for i in s]

def get_numbers(parsed: list[list[int]], start, end):
    result = []
    for i in range(start, end):
        num = []
        for l in parsed:
            if l[i]:
                num.append(str(l[i]))
        result.append(int("".join(num)))
    return result
