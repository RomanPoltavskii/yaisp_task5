from PyQt5.QtWidgets import QMessageBox, QWidget, QMainWindow
from Game import *
from PyQt5.QtGui import QPainter, QColor


class GameWindow(QWidget):
    def __init__(self, color_off='gray', color_on='yellow', width=500, height=500):
        super().__init__()

        self._color_off = color_off
        self._color_on = color_on
        self._width = width
        self._height = height

        self._game = Game()

        self.init_ui()

    def init_ui(self):
        self.setFixedWidth(self._width)
        self.setFixedHeight(self._height)
        self.setWindowTitle("Выключить свет!")

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.draw_cells(painter)
        painter.end()

    # событие нажатия на кнопку мыши
    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
        i = int(y / self._height // 0.2)
        j = int(x / self._width // 0.2)
        self._game.left_mouse_click(i, j)
        self.update()
        if self._game.game_ended:
            self.show_win_msg()
            self.close()

    # сообщение о победе
    @staticmethod
    def show_win_msg():
        msg = QMessageBox()
        msg.setWindowTitle("Ура!")
        msg.setText("Поздравляем, вы победили!")
        msg.exec_()

    # отрисовка ячеек
    def draw_cells(self, painter):
        painter.setPen(QColor('green'))

        cell_width = int(self._width / self._game.width)
        cell_height = int(self._height / self._game.height)

        for i in range(self._game.height):
            for j in range(self._game.width):
                if self._game.get_color_of_cell(i, j) == 'yellow':
                    color = self._color_on
                else:
                    color = self._color_off

                painter.fillRect(cell_width * j, cell_height * i, cell_width, cell_height, QColor(color))
                painter.drawRect(cell_width * j, cell_height * i, cell_width, cell_height)

    @property
    def color_off(self):
        return self._color_off

    @color_off.setter
    def color_off(self, value):
        self._color_off = value

    @property
    def color_on(self):
        return self._color_on

    @color_on.setter
    def color_on(self, value):
        self._color_on = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def set_lvl(self, value):
        self._game.set_field(value)