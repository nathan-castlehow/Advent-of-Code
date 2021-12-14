import os
from read_input import read_input_as_string

STEPS = 5


def part_one():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input_sample")
    input_data = read_input_as_string(abs_file_path)

    base_string = input_data[0]
    insertion_rules = []

    # skip empty line between base string and instructions
    for i in range(2, len(input_data)):
        insertion_rule_split = input_data[i].split(" -> ")
        insertion_rules.append(
            InsertionRule((insertion_rule_split[0][0], insertion_rule_split[0][1]), insertion_rule_split[1]))

    pair_wise_count = {}

    for i in range(1, len(base_string)):
        pair = (base_string[i - 1], base_string[i])
        pair_wise_count[pair] = pair_wise_count.get(pair, 0) + 1

    for i in range(STEPS):
        tmp_pair_wise_count = {}
        for rule in insertion_rules:
            tmp_pair_wise_count[rule.startPair] = tmp_pair_wise_count.get(rule.startPair, 0) + pair_wise_count.get(
                rule.pair, 0)
            tmp_pair_wise_count[rule.endPair] = tmp_pair_wise_count.get(rule.endPair, 0) + pair_wise_count.get(
                rule.pair, 0)
            # tmp_pair_wise_count[rule.pair] = 0

        for key in pair_wise_count.keys():
            if key not in tmp_pair_wise_count.keys():
                tmp_pair_wise_count[key] = pair_wise_count[key]

        pair_wise_count = tmp_pair_wise_count
        print(tmp_pair_wise_count)
    print(pair_wise_count)

    element_count = {}
    for pair in pair_wise_count.keys():
        element_count[pair[0]] = element_count.get(pair[0], 0) + pair_wise_count[pair]
        element_count[pair[1]] = element_count.get(pair[1], 0) + pair_wise_count[pair]


    # counts = list(element_count.values())
    # print(element_count)
    # print(element_count.values())
    min_value = min(element_count.values())
    max_value = max(element_count.values())

    total = max_value - min_value

    print(f"Total: {total}")
    # for i in range(STEPS):


class InsertionRule:
    def __init__(self, pair, element):
        self.pair = pair
        self.startPair = (pair[0], element)
        self.endPair = (element, pair[1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_one()
