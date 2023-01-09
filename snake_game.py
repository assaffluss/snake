from typing import Optional
from game_display import GameDisplay
from game_utils import *
import math


class SnakeGame:

    def __init__(self, height, width, n_apples, n_walls) -> None:
        self.__x = height // 2
        self.__y = width // 2
        self.__key_clicked = None
        self.snake = [(self.__x - 2, self.__y), (self.__x - 1, self.__y), (self.__x, self.__y)]
        self.apples = []
        self.n_apples = n_apples
        self.walls = []
        self.n_walls = n_walls
        self.direction = None
        self.grow = 0
        self.score = 0

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
        self.snake.append((self.__x, self.__y))
        # keep snake same length if apple wasn't eaten
        self.check_apple()
        if self.grow == 0:
            # check how to keep snake length 3 until first apple eaten
            self.snake.remove(self.snake[0])
        else:
            self.grow -= 1

    def apple_maker(self):
        # if max number of apples were eaten, renew them
        if len(self.apples) < self.n_apples:
            # get random coordinates for the apple
            coordinates = get_random_apple_data()
            # check if coordinates are valid
            is_valid = True
            # check if coordinates clash with existing apple , snake or wall
            if coordinates in self.apples or coordinates in self.snake or coordinates in self.walls:
                is_valid = False
            # add apple to the game
            if is_valid:
                self.apples.append(coordinates)
                pass

    def check_apple(self):
        # check if snake ate the apple
        for apple in self.apples:
            if self.__x == apple[0] and self.__y == apple[1]:
                self.apples.remove(apple)
                self.grow = 3
                # update the score for eating an apple
                self.score += round(math.sqrt(len(self.snake)-1))
                return True
        return False

    def get_score(self):
        return self.score

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

    def out_of_bounds(self, key_clicked):
        # check if snake head goes out of bounds
        if (key_clicked == 'Left') and self.__x - 1 < 0:
            return True
        if (key_clicked == 'Right') and self.__x + 1 == 40:
            return True
        if (key_clicked == 'Up') and self.__y + 1 == 30:
            return True
        if (key_clicked == 'Down') and self.__y - 1 < 0:
            return True

    def is_over(self, bounds) -> bool:
        # if snake head bumps into itself or is out of bounds, game ends
        if bounds is True:
            return True
        for block in self.snake:
            if block == self.snake[len(self.snake) - 2]:
                return False
            if block == (self.__x, self.__y):
                return True
        return False
