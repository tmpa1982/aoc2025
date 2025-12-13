from day12.solution import solve


def main():
    with open("day12/input.txt") as f:
        input = [line.strip() for line in f.readlines()]
        result = solve(input)
        print(f"Part 1: {result}")

if __name__ == "__main__":
    main()
