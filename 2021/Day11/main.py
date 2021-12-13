import os
from read_input import read_input_as_string

STEPS = 10000


def part_one():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    input_data = read_input_as_string(abs_file_path)

    octopus_grid = [[int(octopus_energy) for octopus_energy in line] for line in input_data]

    flashes = 0
    for i in range(STEPS):
        is_step_complete = False
        for y in range(0, len(octopus_grid)):
            print(''.join([str(octo) for octo in octopus_grid[y]]))
        print("------------------------------------")

        for y in range(0, len(octopus_grid)):
            for x in range(0, len(octopus_grid[y])):
                if octopus_grid[y][x] != -1:
                    octopus_grid[y][x] += 1

        while not is_step_complete:
            has_flashed = False
            for y in range(0, len(octopus_grid)):
                for x in range(0, len(octopus_grid[y])):
                    if octopus_grid[y][x] > 9:
                        octopus_grid[y][x] = -1
                        flashes += 1
                        has_flashed = True

                        #  up
                        safe_update(x, y + 1, octopus_grid)
                        safe_update(x - 1, y + 1, octopus_grid)
                        safe_update(x + 1, y + 1, octopus_grid)

                        # down
                        safe_update(x, y - 1, octopus_grid)
                        safe_update(x - 1, y - 1, octopus_grid)
                        safe_update(x + 1, y - 1, octopus_grid)

                        # left / right
                        safe_update(x + 1, y, octopus_grid)
                        safe_update(x - 1, y, octopus_grid)

            is_step_complete = not has_flashed

        # reset -1 to  0's
        for y in range(0, len(octopus_grid)):
            for x in range(0, len(octopus_grid[y])):
                if octopus_grid[y][x] == -1:
                    octopus_grid[y][x] = 0

    print(f"Total flashes: {flashes}")


def part_two():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    input_data = read_input_as_string(abs_file_path)

    octopus_grid = [[int(octopus_energy) for octopus_energy in line] for line in input_data]

    for i in range(STEPS):
        inner_flashes = 0
        is_step_complete = False
        for y in range(0, len(octopus_grid)):
            print(''.join([str(octo) for octo in octopus_grid[y]]))
        print("------------------------------------")

        for y in range(0, len(octopus_grid)):
            for x in range(0, len(octopus_grid[y])):
                if octopus_grid[y][x] != -1:
                    octopus_grid[y][x] += 1

        while not is_step_complete:
            has_flashed = False
            for y in range(0, len(octopus_grid)):
                for x in range(0, len(octopus_grid[y])):
                    if octopus_grid[y][x] > 9:
                        octopus_grid[y][x] = -1
                        inner_flashes += 1
                        has_flashed = True

                        #  up
                        safe_update(x, y + 1, octopus_grid)
                        safe_update(x - 1, y + 1, octopus_grid)
                        safe_update(x + 1, y + 1, octopus_grid)

                        # down
                        safe_update(x, y - 1, octopus_grid)
                        safe_update(x - 1, y - 1, octopus_grid)
                        safe_update(x + 1, y - 1, octopus_grid)

                        # left / right
                        safe_update(x + 1, y, octopus_grid)
                        safe_update(x - 1, y, octopus_grid)

            is_step_complete = not has_flashed

        # reset -1 to  0's
        for y in range(0, len(octopus_grid)):
            for x in range(0, len(octopus_grid[y])):
                if octopus_grid[y][x] == -1:
                    octopus_grid[y][x] = 0

        if inner_flashes == (len(octopus_grid) * len(octopus_grid[0])):
            break

    print(f"Step: {i + 1}")


def safe_update(unsafe_x, unsafe_y, grid):
    if 0 <= unsafe_y < len(grid) and 0 <= unsafe_x < len(grid[unsafe_y]) \
            and grid[unsafe_y][unsafe_x] != -1:
        grid[unsafe_y][unsafe_x] += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_two()
