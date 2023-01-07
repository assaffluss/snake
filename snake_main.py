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
            if not check_click:
                continue
        except:
            pass
        # UPDATE OBJECTS
        game.update_objects()
        # DRAW BOARD
        game.draw_board(gd)
        rounds -= 1
        # WAIT FOR NEXT ROUND:
        game.end_round()
        gd.end_round()


def clicked(key_clicked, last_click):
    if last_click == 'Up' and key_clicked == 'Down':
        return False
    if last_click == 'Down' and key_clicked == 'Up':
        return False
    if last_click == 'Left' and key_clicked == 'Right':
        return False
    if last_click == 'Right' and last_click == 'Left':
        return False
    return True


if __name__ == "__main__":
    print("You should run:\n"
          "> python game_display.py")
