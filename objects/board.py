"""
Board:
* 8 rows of squares
* 8 columns of squares
"""
from objects.pieces import SYMBOLS
from colorama import init as colorama_init
from colorama import Fore, Style

"""
Square
* Color
* Position
"""
colorama_init()
"""
SYMBOLS = {
    'Rook': 'R',
    'Knight': 'N',
    'King': 'K',
    'Queen': 'Q',
    'Pawn': 'P',
    'Bishop': 'B',
}
"""


PIECE_NOTATION = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']


class Square:
    color: str  # white or black
    position: str  # a8
    piece: str

    def __init__(self, position, color, piece=None):
        self.position = position
        self.color = color
        self.piece = piece

    def __str__(self):
        if self.piece:
            contents = self.piece
        else:
            contents = ' '

        if self.color == "W":
            return f"{Fore.WHITE}[{contents}]{Style.RESET_ALL}"
        elif self.color == "B":
            return f"{Style.DIM}[{contents}]{Style.RESET_ALL}"
        else:
            return 'what are you doing bro'

    def __repr__(self):
        return str(self)


class WhiteSquare(Square):
    color = 'W'


class BlackSquare(Square):
    color = 'B'


class Row:
    def __init__(self, row_number):
        self.rownum = row_number
        self.setup_squares()

    def setup_squares(self):
        row_is_odd = self.rownum % 2

        if row_is_odd:
            colors = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
        else:
            colors = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

        self.squares = []

        column_letters = 'ABCDEFGH'

        for column_num in range(8):
            if self.rownum in [1, 8]:
                piece = PIECE_NOTATION[column_num]
            elif self.rownum in [2, 7]:
                piece = 'P'
            else:
                piece = None

            self.squares.append(
                Square(
                    position=f'{column_letters[column_num]}{self.rownum}',
                    color=colors[column_num],
                    piece=piece
                )
            )

    def print_row(self):
        square_strings = [str(item) for item in self.squares]
        squares_string = "".join(square_strings)
        print(self.rownum, squares_string)

    def __repr__(self):
        return f"Row {self.rownum}"


class Board:
    def __init__(self):
        self.setup_rows()

    def setup_rows(self):
        self.rows = []
        for row_number in range(1, 9):
            self.rows.append(Row(row_number))

        self.rows.reverse()

    def print_rows(self):
        for row in self.rows:
            row.print_row()
        print('   A  B  C  D  E  F  G  H')


def print_board():
    my_board = Board()
    my_board.print_rows()


