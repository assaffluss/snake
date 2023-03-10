import argparse
import game_utils
from snake_game import SnakeGame
from game_display import GameDisplay


def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:
    # INIT OBJECTS
    game = SnakeGame(args.height, args.width, args.apples, args.walls)
    gd.show_score(0)
    # DRAW BOARD
    game.apple_maker()
    game.draw_board(gd)
    # END OF ROUND 0
    gd.end_round()
    check_click = None
    check_bounds = False
    change_click = 'Up'
    key_clicked = 'Up'
    while not game.is_over(check_bounds):
        # check which next click is an illegal one
        if key_clicked is not None:
            check_click, change_click = clicked(key_clicked)
        # CHECK KEY CLICKS
        key_clicked = gd.get_key_clicked()
        # check if current click is an illegal one
        if key_clicked == check_click:
            key_clicked = change_click
        # makes sure snake does not go out of bounds
        if game.out_of_bounds(key_clicked):
            check_bounds = True
            continue
        game.read_key(key_clicked)
        # UPDATE OBJECTS
        game.update_objects()
        gd.show_score(game.get_score())
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
