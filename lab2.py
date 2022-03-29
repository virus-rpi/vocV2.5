for i in range(1, 29):
    eval("self.label_", i, " = self.findChild(QLabel, 'label_", i, "')")
    eval("self.in_", i, "= self.findChild(QTextEdit, 'textEdit_", i, "')")
