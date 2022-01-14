import os
import sys

from read_input import read_input_as_string


def part_one():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    input_data = [int(pos) for pos in read_input_as_string(abs_file_path)[0].split(",")]

    min_crab_pos = min(input_data)
    max_crab_pos = max(input_data)

    cost_per_pos = {}
    for i in range(min_crab_pos, max_crab_pos + 1):
        fuel_usage = 0
        for crab in input_data:
            fuel_usage += abs(crab - i)
        cost_per_pos[i] = fuel_usage

    min_fuel = 99999999
    for fuel in cost_per_pos.values():
        if fuel < min_fuel:
            min_fuel = fuel

    print(f"Fuel: {min_fuel}")


def part_two():

    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    input_data = [int(pos) for pos in read_input_as_string(abs_file_path)[0].split(",")]

    min_crab_pos = min(input_data)
    max_crab_pos = max(input_data)

    cost_per_pos = {}
    for i in range(min_crab_pos, max_crab_pos + 1):
        fuel_usage = 0
        for crab in input_data:
            n = abs(crab - i)
            fuel_usage += (n * (n + 1)) / 2
        cost_per_pos[i] = fuel_usage

    min_fuel = 99999999
    for fuel in cost_per_pos.values():
        if fuel < min_fuel:
            min_fuel = fuel

    print(f"Fuel: {min_fuel}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_one()
