from joltage import solve2

def main():
    with open("day3/input.txt", 'r') as file:
        input = file.readlines()
        result = solve2(input)
        print(result)

if __name__ == "__main__":
    main()
