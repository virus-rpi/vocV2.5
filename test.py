from PyQt5.QtWidgets import *
from PyQt5 import uic
from threading import Thread
import sys
import time


class UI(QMainWindow):
    def __init__(self, voclist, t=120):
        super(UI, self).__init__()
        self.voclist = voclist
        self.r = []
        self.t = t

        uic.loadUi("ui/Test.ui", self)

        self.disp = self.findChild(QLCDNumber, "lcdNumber")

        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.finish)

        for i in range(1, 29):
            exec("self.label_" + str(i) + ' = self.findChild(QLabel, "label_' + str(i) + '")')
            exec("self.in_" + str(i) + "= self.findChild(QTextEdit, 'textEdit_" + str(i) + "')")

        x = 1
        for i in voclist:
            z = eval("self.label_" + str(x))
            z.setText(i + "  ")
            x += 1

        self.t1 = Thread(target=self.tick)
        self.t1.start()

        self.show()

    def tick(self):
        while True:
            self.disp.display(self.t)
            self.disp.repaint()
            time.sleep(1)
            self.t -= 1
            if self.t <= 0:
                self.finish()
                return

    def finish(self):
        self.r = []
        # print(self.in_1.toPlainText())
        # self.in_1.setPlainText("")
        try:
            for i in range(1, 29):
                exe = ""
                exec(eval('exe = "self.in_" + str(i) + ".toPlainText()"'))
                self.r.append(exe)

        # noinspection PyBroadException
        except:
            self.r.append("fail")
        print(self.r)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    vocs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
            "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"]
    UIWindow = UI(vocs)
    app.exec_()
