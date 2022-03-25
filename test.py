import sys

from PyQt5.QtWidgets import *
from PyQt5 import *

from main_window_ui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def Test(self):
        dialog = FindTest(self)
        dialog.exec()

    def fill(self, voclist):
        self.label_1 = QLabel("x", self)
        self.label_2 = QLabel("x", self)
        self.label_3 = QLabel("x", self)
        self.label_4 = QLabel("x", self)
        self.label_5 = QLabel("x", self)
        self.label_6 = QLabel("x", self)
        self.label_7 = QLabel("x", self)
        self.label_8 = QLabel("x", self)
        self.label_9 = QLabel("x", self)
        self.label_10 = QLabel("x", self)
        self.label_11 = QLabel("x", self)
        self.label_12 = QLabel("x", self)
        self.label_13 = QLabel("x", self)
        self.label_14 = QLabel("x", self)
        self.label_15 = QLabel("x", self)
        self.label_16 = QLabel("x", self)

        x = 1
        for i in voclist:
            z = eval("self.label_" + str(x))
            z.setText(i)
            x += 1


class FindTest(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/Test.ui", self)


if __name__ == "__main__":
    list = ["test ewgh", "test awogih"]
    app = QApplication(sys.argv)
    win = Window()
    win.fill(list)
    win.show()
    sys.exit(app.exec())
