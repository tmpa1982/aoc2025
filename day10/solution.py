from lights_machine import LightsMachine


def solve(input: list[str]) -> int:
    result = 0
    for line in input:
        machine = LightsMachine.parse(line)
        path = machine.find_shortest_path()
        result += len(path)
    return result
