from day9.solution9 import solve, solve2


def main():
    with open("day9/input.txt", 'r') as file:
        input = file.readlines()
        cleaned = [s.strip("\n") for s in input]
        result = solve(cleaned)
        print(f"Part 1: {result}")
        result = solve2(cleaned)
        print(f"Part 2: {result}")

if __name__ == "__main__":
    main()
