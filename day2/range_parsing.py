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
    first = int(s[:division_length])
    second = int(s[division_length:2*division_length])
    lead_num = first + 1 if (first < second) else first
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
    first = int(s[:division_length])
    second = int(s[division_length:2*division_length])
    lead_num = first - 1 if (first > second) else first
    return repeat(lead_num, times)

def prev_invalid(size: int):
    return int("9" * size)

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
    
    return [int((str(i) * times)) for i in range(bottom, top + 1)]

def solve(s: str, times: int = 2):
    ranges = [parse(i) for i in split(s)]
    mapped = list(map(lambda x: count_invalid(x, times), ranges))
    return sum([sum(i) for i in mapped])
