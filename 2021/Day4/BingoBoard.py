class BingoBoard:
    _board = []

    def __init__(self, board_by_line):
        self.__deserialize_board(board_by_line)

    """
        Expects a list of strings
        Each string representing a row which needs to be deserialized
    """
    def __deserialize_board(self, board_by_line):
        self._board = [[int(number.strip()) for number in line.split()] for line in board_by_line]
        print(self._board)

    def play(self, move):
        for i in range(0, len(self._board)):
            row = self._board[i]
            for j in range(0, len(row)):
                if row[j] == move:
                    row[j] = None

    def is_complete(self):
        pass

    def sum_remaining_places(self):
        return sum([sum(filter(None,row)) for row in self._board])
