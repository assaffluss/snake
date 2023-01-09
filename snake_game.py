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
        if key_clicked:
            self.__key_clicked = key_clicked

    def update_objects(self) -> None:
        self.wall_maker()
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
        
   def wall_maker(self):
        if len(self.walls) < self.n_walls:
            for i in range(self.n_walls):
                wall_coordinates = get_random_wall_data()
                #check if coordinates are valid
                is_valid = True
                # if coordinates clash with apple, snake or existing wall
                if wall_coordinates in self.apples or wall_coordinates in self.snake or wall_coordinates in self.walls:
                    is_valid = False
                # add apple to the game
                if is_valid:
                    self.walls.append(wall_coordinates)
    #fixed wall maker                 
    def wall_maker(self):
    if len(self.walls) < self.n_walls:
        wall_coordinates = get_random_wall_data()
        wall_x = wall_coordinates[0]
        wall_y = wall_coordinates[1]
        direction = wall_coordinates[2]
        wall = []
        for i in range (-1, 2):
            if direction == "Up":
                wall.append((wall_x, wall_y - i))
            if direction == "Down":
                wall.append((wall_x, wall_y + i))
            if direction == "Left":
                wall.append((wall_x - i, wall_y))
            if direction == "Right":
                wall.append((wall_x + i, wall_y))
        is_valid = True
        for coordinate in wall:
            if coordinate in self.apples or coordinate in self.snake or coordinate in self.walls:
                is_valid = False

        if is_valid:
            self.walls.append(wall)
                

    def get_score(self):
        return self.score

    def draw_board(self, gd: GameDisplay) -> None:
        # Draw updated position
        for x, y in self.snake:
            gd.draw_cell(x, y, "black")
        for apple in self.apples:
            gd.draw_cell(apple[0], apple[1], "green")
                for wall in self.walls:
        for x, y in wall:
            gd.draw_cell(x, y , "blue")

    def end_round(self) -> None:
        pass

    def out_of_bounds(self, key_clicked):
        # check if snake head goes out of bounds
        if (self.__key_clicked == 'Left') and self.__x == 0:
            self.snake.remove(self.snake[len(self.snake)-1])
            return True
        if (self.__key_clicked == 'Right') and self.__x == 39:
            self.snake.remove(self.snake[len(self.snake) - 1])
            return True
        if (self.__key_clicked == 'Up') and self.__y == 29:
            self.snake.remove(self.snake[len(self.snake) - 1])
            return True
        if (self.__key_clicked == 'Down') and self.__y == 0:
            self.snake.remove(self.snake[len(self.snake) - 1])
            return True
        return False

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
