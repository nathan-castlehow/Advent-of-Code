import string

from read_input import read_input_as_string
import os


def part_one():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    question_input = read_input_as_string(abs_file_path)

    bit_positions_on = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bit_positions_off = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0, len(question_input)):
        line = question_input[i]
        for j in range(0, len(question_input[i])):
            char = line[j]
            if char == "1":
                bit_positions_on[j] += 1
            else:
                bit_positions_off[j] += 1

    gamma_str = "".join(["0" if tup[0] > tup[1] else "1" for tup in zip(bit_positions_on, bit_positions_off)])
    alpha_str = "".join(["1" if tup[0] > tup[1] else "0" for tup in zip(bit_positions_on, bit_positions_off)])

    print(f"gamma: {gamma_str}")
    print(f"alpha: {alpha_str}")
    print(f"Total: {int(gamma_str, 2) * int(alpha_str, 2)}")


def part_two():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    question_input = read_input_as_string(abs_file_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_one()
