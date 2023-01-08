from typing import Optional
from game_display import GameDisplay
from game_utils import *


class SnakeGame:

    def __init__(self) -> None:
        # check how to get HEIGHT and WIDTH
        self.__x = 5
        self.__y = 5
        self.__key_clicked = None
        self.snake = [(self.__x - 2, self.__y), (self.__x - 1, self.__y), (self.__x, self.__y)]
        self.apples = []
        self.n_apples = 3
        self.walls = []
        self.direction = None

    def read_key(self, key_clicked: Optional[str]) -> None:
        self.__key_clicked = key_clicked

    def update_objects(self) -> None:
        if (self.__key_clicked == 'Left') and (self.__x > 0):
            self.__x -= 1
            self.direction = 'l'
        elif (self.__key_clicked == 'Right') and (self.__x < 40):
            self.__x += 1
            self.direction = 'r'
        if (self.__key_clicked == 'Up') and (self.__y > 0):
            self.__y += 1
            self.direction = 'u'
        elif (self.__key_clicked == 'Down') and (self.__y < 30):
            self.__y -= 1
            self.direction = 'd'
        if self.__key_clicked is None:
            self.move(self.direction)
        self.apple_maker()
        # move snake to direction chosen by user
        self.snake.append((self.__x, self.__y))
        # keep snake same length if apple wasn't eaten
        if not self.check_apple():
            self.snake.remove(self.snake[0])

    def apple_maker(self):
        if len(self.apples) < 1:  # if max number of apples were eaten, renew them
            # get random coordinates for the apple
            for i in range(self.n_apples):
                coordinates = get_random_apple_data()
                # check if coordinates are valid
                is_valid = True
                # if coordinates clash with existing apple , snake or wall
                if coordinates in self.apples or coordinates in self.snake or coordinates in self.walls:
                    is_valid = False
                # add apple to the game
                if is_valid:
                    self.apples.append(coordinates)

    def check_apple(self):
        # check if snake ate the apple
        for apple in self.apples:
            if self.__x == apple[0] and self.__y == apple[1]:
                self.apples.remove(apple)
                return True
        return False

    def move(self, direction):
        # check last pressed direction and keep moving that way
        if direction == 'l':
            self.__x -= 1
        if direction == 'r':
            self.__x += 1
        if direction == 'u':
            self.__y += 1
        if direction == 'd':
            self.__y -= 1

    def draw_board(self, gd: GameDisplay) -> None:
        # Draw updated position
        for x, y in self.snake:
            gd.draw_cell(x, y, "black")
        for apple in self.apples:
            gd.draw_cell(apple[0], apple[1], "green")

    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        # if snake head goes out of bounds game ends
        # check why bounds return an error and why
        # <= 0 doesn't let us reach the last line of board
        if self.__x >= 40 or self.__x < 0:
            self.snake.remove((self.__x, self.__y))
            return True
        if self.__y >= 30 or self.__y < 0:
            self.snake.remove((self.__x, self.__y))
            return True
        # if snake head bumps into itself game ends
        for block in self.snake:
            if block == self.snake[len(self.snake)-2]:
                return False
            if block == (self.__x, self.__y):
                return True
        return False

