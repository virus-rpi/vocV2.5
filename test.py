import sys

from PyQt5.QtWidgets import *

from main_window_ui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def Test(self):
        dialog = FindTest(self)
        dialog.exec()

    def fill(self, list):
        x = 1
        for i in list:
            z = eval("self.label_" + str(x))
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
