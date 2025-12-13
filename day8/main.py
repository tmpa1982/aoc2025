from day8.circuit import solve
from day8.mst import solve2


def main():
    with open("day8/input.txt", 'r') as file:
        input = file.readlines()
        cleaned = [s.strip("\n") for s in input]
        result = solve(cleaned, 1000)
        print(f"Part 1: {result}")
        result = solve2(cleaned)
        print(f"Part 2: {result}")

if __name__ == "__main__":
    main()
