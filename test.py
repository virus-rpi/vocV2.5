from PyQt5.QtWidgets import *
from PyQt5 import uic
from threading import Thread
import sys
import time


class UI(QMainWindow):
    def __init__(self, list, t = 120):
        super(UI, self).__init__()
        self.list = list
        self.r = []
        self.t = t

        uic.loadUi("ui/Test.ui", self)

        self.display = self.findChild(QLCDNumber, "lcdNumber")

        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.finish)

        # self.in_1 = self.findChild(QTextEdit, "textEdit_1")
        # self.in_2 = self.findChild(QTextEdit, "textEdit_2")
        # self.in_3 = self.findChild(QTextEdit, "textEdit_3")
        # self.in_4 = self.findChild(QTextEdit, "textEdit_4")
        # self.in_5 = self.findChild(QTextEdit, "textEdit_5")
        # self.in_6 = self.findChild(QTextEdit, "textEdit_6")
        # self.in_7 = self.findChild(QTextEdit, "textEdit_7")
        # self.in_8 = self.findChild(QTextEdit, "textEdit_8")
        # self.in_9 = self.findChild(QTextEdit, "textEdit_9")
        # self.in_10 = self.findChild(QTextEdit, "textEdit_10")
        # self.in_11 = self.findChild(QTextEdit, "textEdit_11")
        # self.in_12 = self.findChild(QTextEdit, "textEdit_12")
        # self.in_13 = self.findChild(QTextEdit, "textEdit_13")
        # self.in_14 = self.findChild(QTextEdit, "textEdit_14")
        # self.in_15 = self.findChild(QTextEdit, "textEdit_15")
        # self.in_16 = self.findChild(QTextEdit, "textEdit_16")
        # self.in_17 = self.findChild(QTextEdit, "textEdit_17")
        # self.in_18 = self.findChild(QTextEdit, "textEdit_18")
        # self.in_19 = self.findChild(QTextEdit, "textEdit_19")
        # self.in_20 = self.findChild(QTextEdit, "textEdit_20")
        # self.in_21 = self.findChild(QTextEdit, "textEdit_21")
        # self.in_22 = self.findChild(QTextEdit, "textEdit_22")
        # self.in_23 = self.findChild(QTextEdit, "textEdit_23")
        # self.in_24 = self.findChild(QTextEdit, "textEdit_24")
        # self.in_25 = self.findChild(QTextEdit, "textEdit_25")
        # self.in_26 = self.findChild(QTextEdit, "textEdit_26")
        # self.in_27 = self.findChild(QTextEdit, "textEdit_27")
        # self.in_28 = self.findChild(QTextEdit, "textEdit_28")
        # self.in_29 = self.findChild(QTextEdit, "textEdit_29")

        for i in range(1, 29):
            exec("self.label_" + str(i) + ' = self.findChild(QLabel, "label_' + str(i) + '")')
            exec("self.in_" + str(i) + "= self.findChild(QTextEdit, 'textEdit_" + str(i) + "')")

        x = 1
        for i in list:
            z = eval("self.label_" + str(x))
            z.setText(i + "  ")
            x += 1

        self.t1 = Thread(target = self.tick)
        self.t1.start()

        self.show()

    def tick(self):
        while True:
            self.display.display(self.t)
            self.display.repaint()
            time.sleep(1)
            self.t -= 1
            if self.t <= 0:
                self.finish()
                return

    def finish(self):
        # print(self.in_1.toPlainText())
        # self.in_1.setPlainText("")
        try:
            for i in range(1, 29):
                self.r.append(eval("self.in_" + str(i) + ".toPlainText()"))
        except:
            self.r = ["fail"]
        print(self.r)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    l = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
         "21", "22", "23", "24", "25", "26", "27", "28", "29"]
    UIWindow = UI(l)
    app.exec_()
