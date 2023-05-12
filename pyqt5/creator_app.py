import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from pyqt5.MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


app = QApplication(sys.argv)
window = MainWindow()
window.resize(300, 900)
window.show()

app.exec_()