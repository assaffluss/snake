import argparse
import game_utils
from snake_game import SnakeGame
from game_display import GameDisplay


def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:
    # INIT OBJECTS
    game = SnakeGame()
    gd.show_score(0)
    # DRAW BOARD
    game.apple_maker()
    game.draw_board(gd)
    # END OF ROUND 0
    gd.end_round()
    check_click = None
    last_click = None
    check_bounds = False
    while not game.is_over(check_bounds):
        # CHECK KEY CLICKS
        key_clicked = gd.get_key_clicked()
        if key_clicked is not None:
            # check if current click is an illegal one
            if key_clicked == check_click:
                continue
            # update last click to current one for next round
            last_click = key_clicked
            check_click = clicked(last_click)
        if game.out_of_bounds(last_click):
            check_bounds = True
            continue
        game.read_key(key_clicked)
        # UPDATE OBJECTS
        game.update_objects()
        # DRAW BOARD
        game.draw_board(gd)
        # WAIT FOR NEXT ROUND:
        game.end_round()
        gd.end_round()


def clicked(last_click):
    # return the value of illegal click for next time
    # user clicks
    if last_click == 'Up':
        return 'Down'
    if last_click == 'Down':
        return 'Up'
    if last_click == 'Left':
        return 'Right'
    if last_click == 'Right':
        return 'Left'
    return None


if __name__ == "__main__":
    print("You should run:\n"
          "> python game_display.py")
