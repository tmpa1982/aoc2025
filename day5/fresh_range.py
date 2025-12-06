class FreshRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def contains(self, element: int):
        return self.start <= element <= self.end

    def has_overlap(self, other: FreshRange):
        if self.contains(other.start):
            return True
        if self.contains(other.end):
            return True
        if other.contains(self.start):
            return True
        if other.contains(self.end):
            return True
        return False

    def assemble(self, other: FreshRange):
        if not self.has_overlap(other):
            raise ValueError(f"No overlap with {other}")
        start = min(self.start, other.start)
        end = max(self.end, other.end)
        return FreshRange(start, end)
    
    def __eq__(self, value):
        return self.start == value.start and self.end == value.end
    
    def __repr__(self):
        return f"{self.start}-{self.end}"

def parse_range(s: str):
    [start, end] = s.split("-")
    return FreshRange(int(start), int(end))

def parse_input(lines: list[str]):
    sep = find_separator_index(lines)
    ranges = [parse_range(i) for i in lines[:sep]]
    ingredients = [int(i) for i in lines[sep+1:]]
    return (ranges, ingredients)

def count_spoiled(ranges: list[FreshRange], ingredients: list[int]):
    result = 0
    for ingredient in ingredients:
        if is_spoiled(ingredient, ranges):
            result = result + 1
    return result

def is_spoiled(ingredient: int, ranges: list[FreshRange]):
    for range in ranges:
        if range.contains(ingredient):
            return True
    return False

def find_separator_index(lines: list[str]):
    for index, element in enumerate(lines):
        if element == "":
            return index
    raise ValueError("lines list does not contain empty string separator")

def solve(lines: list[str]):
    (ranges, ingredients) = parse_input(lines)
    return count_spoiled(ranges, ingredients)

def merge_overlaps(ranges: list[FreshRange]):
    result = ranges
    iteration_result = []
    while True:
        iteration_result = merge_overlaps_iteration(result)
        if iteration_result == result:
            return result
        else:
            result = iteration_result

def merge_overlaps_iteration(ranges: list[FreshRange]):
    result = []
    for new_range in ranges:
        has_merge = False
        for index, existing in enumerate(result):
            if (new_range.has_overlap(existing)):
                merged = new_range.assemble(existing)
                del result[index]
                result.append(merged)
                has_merge = True
        if not has_merge:
            result.append(new_range)
    print(f"iteration: {result}")
    return result

def count_fresh(ranges: list[FreshRange]):
    merged = merge_overlaps(ranges)
    print(merged)
    result = 0
    for r in merged:
        result = result + r.end - r.start + 1
    return result

def solve2(lines: list[str]):
    (ranges, _) = parse_input(lines)
    return count_fresh(ranges)
