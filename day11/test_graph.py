from day11.graph import Graph


def test_sample():
    with open("day11/input_sample.txt") as f:
        input = [line.strip() for line in f.readlines()]
    graph = Graph.create(input)
    assert len(graph.nodes) == 10
    assert "you" in graph.nodes
    assert graph.nodes["ccc"].next_nodes == ["ddd", "eee", "fff"]
    assert graph.nodes["iii"].next_nodes == ["out"]
    
    paths = graph.find_all_paths()
    assert len(paths) == 5

def test_find_all_paths_trivial():
    input = [
        "you: out",
    ]
    
    expected = [["you", "out"]]
    execute_find_all_paths(input, expected)

def test_find_all_paths_single_multi_hop():
    input = [
        "you: a",
        "a: out",
    ]
    
    expected = [["you", "a", "out"]]
    execute_find_all_paths(input, expected)

def test_find_all_paths_all_branches():
    input = [
        "you: a b",
        "a: out",
        "b: out",
    ]
    
    expected = [
        ["you", "a", "out"],
        ["you", "b", "out"],
    ]
    execute_find_all_paths(input, expected)

def test_find_all_paths_some_branches():
    input = [
        "you: a b c",
        "a: out",
        "c: out",
    ]
    
    expected = [
        ["you", "a", "out"],
        ["you", "c", "out"],
    ]
    execute_find_all_paths(input, expected)


def test_find_all_paths_different_branch_lengths():
    input = [
        "you: a b",
        "a: out",
        "b: c",
        "c: out",
    ]
    
    expected = [
        ["you", "a", "out"],
        ["you", "b", "c", "out"],
    ]
    execute_find_all_paths(input, expected)

def execute_find_all_paths(input: list[str], expected: list[list[str]]):
    graph = Graph.create(input)
    paths = graph.find_all_paths()
    assert set(map(tuple, paths)) == set(map(tuple, expected))
