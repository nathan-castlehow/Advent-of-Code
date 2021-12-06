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

    def play(self, move):
        for i in range(0, len(self._board)):
            row = self._board[i]
            for j in range(0, len(row)):
                if row[j] == move:
                    row[j] = None

    def is_complete(self):

        for row in self._board:
            if all(map(lambda x: x is None, row)):
                return True

        for j in range(0, len(self._board[0])):
            col = [self._board[i][j] for i in range(0, len(self._board))]
            if all(map(lambda x: x is None, col)):
                return True

        return False

    def sum_remaining_places(self):
        return sum([sum(filter(None,row)) for row in self._board])
