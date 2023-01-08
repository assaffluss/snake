from typing import Optional
from game_display import GameDisplay


class SnakeGame:

    def __init__(self) -> None:
        self.__x = 5
        self.__y = 5
        self.__key_clicked = None
        self.cells = [(self.__x-2, self.__y), (self.__x-1, self.__y), (self.__x, self.__y)]
        self.len = 3
        self.direction = None

    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def update_objects(self)-> None:
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
        self.cells.append((self.__x, self.__y))
        self.cells.remove(self.cells[0])

    def move(self, direction):
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
        for x, y in self.cells:
            gd.draw_cell(x, y, "black")

    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        #if snake head goes out of bounds game ends
        if self.__x > 40 or self.__x < 0:
            return True
        if self.__y > 30 or self.__y < 0:
            return True
        #if snake head bumps into itself game ends
        # for block in self.cells[0:len(self.cells)-2]:
        #     if self.__x  == block[0] and self.__y == block[1]:
        #         return True
        return False
