import os
from read_input import read_input_as_string

SIMULATION_DAYS = 256


def part_one():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    input_data = read_input_as_string(abs_file_path)
    print(input_data[1])

    height_map = [[int(height) for height in line.split()] for line in input_data]

    print(height_map[1])
    # find current max / min position
    # move downwards?
    # weighted average?


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_one()
