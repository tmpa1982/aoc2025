def calculate(numbers: list[int], operation: str):
    match operation:
        case "*":
            return multiply(numbers)
        case "+":
            return add(numbers)
        case _:
            raise(ValueError(f"Invalid operation: {operation}"))

def multiply(numbers: list[int]):
    result = 1
    for number in numbers:
        result = result * number
    return result

def add(numbers: list[int]):
    result = 0
    for number in numbers:
        result = result + number
    return result

def solve(input: list[str]):
    parsed_numbers = []
    for row in input[:-1]:
        parsed = parse_number_row(row)
        parsed_numbers.append(parsed)

    operation = [i for i in input[-1].split(" ") if i]
    
    result = 0
    for i in range(0, len(operation)):
        numbers = get_numbers(parsed_numbers, i)
        op = operation[i]
        col_result = calculate(numbers, op)
        result = result + col_result
    
    return result

def parse_number_row(s: str):
    return [int(i) for i in s.split(" ") if i]

def get_numbers(parsed: list[list[int]], index):
    result = []
    for l in parsed:
        result.append(l[index])
    return result
