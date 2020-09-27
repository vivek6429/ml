# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Assignment Ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys,os,subprocess,platform # to open tree  image in default app
import numpy as np
import pandas as pd
#############################
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
# from sklearn.externals.six import StringIO  
import io # IO.string
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.fileloc=""
        self.y_pred= None
        self.classifier=None

   

    def setupUi(self, MainWindow):
        # wee need this addr
        self.tempwindow=MainWindow
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(365, 316)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 200, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.predict)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 181, 17))
        self.label.setObjectName("label")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 10, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.browse)
        
        self.label_outlook = QtWidgets.QLabel(self.centralwidget)
        self.label_outlook.setGeometry(QtCore.QRect(10, 60, 67, 17))
        
        self.label_outlook.setObjectName("label_outlook")
        self.label_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_temp.setGeometry(QtCore.QRect(110, 60, 67, 17))
        
        self.label_temp.setObjectName("label_temp")
        self.label_humidity = QtWidgets.QLabel(self.centralwidget)
        self.label_humidity.setGeometry(QtCore.QRect(220, 60, 67, 17))
        
        self.label_humidity.setObjectName("label_humidity")
        self.label_wind = QtWidgets.QLabel(self.centralwidget)
        self.label_wind.setGeometry(QtCore.QRect(10, 130, 41, 17))
        
        self.label_wind.setObjectName("label_wind")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 121, 31))
        self.label_2.setObjectName("label_2")
        
        self.textEdit_outllook = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_outllook.setGeometry(QtCore.QRect(0, 90, 71, 21))
        self.textEdit_outllook.setObjectName("textEdit_outllook")
        self.textEdit_outllook.setText("Sunny")


        self.textEdit_temp = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_temp.setGeometry(QtCore.QRect(100, 90, 71, 21))
        self.textEdit_temp.setText("Hot")
        self.textEdit_temp.setObjectName("textEdit_temp")
        
        self.textEdit_humidity = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_humidity.setGeometry(QtCore.QRect(220, 90, 71, 21))
        self.textEdit_humidity.setText("High")
        self.textEdit_humidity.setObjectName("textEdit_humidity")

        self.textEdit_wind = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_wind.setGeometry(QtCore.QRect(0, 160, 71, 21))
        self.textEdit_wind.setObjectName("textEdit_wind")
        self.textEdit_wind.setText("Weak")
        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(110, 240, 104, 21))
        self.plainTextEdit.setObjectName("plainTextEdit")
        
        self.pushButton_acc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_acc.setGeometry(QtCore.QRect(240, 150, 89, 25))
        self.pushButton_acc.setObjectName("pushButton_acc")
        self.pushButton_acc.clicked.connect(self.printaccuracy)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 365, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def browse(self):
        self.fileloc =QFileDialog.getOpenFileName(self.tempwindow,"DS1 file(*.csv)")
        print("DS1 at ",self.fileloc[0])
        print ("now training..")
        self.mainprogram_assignment()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Randomforest_inputwindow"))
        self.pushButton.setText(_translate("MainWindow", "Predict"))
        self.label.setText(_translate("MainWindow", "Select the DS1.sc file"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse file"))
        self.label_outlook.setText(_translate("MainWindow", "Outlook"))
        self.label_temp.setText(_translate("MainWindow", "Temp"))
        self.label_humidity.setText(_translate("MainWindow", "Humidity"))
        self.label_wind.setText(_translate("MainWindow", "wind"))
        self.label_2.setText(_translate("MainWindow", "PLAY GOLF ?"))
        self.pushButton_acc.setText(_translate("MainWindow", "Acuuracy"))

    def mainprogram_assignment(self):
        # self.self.Preg=int(self.lineEdit.text())

        self.outlook=self.textEdit_outllook.toPlainText()
        self.temp=self.textEdit_temp.toPlainText()
        self.humidity=self.textEdit_humidity.toPlainText()
        self.wind=self.textEdit_wind.toPlainText()
        print(self.outlook,"---testing")


        print("testing")
        self.df_full=pd.read_csv(self.fileloc[0])
        self.df_full.set_index('Day')
        self.df_full.head()
        print("tetsing 123")
        # self.clf=RandomForestClassifier(n_estimators=100)
        


        self.df=self.df_full.drop("Day",1)
        self.df["Outlook"]=self.df["Outlook"].map(dict(Sunny=1,Overcast=0,Rain=-1))
        self.df["Temperature"]=self.df["Temperature"].map(dict(Hot=1,Mild=0,Cool=-1))
        self.df["Humidity"]=self.df["Humidity"].map(dict(High=1,Normal=0))
        self.df["Wind"]=self.df["Wind"].map(dict(Strong=1,Weak=0))
        self.df["Play Golf"]=self.df["Play Golf"].map(dict(Yes=1,No=0))
        self.df.head()

        self.X=self.df.drop("Play Golf",1)
        self.y=self.df['Play Golf']
        X_train, X_test, y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=0)


        self.classifier = RandomForestClassifier()
        self.classifier.fit(X_train, y_train)
        self.y_pred = self.classifier.predict(X_test)
        print(X_test,"\n outcomes in y_test",self.y_test.values)
        print(self.y_pred)

        cm = confusion_matrix(self.y_test, self.y_pred)
        print(cm)
        print('Accuracy ' + str(accuracy_score(self.y_test, self.y_pred)))


        pass

    def printaccuracy(self):
        try :
            if self.y_pred == None:
                print("browse the csv file")
                return
        except: 
            print("working....")

        cm = confusion_matrix(self.y_test,self.y_pred)
        print(cm)
        print('Accuracy ' + str(accuracy_score(self.y_test,self.y_pred)))
        pass

    def predict(self):
        if self.classifier==None:
            print("load csv")
            return

        feature_cols=["Outlook","Temperature","Humidity","Wind"]
        data=pd.DataFrame(columns=feature_cols)
        
        self.outlook=self.textEdit_outllook.toPlainText()
        self.outlook=dict(Sunny=1,Overcast=0,Rain=-1)[self.outlook]

        self.temp=self.textEdit_temp.toPlainText()
        self.temp=dict(Hot=1,Mild=0,Cool=-10)[self.temp]

        self.humidity=self.textEdit_humidity.toPlainText()
        self.humidity=dict(High=1,Normal=0)[self.humidity]
        
        self.wind=self.textEdit_wind.toPlainText()
        self.wind=dict(Strong=1,Weak=0)[self.wind]

        data.loc[0,:]=[self.outlook,self.temp,self.humidity,self.wind]


        print(self.outlook,"---testing")
        y_pred = self.classifier.predict(data)
        print(y_pred)
        self.plainTextEdit.setPlainText(str(y_pred[0]))

        pass
    





app=QApplication(sys.argv) # the application and internal system config
win=QMainWindow()  # initialize the main QT window
mainui=Ui_MainWindow()
mainui.setupUi(win) # initializing the custom ui on the main window

win.show()
app.exec_()