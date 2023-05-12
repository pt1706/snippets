from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Программа')
        self.setGeometry(300, 250, 350, 200)

        main_text = QtWidgets.QLabel(self)
        main_text.setText('Текстовая надпись')
        main_text.move(100, 100)
        main_text.adjustSize()

        self.added_text = QtWidgets.QLabel(self)
        self.added_text_pushed = None

        btn = QtWidgets.QPushButton(self)
        btn.setText('Нажми на меня')
        btn.move(70, 150)
        btn.setFixedWidth(150)
        btn.clicked.connect(self.add_text)

    def add_text(self):
        if not self.added_text_pushed:
            self.added_text_pushed = 1
            self.added_text.setText('clicked')
            self.added_text.move(100, 50)
            self.added_text.adjustSize()
        else:
            self.added_text_pushed = None
            self.added_text.setText('')


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
