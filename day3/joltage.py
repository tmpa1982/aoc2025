def joltage(s: str):
    nums = [int(c) for c in s]
    max_index = 0
    for index, num in enumerate(nums[1:-1]):
        if (num > nums[max_index]):
            max_index = index + 1

    offset = max_index + 1
    max_index2 = offset
    for index, num in enumerate(nums[offset:]):
        if (num > nums[max_index2]):
            max_index2 = offset + index
    
    print(f"{s}: {max_index} {max_index2} {nums[max_index]}{nums[max_index2]}")
    return nums[max_index] * 10 + nums[max_index2]

def solve(arr: list[str]):
    return sum([joltage(s.strip()) for s in arr])
