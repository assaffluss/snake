import argparse
import game_utils
from snake_game import SnakeGame
from game_display import GameDisplay

def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:

    # INIT OBJECTS
    game = SnakeGame()
    gd.show_score(0)
    # DRAW BOARD
    game.draw_board(gd)
    # END OF ROUND 0
    rounds = args.rounds
    while not game.is_over() and rounds != 0:
        # CHECK KEY CLICKS
        try:
            last_click = key_clicked
        except:
            pass
        key_clicked = gd.get_key_clicked()
        game.read_key(key_clicked)
        try:
            check_click = clicked(key_clicked, last_click)
        except:
            pass
        # UPDATE OBJECTS
        game.update_objects()
        # DRAW BOARD
        game.draw_board(gd)
        # WAIT FOR NEXT ROUND:
        game.end_round()
        gd.end_round()


def clicked(key_clicked, last_click):
    if key_clicked == 'Up':
        check_click = 0
    if key_clicked == 'Down':
        check_click = 1
    if key_clicked == 'Left':
        check_click = 2
    if key_clicked == 'Right':
        check_click = 3
    if last_click == 'Up' and check_click == 1 or last_click == 'Down' and check_click == 0:
        return
    if last_click == 'Left' and check_click == 3 or last_click == 'Right' and check_click == 2:
        return
    return check_click


if __name__ == "__main__":
    print("You should run:\n"
          "> python game_display.py")