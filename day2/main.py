from range_parsing import solve

def main():
    with open("day2/input.txt", 'r') as file:
        input = file.readline()
        result = solve(input)
        print(result)

if __name__ == "__main__":
    main()
