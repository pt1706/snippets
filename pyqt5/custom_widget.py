from PyQt5 import QtCore, QtGui, QtWidgets
from power_bar import PowerBar

app = QtWidgets.QApplication([])
volume = PowerBar()
volume.resize(200, 400)
volume.show()
app.exec_()