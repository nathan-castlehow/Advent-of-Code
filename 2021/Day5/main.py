import os
from read_input import read_input_as_string


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class HydrothermalVent:
    def __init__(self, serialized_vent):
        self.__deserialize_vent(serialized_vent)

    def __deserialize_vent(self, serialized_vent):
        positions = serialized_vent.split(" -> ")
        assert len(positions) == 2

        self.start_position = position_from_list([int(position) for position in positions[0].split(",")])
        self.end_position = position_from_list([int(position) for position in positions[1].split(",")])


def position_from_list(position_list):
    (x, y) = position_list
    return Position(x, y)


def part_one():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    input_data = read_input_as_string(abs_file_path)

    ocean_floor = {}
    hydrothermal_vents = [HydrothermalVent(serialized_vent) for serialized_vent in input_data]

    for vent in hydrothermal_vents:
        if vent.start_position.x == vent.end_position.x:
            min_y = min(vent.start_position.y, vent.end_position.y)
            for i in range(abs(vent.start_position.y - vent.end_position.y) + 1):
                key = (vent.start_position.x, min_y + i)
                ocean_floor[key] = ocean_floor.get(key, 0) + 1

        elif vent.start_position.y == vent.end_position.y:
            min_x = min(vent.start_position.x, vent.end_position.x)
            for i in range(abs(vent.start_position.x - vent.end_position.x) + 1):
                key = (min_x + i, vent.start_position.y)
                ocean_floor[key] = ocean_floor.get(key, 0) + 1

    overlapping_points_count = len(list(filter(lambda x: x > 1, ocean_floor.values())))

    print(f"Overlapping points: {overlapping_points_count}")


def part_two():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    input_data = read_input_as_string(abs_file_path)

    ocean_floor = {}
    hydrothermal_vents = [HydrothermalVent(serialized_vent) for serialized_vent in input_data]

    for vent in hydrothermal_vents:
        if vent.start_position.x == vent.end_position.x:
            min_y = min(vent.start_position.y, vent.end_position.y)
            for i in range(abs(vent.start_position.y - vent.end_position.y) + 1):
                key = (vent.start_position.x, min_y + i)
                ocean_floor[key] = ocean_floor.get(key, 0) + 1

        elif vent.start_position.y == vent.end_position.y:
            min_x = min(vent.start_position.x, vent.end_position.x)
            for i in range(abs(vent.start_position.x - vent.end_position.x) + 1):
                key = (min_x + i, vent.start_position.y)
                ocean_floor[key] = ocean_floor.get(key, 0) + 1
        else:
            step_x = -1 if vent.start_position.x > vent.end_position.x else 1
            step_y = -1 if vent.start_position.y > vent.end_position.y else 1

            for i in range(abs(vent.start_position.x - vent.end_position.x) + 1):
                key = (vent.start_position.x +(i * step_x), vent.start_position.y + (i * step_y))
                ocean_floor[key] = ocean_floor.get(key, 0) + 1

    overlapping_points_count = len(list(filter(lambda x: x > 1, ocean_floor.values())))

    print(f"Overlapping points: {overlapping_points_count}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_two()
