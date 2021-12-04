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

    scrubber_rating = get_scrubber_rating(question_input)
    oxygen_rating = get_oxygen_rating(question_input)
    
    print(f"Life support rating: {oxygen_rating * scrubber_rating}")


def get_oxygen_rating(question_input):
    bit_off = []
    bit_on = []

    current_list = question_input

    for current_bit_pos in range(0, len(question_input[0])):
        if len(current_list) <= 1:
            break

        for line in current_list:
            current_bit = line[current_bit_pos]

            match current_bit:
                case "0":
                    bit_off.append(line)
                case "1":
                    bit_on.append(line)

        current_list = bit_on if len(bit_off) <= len(bit_on) else bit_off
        bit_off = []
        bit_on = []

    return int(current_list.pop(), 2)


def get_scrubber_rating(question_input):
    bit_off = []
    bit_on = []

    current_list = question_input

    for current_bit_pos in range(0, len(question_input[0])):
        if len(current_list) <= 1:
            break

        for i in range(0, len(current_list)):
            line = current_list[i]
            current_bit = line[current_bit_pos]

            match current_bit:
                case "0":
                    bit_off.append(line)
                case "1":
                    bit_on.append(line)

        current_list = bit_off if len(bit_on) >= len(bit_off) else bit_on
        bit_off = []
        bit_on = []

    return int(current_list.pop(), 2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_two()
