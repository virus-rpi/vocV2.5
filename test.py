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

    def fill(self, list):
        self.lable1 = QLable(one, self)
        self.lable2 = QLable(zwo, self)

        x = 1
        for i in list:
            z = eval("lable" + x)
            z = i
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
