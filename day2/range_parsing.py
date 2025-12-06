from range import Range


def split(s: str):
    return s.split(",") if s else []

def parse(s: str):
    [first, second] = s.split("-")
    return Range.create(first, second)

def trim_bottom(n: int, times: int):
    s = str(n)
    length = len(s)
    if length % times != 0:
        return next_invalid(length // times + 1, times)
    division_length = length // times
    first_num = int(s[:division_length] * times)
    if first_num >= n:
        return first_num

    lead_num = int(s[:division_length]) + 1
    return repeat(lead_num, times)

def next_invalid(size: int, times):
    power = int(pow(10, size - 1))
    return repeat(power, times)

def repeat(num: int, times: int):
    return int(str(num) * times)

def trim_top(n: int, times: int):
    s = str(n)
    length = len(s)
    if (length % times != 0):
        return prev_invalid((length // times) * times)
    division_length = length // times
    first_num = int(s[:division_length] * times)
    if first_num <= n:
        return first_num

    lead_num = int(s[:division_length]) - 1
    return repeat(lead_num, times)

def prev_invalid(size: int):
    return int("9" * size) if size else 0

def take_repeating_pattern(n: int, times: int):
    s = str(n)
    return int(s[:len(s) // times])

def count_invalid(r: Range, times):
    bottom = trim_bottom(r.start_num, times)
    top = trim_top(r.end_num, times)
    if (top < bottom):
        return []

    bottom = take_repeating_pattern(bottom, times)
    top = take_repeating_pattern(top, times)
    
    result = [int((str(i) * times)) for i in range(bottom, top + 1)]
    return result

def solve(s: str, times: int = 2):
    mapped = get_invalid_numbers(s, times)
    return sum(mapped)

def get_invalid_numbers(s: str, times: int):
    ranges = [parse(i) for i in split(s)]
    mapped = list(map(lambda x: count_invalid(x, times), ranges))
    return [item for sublist in mapped for item in sublist]

def solve_generic(s: str):
    invalid_numbers = set()
    for range in split(s):
        invalids = solve_generic_for_range(range)
        for invalid in invalids:
            invalid_numbers.add(invalid)
    return sum(invalid_numbers)

def solve_generic_for_range(s: str):
    max_len = len(s.split("-")[1])
    invalid_numbers = set()
    for times in range(2, max_len + 1):
        invalids = get_invalid_numbers(s, times)
        for invalid in invalids:
            invalid_numbers.add(invalid)
    return invalid_numbers
