import os
from read_input import read_input_as_string


def part_one():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    input_data = read_input_as_string(abs_file_path)

    chunk_pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    chunk_points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    illegal_characters = []
    for line in input_data:
        open_chunks = []
        for i in range(0, len(line)):
            current_char = line[i]
            if current_char in chunk_pairs.keys():
                open_chunks.append(current_char)
            else:
                current_open = open_chunks.pop()
                if chunk_pairs[current_open] != current_char:
                    illegal_characters.append(current_char)
                    break

    total = 0
    for char in illegal_characters:
        total += chunk_points[char]

    print(f"Total: {total}")


def part_two():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")
    input_data = read_input_as_string(abs_file_path)

    chunk_pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    chunk_points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    valid_lines = []
    for line in input_data:
        open_chunks = []
        is_valid_line = True

        for i in range(0, len(line)):
            current_char = line[i]
            if current_char in chunk_pairs.keys():
                open_chunks.append(current_char)
            else:
                current_open = open_chunks.pop()
                if chunk_pairs[current_open] != current_char:
                    is_valid_line = False
                    break

        if is_valid_line:
            valid_lines.append(line)

    corrected_lines = []
    for line in valid_lines:
        new_line = ""
        open_chunks = []
        for i in range(0, len(line)):
            current_char = line[i]
            if current_char in chunk_pairs.keys():
                open_chunks.append(current_char)
            else:
                open_chunks.pop()
        for char in reversed(open_chunks):
            new_line = new_line + chunk_pairs[char]
        corrected_lines.append(new_line)

    totals = []
    for line in corrected_lines:
        total = 0
        for char in line:
            total = (total * 5) + chunk_points[char]
        totals.append(total)

    print(totals)
    sorted_totals = list(sorted(totals))
    score_index = int(len(sorted_totals) / 2)

    print(f"Total {sorted_totals[score_index]}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_one()
