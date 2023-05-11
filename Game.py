from Field import *

class Game:
    WIDTH = 5
    HEIGHT = 5

    def __init__(self):
        self.field = Field(self.WIDTH, self.HEIGHT)
        self._game_ended = False

    # изменение цветов при нажатии на ЛКМ
    def left_mouse_click(self, i, j):
        for k in range(-1, 2):
            for h in range(-1, 2):
                if k == 0 or h == 0:
                    if 0 <= i + k < self.field.height and 0 <= j + h < self.field.width:
                        self.field.change_cell_color(i + k, j + h)
        self.check_end()

    # функция проверки окончания игры
    def check_end(self):
        win = True
        for i in range(self.WIDTH):
            for j in range(self.HEIGHT):
                if self.get_color_of_cell(i, j) == 'yellow':
                    win = False
                    break
        self._game_ended = win

    def get_color_of_cell(self, i, j):
        return self.field.get_cell_color(i, j)

    @property
    def width(self):
        return self.WIDTH

    @property
    def height(self):
        return self.HEIGHT

    @property
    def game_ended(self):
        return self._game_ended

    def set_field(self, value):
        self.field.set_new_cells(value)