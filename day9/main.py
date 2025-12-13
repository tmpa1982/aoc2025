from day9.solution9 import solve2


def main():
    with open("day9/input_transformed.txt", 'r') as file:
        input = file.readlines()
        cleaned = [s.strip("\n") for s in input]
        result = solve2(cleaned)
        print(f"Part 2: {result}")

if __name__ == "__main__":
    main()
