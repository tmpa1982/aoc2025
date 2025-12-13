from day10.solution import solve, solve2


def main():
    with open("day10/input.txt", 'r') as file:
        input = file.readlines()
        cleaned = [s.strip("\n") for s in input]
        result = solve(cleaned)
        print("Part 1: ", result)
        result2 = solve2(cleaned)
        print("Part 2: ", result2)

if __name__ == "__main__":
    main()
