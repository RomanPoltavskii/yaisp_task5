from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QMainWindow


class RulesWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        with open('rules.txt', encoding='UTF-8') as f:
            text = f.read()

        label = QLabel(text, self)
        font = QFont()
        font.setPointSize(16)
        label.setFont(font)

        v_layout = QVBoxLayout(self)
        v_layout.addWidget(label)

        self.setWindowTitle('Правила')