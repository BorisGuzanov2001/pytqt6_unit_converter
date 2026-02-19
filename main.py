from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton,
                             QComboBox, QLabel, QLineEdit)

import sys

import json


class NoPositiveValError(Exception):
    def __init__(self):
        super().__init__()

class MyCustomError(Exception):
    def __init__(self):
        super().__init__()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
          with open('units.json', encoding='utf-8') as file:
              self.data = json.load(file)
              # print(self.data)
              self.combo = QComboBox(self)
              self.combo2 = QComboBox(self)
              self.combo3 = QComboBox(self)
              self.qle1 = QLineEdit(self)
              self.qle2 = QLineEdit(self)
              self.qlb1 = QLabel(self)
              self.qlb2 = QLabel(self)
              self.qlb3 = QLabel(self)
              self.qlb4 = QLabel(self)
              self.button = QPushButton("Конвертировать", self)
              for key in self.data.keys():
                self.combo.addItem(key)
              self.combo.setGeometry(50, 50, 150, 50)
              self.combo2.setGeometry(50, 100, 150, 50)
              self.combo3.setGeometry(50, 150, 150, 50)
              self.combo2.hide()
              self.combo3.hide()
              self.qle1.setGeometry(200, 100, 400, 50)
              self.button.setGeometry(50, 200, 150, 50)
              self.qle2.setGeometry(200, 200, 400, 50)
              self.qle2.setText("Здесь будет выводиться результат!")
              self.qlb1.setGeometry(200, 50, 400, 50)
              self.qlb1.setText("Поле для ввода:")
              self.qlb2.setGeometry(200, 150, 400, 50)
              self.qlb2.setText("Поле с результатом:")
              self.qlb3.setText("Из:")
              self.qlb4.setText("В:")
              self.qlb3.setGeometry(25, 100, 25, 50)
              self.qlb4.setGeometry(25, 150, 25, 50)
              self.combo.textActivated[str].connect(self.onActivated)
              self.button.setCheckable(True)
              self.button.clicked.connect(self.the_mouse_was_clicked)
              self.button.released.connect(self.the_mouse_was_released)
              self.setGeometry(300, 300, 450, 400)
              self.setWindowTitle('Конвертер единиц измерения для уроков математики')
              self.show()

    def onActivated(self, text):
        self.combo2.clear()
        self.combo3.clear()
        for key in self.data[text].keys():
            self.combo2.addItem(key)
            self.combo3.addItem(key)
        self.combo2.show()
        self.combo3.show()
        # print(self.data[text].keys())


    def the_mouse_was_clicked(self):
        print("Click Mouse!")
        if self.qle1.text() == "":
            # print("Поле пустое. Введите число!")
            self.qle1.setText("Поле пустое. Введите число!")
        try:
            input_value = int(self.qle1.text())
            if self.combo2.currentText() == self.combo3.currentText():
                raise MyCustomError
            elif input_value < 0:
                raise NoPositiveValError
            output_value = round(self.data[self.combo.currentText()][self.combo2.currentText()] * input_value / self.data[self.combo.currentText()][self.combo3.currentText()], 2)
            self.qle2.setText(str(output_value))
            print(f"output_value = {output_value}")
        except ValueError:
            # print("Ошибка конвертации строки в число!")
            self.qle1.setText("Ошибка конвертации строки в число!")
        except MyCustomError:
            # print("Исходная и целевая единицы должны быть разными")
            self.qle1.setText("Исходная и целевая единицы должны быть разными")
        except NoPositiveValError:
            self.qle1.setText("Разрешены только положительные числа")

    def the_mouse_was_released(self):
        # print("Released Mouse")
        self.button.setStyleSheet("background-color: #262626;")

app = QApplication(sys.argv)


# # создаём виджет окно
window = Example()
window.show() # окно по умолчанию скрыто

# запускаем цикл событий
app.exec()
