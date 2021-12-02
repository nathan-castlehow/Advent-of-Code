from read_input import read_input_as_string
import os

FORWARD = "forward"
DOWN = "down"
UP = "up"


def part_one():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    question_input = read_input_as_string(abs_file_path)

    position = 0
    depth = 0
    for i in question_input:
        command_values = i.split(" ")
        command = command_values[0].strip()
        value = int(command_values[1].strip())

        if command == FORWARD:
            position += value
        if command == DOWN:
            depth += value
        if command == UP:
            depth -= value

    print("Depth: " + str(depth))
    print("Position: " + str(position))
    print("Total: " + str(depth * position))


def part_two():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    question_input = read_input_as_string(abs_file_path)

    position = 0
    depth = 0
    aim = 0
    for i in question_input:
        command_values = i.split(" ")
        command = command_values[0].strip()
        value = int(command_values[1].strip())

        if command == FORWARD:
            position += value
            depth += aim * value
        if command == DOWN:
            aim += value
        if command == UP:
            aim -= value

    print("Depth: " + str(depth))
    print("Position: " + str(position))
    print("Total: " + str(depth * position))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_one()
