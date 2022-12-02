from read_input import read_input_as_int, read_input_as_string
import os


def part_one():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    question_input = read_input_as_string(abs_file_path)

    groups = []

    currentGroup = []
    for line in question_input:
        if line == "":
            groups.append(currentGroup)
            currentGroup = []

        else:
            currentGroup.append(int(line))

    calories_by_elf = [(index, sum(foodItems)) for index, foodItems in enumerate(groups)]
    max_calories = max(calories_by_elf, key=lambda x: x[1])

    print(max_calories)




def part_two():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    question_input = read_input_as_string(abs_file_path)

    groups = []

    currentGroup = []
    for line in question_input:
        if line == "":
            groups.append(currentGroup)
            currentGroup = []

        else:
            currentGroup.append(int(line))

    calories_by_elf = [(index, sum(foodItems)) for index, foodItems in enumerate(groups)]
    sorted_calories_by_elf = sorted(calories_by_elf, key=lambda x: x[1],reverse=True)
    total_calories_for_top_3_elves = sum(map( lambda x: x[1],sorted_calories_by_elf[:3]))
    print(total_calories_for_top_3_elves)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_two()
