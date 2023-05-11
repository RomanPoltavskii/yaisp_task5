
from GameWindow import *
from LevelWindow import *
from SettingsWindow import *
from RulesWindow import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.game_window = GameWindow()
        self.level_window = LevelWindow()
        self.settings_window = SettingsWindow()
        self.rules_window = RulesWindow()

        self.color_off = "gary"
        self.color_on = "yellow"
        self.width = "500"
        self.height = "500"

        self.init_ui()

    def init_ui(self):
        name_label = QLabel('Выключить Свет!', self)
        font = QFont()
        font.setPointSize(14)
        name_label.setFont(font)
        name_label.setMaximumWidth(700)
        name_label.setMaximumHeight(200)

        # кнопки

        play_button = QPushButton('Играть', self)
        play_button.setFixedWidth(400)
        play_button.setFixedHeight(30)
        play_button.clicked.connect(self.play_clicked)

        level_button = QPushButton('Выбрать уровень', self)
        level_button.setFixedWidth(400)
        level_button.setFixedHeight(30)
        level_button.clicked.connect(self.level_clicked)

        settings_button = QPushButton('Настройки', self)
        settings_button.setFixedWidth(400)
        settings_button.setFixedHeight(30)
        settings_button.clicked.connect(self.settings_clicked)

        rules_button = QPushButton('Правила', self)
        rules_button.setFixedWidth(400)
        rules_button.setFixedHeight(30)
        rules_button.clicked.connect(self.rules_clicked)

        layout = QVBoxLayout()
        layout.addWidget(name_label)
        layout.addWidget(play_button)
        layout.addWidget(level_button)
        layout.addWidget(settings_button)
        layout.addWidget(rules_button)
        self.setLayout(layout)

        self.setWindowTitle('Выключить свет!')

    # проверка на нажатие кнопки "играть"
    def play_clicked(self):
        tpl = self.settings_window.get_info()
        if tpl is not None:
            if tpl[0] != "":
                self.game_window.color_off = tpl[0]
            if tpl[1] != "":
                self.game_window.color_on = tpl[1]
            if tpl[2] != "":
                self.game_window.width = int(tpl[2])
            if tpl[3] != "":
                self.game_window.height = int(tpl[3])

        lvl = self.level_window.get_level()
        if lvl is None:
            self.show_no_lvl_err_msg()
        else:
            self.game_window.set_lvl(lvl)
            self.game_window.init_ui()
            self.game_window.show()

    # сообщение об ошибке, если уровень не выбран
    @staticmethod
    def show_no_lvl_err_msg():
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText("Выберите уровень!")
        msg.exec_()

    # проверка на нажатие кнопки "выбрать уровень"
    def level_clicked(self):
        self.level_window.show()

    # проверка на нажатие кнопки "настройки"
    def settings_clicked(self):
        self.settings_window.show()

    # проверка на нажатие кнопки "правила"
    def rules_clicked(self):
        self.rules_window.show()