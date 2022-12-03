import string

from read_input import read_input_as_int, read_input_as_string
import os


def part_one():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    question_input = read_input_as_string(abs_file_path)

    repeated_letters = []
    for line in question_input:
        half_way_value = int(len(line) / 2)
        r1_items = line[:half_way_value]
        r2_items = line[half_way_value:]

        current_letters = set()
        for letter in r1_items:
            current_letters.add(letter)

        repeated_set = set()
        for letter in r2_items:
            if letter in current_letters:
                repeated_set.add(letter)
        for distinctLetter in repeated_set:
            repeated_letters.append(distinctLetter)

    ascii_letters = string.ascii_letters

    priorities = map(lambda x: (ascii_letters.index(x) + 1), repeated_letters)

    print(sum(priorities))


def part_two():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    question_input = read_input_as_string(abs_file_path)

    repeated_letters = []
    for i in range(0, len(question_input), 3):
        bag_1 = set(question_input[i])
        bag_2 = set(question_input[i + 1])
        bag_3 = set(question_input[i + 2])

        common_letters = bag_1.intersection(bag_2).intersection(bag_3)
        for letter in common_letters:
            repeated_letters.append(letter)

    ascii_letters = string.ascii_letters

    priorities = map(lambda x: (ascii_letters.index(x) + 1), repeated_letters)

    print(sum(priorities))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_two()
