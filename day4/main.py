from paper_roll import Board

def main():
    with open("day4/input.txt", 'r') as file:
        input = file.readlines()
        layout = [s.strip() for s in input]
        total = 0
        while True:
            board = Board(layout)
            num_accessible = board.count_accessible()
            print(num_accessible)
            if num_accessible == 0:
                break
            else:
                total = total + num_accessible
                layout = board.remove_accessible()
        print(total)

if __name__ == "__main__":
    main()
