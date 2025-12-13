from day10.lights_machine import LightsMachine


def solve(input: list[str]) -> int:
    result = 0
    for line in input:
        machine = LightsMachine.parse(line)
        path = machine.find_shortest_path()
        result += len(path)
    return result

def solve2(input: list[str]) -> int:
    for line in input:
        machine = LightsMachine.parse(line)
        num_buttons = len(machine.buttons)
        num_joltage = len(machine.joltage)
        if num_buttons > num_joltage:
            print(f"Warning: more buttons ({num_buttons}) than joltage ratings ({num_joltage})")
    return 0
