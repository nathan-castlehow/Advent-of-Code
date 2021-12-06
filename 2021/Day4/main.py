import string
import os
from BingoBoard import BingoBoard

BOARD_WIDTH = 5
BOARD_HEIGHT = 5
SPACER_HEIGHT = 1
LINE_COUNT = BOARD_HEIGHT + SPACER_HEIGHT
"""
Example input:
1,17,33,43
\n
92 20 87 77 52
72 29 81 24 64
26 16 19 79 68
 8 53 90 14 74
28 89 78 54 15
\n
13 17 35  2 85
37 87 57 74 65
60 21 18 98 96
 4 51 46 84  0
90 75 80 41 64
"""


def part_one():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")

    with open(abs_file_path) as f:
        moves = [int(move) for move in f.readline().split(",")]
        next(f)  # skip empty line

        remaining_lines = f.readlines()

        # take the five lines at a time to get a list of the lines per board
        # dropping the new line in between each board
        boards_by_line = [remaining_lines[i - LINE_COUNT:i - SPACER_HEIGHT]
                          for i in range(LINE_COUNT, len(remaining_lines), LINE_COUNT)
                          ]
        boards = [BingoBoard(board) for board in boards_by_line]

        is_complete = False
        i = 0

        while not is_complete and i < len(moves):
            current_move = moves[i]
            for board in boards:
                board.play(current_move)
                if board.is_complete():
                    is_complete = True
                    break
            i += 1
        print(board.sum_remaining_places() * current_move)


def part_two():
    abs_file_path = os.path.join(os.path.dirname(__file__), "input")

    with open(abs_file_path) as f:
        moves = [int(move) for move in f.readline().split(",")]
        next(f)  # skip empty line

        remaining_lines = f.readlines()

        # take the five lines at a time to get a list of the lines per board
        # dropping the new line in between each board
        boards_by_line = [remaining_lines[i - LINE_COUNT:i - SPACER_HEIGHT]
                          for i in range(LINE_COUNT, len(remaining_lines), LINE_COUNT)
                          ]
        boards = [BingoBoard(board) for board in boards_by_line]

        i = 0
        completed_boards = []
        while i < len(moves) and any(boards):
            current_move = moves[i]
            for board in boards:
                board.play(current_move)
                if board.is_complete():
                    completed_boards.append(board)
            boards = list(filter(lambda x: not x.is_complete(), boards))
            i += 1

        print(f"Score: {completed_boards.pop().sum_remaining_places() * current_move})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_two()
