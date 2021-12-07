import os
from read_input import read_input_as_string


def part_one():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    input_data = read_input_as_string(abs_file_path)
    lantern_fish_ages = [int(age) for line in input_data for age in line.split(",")]

    print(lantern_fish_ages)


def part_two():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_one()
