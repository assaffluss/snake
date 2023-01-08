from typing import Optional
from game_display import GameDisplay


class SnakeGame:

    def __init__(self) -> None:
        self.__x = 5
        self.__y = 5
        self.__key_clicked = None
        self.cells = [(self.__x-2, self.__y), (self.__x-1, self.__y), (self.__x, self.__y)]
        self.len = 3

    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def update_objects(self)-> None:
        x, y = 0, 0
        if (self.__key_clicked == 'Left') and (self.__x > 0):
            self.__x -= 1
            x = 2
        elif (self.__key_clicked == 'Right') and (self.__x < 40):
            self.__x += 1
            x = 1
        if (self.__key_clicked == 'Up') and (self.__x > 0):
            self.__y += 1
            y = 1
        elif (self.__key_clicked == 'Down') and (self.__x < 30):
            self.__y -= 1
            y = 2
        self.cells.append((self.__x, self.__y))
        # self.move(x, y)

    # def move(self, x, y):
    #     if self.__key_clicked == None:
    #         if x == 2:
    #             self.__x -= 1
    #         if x == 1:
    #             self.__x += 1
    #         if y == 1:
    #             self.__y += 1
    #         if y == 2:
    #             self.__y -= 1
    #     self.cells.append((self.__x, self.__y))
    #     self.cells.remove(self.cells[0])

    def draw_board(self, gd: GameDisplay) -> None:
        # Draw updated position
        for x, y in self.cells:
            gd.draw_cell(x, y, "black")

    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        return False
        def is_over(self) -> bool:
        #if snake head goes out of bounds game ends
        if self.__x >= 40 or self.__x < 0:
            return True
        if self.__y >= 30 or self.__y <=0:
            return True
        #if snake head bumps into itself game ends
        for block in self.cells[0:len(self.cells)-2]:
            if self.__x  == block[0] and self.__y == block[1]:
                return True
        return False
