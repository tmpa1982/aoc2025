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

def joltage_high(s: str):
    length = len(s)
    if (length < 13):
        return int(s)

    nums = trim_left_small([int(c) for c in s])
    num_to_remove = len(nums) - 12

    for _ in range(num_to_remove):
        i = find_left_min_index(nums)
        del nums[i]
    return int("".join(map(str, nums)))

def trim_left_small(nums: list[int]):
    arr = nums
    min_size = 12
    result = []
    while True:
        trimmed = trim_left_small_once(arr, min_size)
        if trimmed is None:
            return result + arr
        else:
            result.append(trimmed[0])
            arr = trimmed[1:]
            min_size = min_size - 1
    return result

def trim_left_small_once(nums: list[int], min_size: int):
    length = len(nums)
    for n in range(9, 0, -1):
        for index, val in enumerate(nums):
            if val == n and length - index >= min_size:
                return nums[index:]
    return None

def find_left_min_index(nums: list[int]):
    result = 0
    value = nums[0]
    for index, val in enumerate(nums):
        if val < value:
            value = val
            result = index
    return result

def solve2(arr: list[str]):
    return sum([joltage_high(s.strip()) for s in arr])
