from day12.region import Region


def solve(input: list[str]) -> int:
    trivial_fit = 0
    trivial_no_fit = 0
    regions = [Region.parse(line) for line in input]
    for region in regions:
        if region.is_trivial_fit():
            trivial_fit += 1
        elif region.is_trivial_no_fit():
            trivial_no_fit += 1
    undetermined = len(regions) - trivial_fit - trivial_no_fit
    print(f"Trivial fit: {trivial_fit}, trivial no fit: {trivial_no_fit}, undetermined: {undetermined}")
    return trivial_fit
