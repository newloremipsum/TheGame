#!/usr/bin/python2.7

import sys
from PyQt4 import QtGui, QtCore

class TestGui(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)

        self.setGeometry(600, 300, 400, 400)
        self.setWindowTitle("The")
        btnLines = []
        for j in range(10):
            btnLines.append([QtGui.QPushButton(str(i) + ';' + str(j), self) for i in xrange(10)])
            for i in range(10):
                btnLines[j][i].setGeometry(i*40, j*40, 40, 40)

app = QtGui.QApplication(sys.argv)
tg = TestGui()
tg.show()
app.exec_()
