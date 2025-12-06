class FreshRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def contains(self, element: int):
        return self.start <= element <= self.end
    
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
