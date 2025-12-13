from day12.region import Region


def solve(input: list[str]) -> int:
    regions = [Region.parse(line) for line in input]
    result = len(regions)
    return result
