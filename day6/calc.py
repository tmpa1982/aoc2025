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
