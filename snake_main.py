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
    gd.end_round()
    check_click = None
    while not game.is_over():
        # CHECK KEY CLICKS
        key_clicked = gd.get_key_clicked()
        if key_clicked is not None:
            if key_clicked == check_click:
                continue
            last_click = key_clicked
            check_click = clicked(last_click)
        game.read_key(key_clicked)
        # UPDATE OBJECTS
        game.update_objects()
        # DRAW BOARD
        game.draw_board(gd)
        # WAIT FOR NEXT ROUND:
        game.end_round()
        gd.end_round()


def clicked(last_click):
    if last_click == 'Up':
        return 'Down'
    if last_click == 'Down':
        return 'Up'
    if last_click == 'Left':
        return 'Right'
    if last_click == 'Right':
        return 'Left'
    return True


if __name__ == "__main__":
    print("You should run:\n"
          "> python game_display.py")