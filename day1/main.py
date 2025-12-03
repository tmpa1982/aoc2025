from solution import solve

def main():
    with open("day1/input.txt", 'r') as file:
        input = file.readlines()
        result = solve(input)
        print(result)

if __name__ == "__main__":
    main()
