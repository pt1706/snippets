from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QAction, QStatusBar, QCheckBox, QDesktopWidget, \
    QVBoxLayout, QComboBox, QDateEdit, QDateTimeEdit, QDial, QDoubleSpinBox, QFontComboBox, QLCDNumber, QLineEdit, \
    QProgressBar, QPushButton, QRadioButton, QSlider, QSpinBox, QTimeEdit, QWidget, QListWidget
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QKeySequence, QPixmap

import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('My Awesome App')

        # label = QLabel("THIS IS AWESOME!!!")
        # label.setAlignment(Qt.AlignCenter)
        #
        # self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("img/bug.png"), "Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)
        button_action.setCheckable(True)
        button_action.setShortcut(QKeySequence("Ctrl+p"))

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("img/fruit.png"), "Your button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addSeparator()

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)
        self.setCentralWidget(widget)

    def onMyToolBarButtonClick(self, s):
        print('click', s)

    def contextMenuEvent(self, event):
        print("Context menu event!")
        super().contextMenuEvent(event)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.resize(400, 300)
window.show()

app.exec_()