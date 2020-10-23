from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Application")

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World!")
        self.label.move(50, 250)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("Click Me")
        self.btn.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You clicked the button")
        self.update()

    def update(self):
        self.label.adjustSize()

def clicked():
    print('Clicked')


def window():
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec_())


window()
