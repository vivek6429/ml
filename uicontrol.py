#!/bin/python3
import sys
import os
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        # parent constructor
        super(MainWindow,self).__init__()
        self.setGeometry(200,200,300,300)# xpos,ypos,width,height
        self.setWindowTitle("Assignment ")
        self.initUI()

    def initUI(self):
        print(self)
        self.label = QtWidgets.QLabel(self)# label on which window
        self.label.setText("aaaa")
        self.label.move(60,60)
        self.b1=QtWidgets.QPushButton(self)
        self.b1.setText("BuTTOnn") 
        self.b1.clicked.connect(self.selectFile)

    def clicked(self):
        self.label.setText("aaaaaaaaaaaaaaaaaaaaaaaa") 
        self.update()
        print("helooo")
    
    def update(self):
        self.label.adjustSize()
    
    def selectFile(self):
        print(self)
        filename=QFileDialog.getOpenFileName(self)
        print(filename[0])
    

        

#     def __home__():
#     def selectFile():
#         # lineEdit.setText(QFileDialog.getOpenFileName())
#         filename=QFileDialog.getOpenFileName()
#         return filename
#     pushButton.clicked.connect(selectFile)
    



def window():
    app=QApplication(sys.argv) # SETUP APP os dependent
    win=MainWindow()  
      
    win.show()
    sys.exit(app.exec_())

window()