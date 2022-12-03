from read_input import read_input_as_int, read_input_as_string
import os


def part_one():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    question_input = read_input_as_string(abs_file_path)
    user_to_base_move_dict = {
        "Y": "B",
        "X": "A",
        "Z": "C",
    }
    user_reward_lookup = {
        "A": 1,  # Rock
        "B": 2,  # Paper
        "C": 3  # Scissors
    }

    win_loss_lookup = {
        ("A", "A"): 3,
        ("B", "B"): 3,
        ("C", "C"): 3,

        ("A", "B"): 6,
        ("A", "C"): 0,
        ("B", "A"): 0,
        ("B", "C"): 6,
        ("C", "A"): 6,
        ("C", "B"): 0,
    }

    normalized_input = [(line.split()[0], user_to_base_move_dict[line.split()[1]]) for line in question_input]
    round_values = [user_reward_lookup[pair[1]] + win_loss_lookup[pair] for pair in normalized_input]

    total_score = sum(round_values)
    print(total_score)


def part_two():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    question_input = read_input_as_string(abs_file_path)

    game_to_user_move_dict = {
        ("A", "X"): "C",
        ("A", "Y"): "A",
        ("A", "Z"): "B",
        ("B", "X"): "A",
        ("B", "Y"): "B",
        ("B", "Z"): "C",
        ("C", "X"): "B",
        ("C", "Y"): "C",
        ("C", "Z"): "A",
    }
    user_reward_lookup = {
        "A": 1,  # Rock
        "B": 2,  # Paper
        "C": 3  # Scissors
    }

    win_loss_lookup = {
        ("A", "A"): 3,
        ("B", "B"): 3,
        ("C", "C"): 3,

        ("A", "B"): 6,
        ("A", "C"): 0,
        ("B", "A"): 0,
        ("B", "C"): 6,
        ("C", "A"): 6,
        ("C", "B"): 0,
    }

    normalized_input = [(line.split()[0], game_to_user_move_dict[(line.split()[0], line.split()[1])]) for line in
                        question_input]
    round_values = [user_reward_lookup[pair[1]] + win_loss_lookup[pair] for pair in normalized_input]

    total_score = sum(round_values)
    print(total_score)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_two()
