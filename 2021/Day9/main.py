import os
from read_input import read_input_as_string


def part_one():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")

    input_data = read_input_as_string(abs_file_path)

    height_map = [[int(height) for height in line] for line in input_data]
    low_points = []

    for y in range(0, len(height_map)):
        for x in range(0, len(height_map[y])):
            current_val = height_map[y][x]
            if (
                    is_lower_location(x, y, x, y - 1, height_map)
                    and is_lower_location(x, y, x, y + 1, height_map)
                    and is_lower_location(x, y, x + 1, y, height_map)
                    and is_lower_location(x, y, x - 1, y, height_map)
            ):
                low_points.append(current_val)
            else:
                pass

    risk_level_total = sum(low_points) + len(low_points)
    print(f"Total risk level: {risk_level_total}")


def is_lower_location(x, y, unsafe_x, unsafe_y, height_map):
    return (
            (not (0 <= unsafe_y < len(height_map) and 0 <= unsafe_x < len(height_map[unsafe_y])))
            or (height_map[y][x] < height_map[unsafe_y][unsafe_x])
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_one()
