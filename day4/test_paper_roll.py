from paper_roll import Board, Coordinate


def test_no_neighbor_is_accessible():
    layout = [
        "...",
        ".@.",
        "...",
    ]
    coordinate = Coordinate(1, 1)
    exec_test_accessible(layout, coordinate)

def test_one_neighbor_is_accessible():
    layout = [
        ".@.",
        ".@.",
        "...",
    ]
    coordinate = Coordinate(1, 1)
    exec_test_accessible(layout, coordinate)

def test_one_diagonal_neighbor_is_accessible():
    layout = [
        "...",
        ".@.",
        "..@",
    ]
    coordinate = Coordinate(1, 1)
    exec_test_accessible(layout, coordinate)

def test_two_diagonal_neighbors_is_accessible():
    layout = [
        "..@",
        ".@.",
        "..@",
    ]
    coordinate = Coordinate(1, 1)
    exec_test_accessible(layout, coordinate)

def test_three_diagonal_neighbors_is_accessible():
    layout = [
        "..@",
        ".@.",
        "@.@",
    ]
    coordinate = Coordinate(1, 1)
    exec_test_accessible(layout, coordinate)

def test_four_diagonal_neighbors_is_not_accessible():
    layout = [
        "@.@",
        ".@.",
        "@.@",
    ]
    coordinate = Coordinate(1, 1)
    exec_test_not_accessible(layout, coordinate)

def test_top_left_corner_is_accessible():
    layout = [
        "@.@",
        ".@.",
        "@.@",
    ]
    coordinate = Coordinate(0, 0)
    exec_test_accessible(layout, coordinate)

def test_bottom_right_corner_is_accessible():
    layout = [
        "@.@",
        ".@.",
        "@.@",
    ]
    coordinate = Coordinate(2, 2)
    exec_test_accessible(layout, coordinate)

def test_empty_cell_is_not_accessible():
    layout = [
        "..@",
        "...",
        "@.@",
    ]
    coordinate = Coordinate(1, 1)
    exec_test_not_accessible(layout, coordinate)

def test_count_accessible():
    layout = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@."
    ]
    exec_test_not_accessible(layout, Coordinate(7, 0))
    
    board = Board(layout)
    assert board.count_accessible() == 13

def test_remove_accessible():
    layout = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@."
    ]

    board = Board(layout)
    new_layout = [
        ".......@..",
        ".@@.@.@.@@",
        "@@@@@...@@",
        "@.@@@@..@.",
        ".@.@@@@.@.",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "..@@@.@@@@",
        ".@@@@@@@@.",
        "....@@@..."
    ]
    assert board.remove_accessible() == new_layout

def exec_test_accessible(layout, coordinate):
    board = Board(layout)
    
    assert board.is_accessible(coordinate)

def exec_test_not_accessible(layout, coordinate):
    board = Board(layout)
    
    assert not board.is_accessible(coordinate)
