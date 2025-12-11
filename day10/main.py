from solution import solve


def main():
    with open("day10/input.txt", 'r') as file:
        input = file.readlines()
        cleaned = [s.strip("\n") for s in input]
        result = solve(cleaned)
        print(result)

if __name__ == "__main__":
    main()
