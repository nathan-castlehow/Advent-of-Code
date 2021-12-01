from read_input import read_input_as_int
import os


def part_one():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    question_input = read_input_as_int(abs_file_path)

    total = 0
    for i in range(1, len(question_input)):
        if question_input[i] > question_input[i - 1]:
            total += 1

    print(total)


def part_two():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    question_input = read_input_as_int(abs_file_path)

    total = 0

    for i in range(2, len(question_input) - 1, 1):

        prev_sum = question_input[i] + question_input[i - 1] + question_input[i - 2]
        cur_sum = question_input[i - 1] + question_input[i] + question_input[i + 1]

        if cur_sum > prev_sum:
            total += 1

    print(total)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_one()
