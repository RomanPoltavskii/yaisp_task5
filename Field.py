from Cell import *

class Field:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.cells = []

        for i in range(height):
            self.cells.append([])
            for j in range(width):
                self.cells[i].append(Cell("yellow"))

    def set_new_cells(self, new_cells):
        if len(new_cells) != self.height:
            raise Exception("Неверный формат массива")

        for arr in new_cells:
            if len(arr) != self.width:
                raise Exception("Неверный формат массива")

        for i in range(len(new_cells)):
            for j in range(len(new_cells[0])):
                x = new_cells[i][j]
                if x == 1:
                    self.cells[i][j].color = 'yellow'
                else:
                    self.cells[i][j].color = 'gray'

    def change_cell_color(self, i, j):
        self.cells[i][j].change_color()

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def get_cell_color(self, i, j):
        return self.cells[i][j].color
