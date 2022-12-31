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


class Square:
    color: str  # white or black
    position: str  # a8

    def __init__(self, position, color):
        self.position = position
        self.color = color

    def __str__(self):
        if self.color == "W":
            return f"{Fore.WHITE}[{self.position}]{Style.RESET_ALL}"
        elif self.color == "B":
            return f"{Style.DIM}[{self.position}{Style.RESET_ALL}]"
        else:
            return 'what are you doing bro'
    def __repr__(self):
        return str(self)


class WhiteSquare(Square):
    color = 'W'


class BlackSquare(Square):
    color = 'B'


class Row:
    squares: list
    num: int

    def __init__(self, num):
        self.num = num

        row_is_odd = self.num % 2

        if row_is_odd:
            colors = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
        else:
            colors = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

        self.squares = []

        column_letters = 'ABCDEFGH'

        for num in range(8):
            self.squares.append(
                Square(
                    position=f'{column_letters[num]}{self.num}',
                    color=colors[num]
                )
            )

    def print_row(self):
        square_strings = [str(item) for item in self.squares]
        squares_string = "".join(square_strings)
        print(squares_string)


def print_board():
    rows = [Row(num) for num in range(1, 9)]
    rows.reverse()
    for row in rows:
        row.print_row()


if __name__ == '__main__':
    print_board()
