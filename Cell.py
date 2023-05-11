class Cell:

    def __init__(self, color):
        self._color = color

    def change_color(self):
        if self._color == "yellow":
            self._color = "gray"
        else:
            self._color = "yellow"

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value