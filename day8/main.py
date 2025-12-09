from circuit import solve


def main():
    with open("day8/input.txt", 'r') as file:
        input = file.readlines()
        cleaned = [s.strip("\n") for s in input]
        result = solve(cleaned, 1000)
        print(result)

if __name__ == "__main__":
    main()
