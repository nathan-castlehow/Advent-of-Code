import os
from read_input import read_input_as_string

STEPS = 40

step_4_value = "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"


def break_down_string():
    pair_wise_count = {}
    base_string = step_4_value
    for i in range(1, len(base_string)):
        pair = (base_string[i - 1], base_string[i])
        pair_wise_count[pair] = pair_wise_count.get(pair, 0) + 1
    print(pair_wise_count)


# {('N', 'B'): 9, ('B', 'B'): 9, ('B', 'N'): 6, ('B', 'C'): 4, ('C', 'C'): 2, ('C', 'N'): 3, ('N', 'C'): 1, ('C', 'B'): 5, ('B', 'H'): 3, ('H', 'C'): 3, ('H', 'H'): 1, ('H', 'N'): 1, ('N', 'H'): 1}
# {('C', 'B'): 5, ('B', 'H'): 3, ('H', 'N'): 1, ('N', 'H'): 1, ('C', 'H'): 0, ('H', 'B'): 0, ('N', 'C'): 1, ('H', 'C'): 3, ('B', 'C'): 4, ('C', 'N'): 3, ('H', 'H'): 1, ('N', 'B'): 9, ('B', 'B'): 9, ('B', 'N'): 6, ('C', 'C'): 2, ('N', 'N'): 0}


def part_one():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    input_data = read_input_as_string(abs_file_path)

    base_string = input_data[0]
    insertion_rules = []

    # skip empty line between base string and instructions
    for i in range(2, len(input_data)):
        insertion_rule_split = input_data[i].split(" -> ")
        insertion_rules.append(
            InsertionRule((insertion_rule_split[0][0], insertion_rule_split[0][1]), insertion_rule_split[1]))

    pair_wise_count = {}
    letter_count = {}
    for i in range(1, len(base_string)):
        pair = (base_string[i - 1], base_string[i])
        pair_wise_count[pair] = pair_wise_count.get(pair, 0) + 1

    for letter in base_string:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    print(letter_count)
    for i in range(STEPS):
        tmp_pair_wise_count = {}
        for rule in insertion_rules:
            tmp_pair_wise_count[rule.startPair] = tmp_pair_wise_count.get(rule.startPair, 0) + pair_wise_count.get(
                rule.pair, 0)
            tmp_pair_wise_count[rule.endPair] = tmp_pair_wise_count.get(rule.endPair, 0) + pair_wise_count.get(
                rule.pair, 0)
            letter_count[rule.element] = letter_count.get(rule.element, 0) + (pair_wise_count.get(rule.pair, 0))
            pair_wise_count[rule.pair] = 0
            print(rule.pair, rule.element, rule.startPair, rule.endPair, pair_wise_count.get(rule.pair, 0))

        for key in pair_wise_count.keys():
            if key not in tmp_pair_wise_count.keys():
                tmp_pair_wise_count[key] = pair_wise_count[key]
        pair_wise_count = tmp_pair_wise_count
        print(pair_wise_count)
        print("-----------------------------")

    print(letter_count)
    # element_count = {}
    # for pair in pair_wise_count.keys():
    #     element_count[pair[0]] = element_count.get(pair[0], 0) + pair_wise_count[pair]
    #     element_count[pair[1]] = element_count.get(pair[1], 0) + pair_wise_count[pair]
    #
    # print(element_count)
    # counts = list(element_count.values())
    # print(element_count)
    # print(element_count.values())
    min_value = min(letter_count.values())
    max_value = max(letter_count.values())

    total = max_value - min_value

    print(f"Total: {total}")


class InsertionRule:
    def __init__(self, pair, element):
        self.pair = pair
        self.startPair = (pair[0], element)
        self.endPair = (element, pair[1])
        self.element = element


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_one()
