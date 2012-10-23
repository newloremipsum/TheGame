#!/usr/bin/python3.2

import sys
from PyQt4 import QtGui, QtCore

width = 500
num = 10

class GameForm(QtGui.QDialog):

    def buttonPressed(self):
            msgbox = QtGui.QMessageBox.about(self, "msgBox", "a button has been pressed")
            
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.btnEndTurn = QtGui.QPushButton("End Turn", self)
        self.btnEndTurn.setGeometry(width+10, 50, 2*width/num, width/num)
        self.btnAttack = QtGui.QPushButton("Attack", self)
        self.btnAttack.setGeometry(width+10, 100, 2*width/num, width/num)
        self.btnMove = QtGui.QPushButton("Move", self)
        self.btnMove.setGeometry(width+10, 150, 2*width/num, width/num)
        self.setGeometry(100, 100, width + 120, width)
        self.btns = []
        for i in xrange(num):
            self.btns.append([QtGui.QPushButton(str(i)+';'+str(j), self) for j in xrange(num)])
            for j in xrange(num):
                self.btns[i][j].setGeometry(i*width/num, j * width/num, width/num, width/num)
                self.btns[i][j].clicked.connect(self.buttonPressed)
    
        #print str(j * width/num)
#self.connect(btnQuit, QtCore.SIGNAL('clicked()'), quit)

app = QtGui.QApplication(sys.argv)
mainForm = GameForm()
mainForm.show()
app.exec_()
