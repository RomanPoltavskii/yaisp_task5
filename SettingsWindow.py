from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QMainWindow


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.input_color_off = QLineEdit(self)
        self.input_color_on = QLineEdit(self)
        self.input_width = QLineEdit(self)
        self.input_height = QLineEdit(self)

        self.color_off = ""
        self.color_on = ""
        self.width = ""
        self.height = ""
        self.button_pressed = False
        self.init_ui()

    def init_ui(self):
        self.setFixedWidth(400)
        self.setFixedHeight(200)
        self.setWindowTitle("Настройки")

        horizontal_layout = QHBoxLayout(self)
        horizontal_layout.setContentsMargins(5, 5, 5, 5)
        horizontal_layout.setSpacing(10)

        vertical_layout = QVBoxLayout()
        vertical_layout.setSpacing(10)

        label_color_off = QLabel("Цвет \"выкл.\"", self)
        label_color_on = QLabel("Цвет \"вкл.\"", self)
        label_width = QLabel("Ширина", self)
        label_height = QLabel("Высота", self)

        vertical_layout.addWidget(label_color_off)
        vertical_layout.addWidget(label_color_on)
        vertical_layout.addWidget(label_width)
        vertical_layout.addWidget(label_height)
        vertical_layout.addWidget(QLabel(""))
        horizontal_layout.addLayout(vertical_layout)

        vertical_layout_2 = QVBoxLayout(self)

        self.input_color_off.setText(self.color_off)
        self.input_color_on.setText(self.color_on)
        self.input_width.setText(self.width)
        self.input_height.setText(self.height)

        vertical_layout_2.addWidget(self.input_color_off)
        vertical_layout_2.addWidget(self.input_color_on)
        vertical_layout_2.addWidget(self.input_width)
        vertical_layout_2.addWidget(self.input_height)

        save_button = QPushButton('Сохранить', self)
        save_button.setGeometry(160, 260, 75, 23)
        save_button.clicked.connect(self.save_button_clicked)

        vertical_layout_2.addWidget(save_button)
        horizontal_layout.addLayout(vertical_layout_2)

    def save_button_clicked(self):
        self.color_off = self.input_color_off.text()
        self.color_on = self.input_color_on.text()
        self.width = self.input_width.text()
        self.height = self.input_height.text()
        self.button_pressed = True
        self.close()

    def get_info(self):
        if self.button_pressed:
            tpl = (self.color_off, self.color_on, self.width, self.height)
            self.button_pressed = False
            return tpl
        else:
            return None