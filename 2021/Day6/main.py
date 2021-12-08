import os
from read_input import read_input_as_string

SIMULATION_DAYS = 256


def part_one_and_two():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    input_data = read_input_as_string(abs_file_path)
    fish_initial_ages = [int(age) for line in input_data for age in line.split(",")]

    fish_age_count = {k: 0 for k in range(0, 8 + 1)}

    for age in fish_initial_ages:
        fish_age_count[age] += 1

    print(fish_age_count)

    for i in range(SIMULATION_DAYS):
        tmp_fish_age_count = {k: 0 for k in range(0, 8 + 1)}
        for j in range(0, 8 + 1):
            if j == 0:
                tmp_fish_age_count[6] = tmp_fish_age_count.get(6, 0) + fish_age_count[j]
                tmp_fish_age_count[8] = tmp_fish_age_count.get(8, 0) + fish_age_count[j]
            else:
                tmp_fish_age_count[j - 1] = tmp_fish_age_count.get(j - 1, 0) + fish_age_count[j]
        fish_age_count = tmp_fish_age_count

        print(sum(fish_age_count.values()))

    total = sum(fish_age_count.values())
    print(f"Total fish: {total}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_one_and_two()
