"""
Make a chess game

"""
from objects import board
from objects import game

"""
Steps:
1. Make a board
2. Make pieces
3. Place pieces on a board
4. Play game


"""
my_board = board.Board()
def main():
    my_board.print_rows()
    move = game.get_move_from_user()
    game.process_move(move)


if __name__ == '__main__':
    main()

chat = [
    "Russ: i dont think i have a mic setup for this hold up",
    "Wade: lol your discord status is prolly playin chess, nice"
    "Russ: where is microphone settings lol"
    "Russ: if you didnt know, you have weird static"
    "Wade: My headset is acting up "
    "Russ: Very cool :) "
]
