from solution import solve2

def main():
    with open("day1/input.txt", 'r') as file:
        input = file.readlines()
        result = solve2(input)
        print(result)

if __name__ == "__main__":
    main()
