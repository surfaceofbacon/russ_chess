"""
Game
* 2 Players
* 1 Board
* 32 Pieces
* Start
* Turns
* Check/Checkmate
* End
"""

from objects import board
import main

def get_move_from_user():
    while True:
        move = input('Enter Move: ')
        if len(move) != 3 and len(move) != 5:
            print('length is not 3 or 5')
            continue
        if move[0] == '0':
            if move == '0-0':
                print('kingside castle')
                break
            elif move == '0-0-0':
                print('queenside castle')
                break

        piece = move[0].upper()
        column = move[1].upper()
        try:
            row = int(move[2])
        except ValueError:
            print('invalid row')
            continue
        if piece not in board.PIECE_NOTATION:
            print('input doesnt work bro (piece not in piece notation)')
            continue
        if not check_column_and_row(column, row):
            continue
        if len(move) == 5:
            second_column = move[3].upper()
            second_row = int(move[4])
            if not check_column_and_row(second_column, second_row):
                continue
        return move

def process_move(move: str):
    columns = 'ABCDEFGH'
    piece = move[0]
    column_one = columns.index(move[1].upper())
    row_one = abs(8 - int(move[2]))
    column_two = columns.index(move[3].upper())
    row_two = abs(8 - int(move[4]))
    main.my_board.rows[row_one].squares[column_one] = '[ ]'
    main.my_board.rows[row_two].squares[column_two] = f'[{piece.upper()}]'
    main.my_board.print_rows()




def check_column_and_row(column: str, row: int) -> bool:
    if column not in 'ABCDEFGH':
        print('input doesnt work bro (column doesnt work)')
        return False
    if row not in range(1, 9):
        print('input doesnt work bro (row doesnt work)')
        return False
    return True




