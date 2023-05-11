from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QMainWindow


class LevelWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lvl = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        lvl_1_button = QPushButton("Уровень 1")
        lvl_1_button.clicked.connect(self.lvl_1_clicked)
        layout.addWidget(lvl_1_button)

        lvl_2_button = QPushButton("Уровень 2")
        lvl_2_button.clicked.connect(self.lvl_2_clicked)
        layout.addWidget(lvl_2_button)

        lvl_3_button = QPushButton("Уровень 3")
        lvl_3_button.clicked.connect(self.lvl_3_clicked)
        layout.addWidget(lvl_3_button)

        lvl_4_button = QPushButton("Уровень 4")
        lvl_4_button.clicked.connect(self.lvl_4_clicked)
        layout.addWidget(lvl_4_button)

        lvl_5_button = QPushButton("Уровень 5")
        lvl_5_button.clicked.connect(self.lvl_5_clicked)
        layout.addWidget(lvl_5_button)

        self.setLayout(layout)

        self.setGeometry(750, 450, 200, 150)
        self.setWindowTitle("Уровни")

    def lvl_1_clicked(self):
        with open('levels/level_01.txt', 'r') as f:
            temp = f.readlines()

        self.lvl = [[int(x) for x in line.split()] for line in temp]
        self.close()

    def lvl_2_clicked(self):
        with open('levels/level_02.txt', 'r') as f:
            temp = f.readlines()

        self.lvl = [[int(x) for x in line.split()] for line in temp]
        self.close()

    def lvl_3_clicked(self):
        with open('levels/level_03.txt', 'r') as f:
            temp = f.readlines()

        self.lvl = [[int(x) for x in line.split()] for line in temp]
        self.close()

    def lvl_4_clicked(self):
        with open('levels/level_04.txt', 'r') as f:
            temp = f.readlines()

        self.lvl = [[int(x) for x in line.split()] for line in temp]
        self.close()

    def lvl_5_clicked(self):
        with open('levels/level_05.txt', 'r') as f:
            temp = f.readlines()

        self.lvl = [[int(x) for x in line.split()] for line in temp]
        self.close()

    def get_level(self):
        return self.lvl