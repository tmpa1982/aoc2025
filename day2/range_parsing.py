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
    power = int(pow(10, half))
    lead_num = first + 1 if (first < second) else first
    return lead_num * power + lead_num

def next_invalid(size: int):
    half = size / 2
    exp = half - 1
    power = int(pow(10, exp))
    return power * (int(pow(10, half)) + 1)

def trim_top(n: int):
    s = str(n)
    length = len(s)
    if (length % 2 == 1):
        return prev_invalid(length - 1)
    half = length // 2
    first = int(s[:half])
    second = int(s[half:])
    power = int(pow(10, half))
    lead_num = first - 1 if (first > second) else first
    return lead_num * power + lead_num

def prev_invalid(size: int):
    return int("9" * size)

def take_half(n: int):
    s = str(n)
    length = len(s)
    half = length // 2
    return int(s[:half])

def count_invalid(r: Range):
    bottom = trim_bottom(r.start_num)
    top = trim_top(r.end_num)
    if (top < bottom):
        return []

    bottom = take_half(bottom)
    top = take_half(top)
    
    return [int((str(i) * 2)) for i in range(bottom, top + 1)]

def solve(s: str):
    ranges = [parse(i) for i in split(s)]
    mapped = list(map(count_invalid, ranges))
    return sum([sum(i) for i in mapped])
