from range import Range


def split(s: str):
    return s.split(",") if s else []

def parse(s: str):
    [first, second] = s.split("-")
    return Range.create(first, second)

def trim_bottom(n: int):
    s = str(n)
    length = len(s)
    if (length % 2 == 1):
        return next_invalid(length + 1)
    half = length // 2
    first = int(s[:half])
    second = int(s[half:])
    power = pow(10, half)
    lead_num = first + 1 if (first < second) else first
    return lead_num * power + lead_num

def next_invalid(size: int):
    half = size / 2
    exp = half - 1
    power = pow(10, exp)
    return power * (pow(10, half) + 1)

def trim_top(n: int):
    s = str(n)
    length = len(s)
    if (length % 2 == 1):
        return prev_invalid(length - 1)
    half = length // 2
    first = int(s[:half])
    second = int(s[half:])
    power = pow(10, half)
    lead_num = first - 1 if (first > second) else first
    return lead_num * power + lead_num

def prev_invalid(size: int):
    return int("9" * size)
