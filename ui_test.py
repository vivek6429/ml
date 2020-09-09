# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testVHsDYs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
################for gui 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys,os
import numpy as np
import pandas as pd
#############################
# second assignment decision tree
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
# from sklearn.externals.six import StringIO  
import io # IO.string
#########################################



class Ui_MainWindow(object):
    def __init__(self):
        print("helloo")
        # self.selectFile(self.tempwindow)
    
    def browse(self):
        filename =QFileDialog.getOpenFileName(self, 'Open File', '.')
        print(filename)

# the entire home screen gui
    def setuphomeUi(self, MainWindow):
        print("hellooworlkd")
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(508, 504)
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName(u"actionexit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        # home screen radio buttons
        self.radioButton_dtorann = QRadioButton(self.centralwidget)
        self.radioButton_dtorann.setObjectName(u"radioButton_dtorann")
        self.radioButton_dtorann.setChecked(False)
        self.gridLayout.addWidget(self.radioButton_dtorann, 2, 0, 1, 2)
        
        self.radioButton_rec = QRadioButton(self.centralwidget)
        self.radioButton_rec.setObjectName(u"radioButton_rec")
        self.radioButton_rec.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_rec, 1, 0, 1, 1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer, 5, 0, 1, 1)
        # next  button
        self.commandLinkButton = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.clicked.connect(self.movetoqn)

        self.gridLayout.addWidget(self.commandLinkButton, 5, 1, 1, 1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)
        # the rxit button forgot to rename 
        self.pushButton_exithome = QPushButton(self.centralwidget)
        self.pushButton_exithome.setObjectName(u"pushButton")
        self.pushButton_exithome.clicked.connect(QCoreApplication.quit)
        self.gridLayout.addWidget(self.pushButton_exithome, 7, 1, 1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 508, 30))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufile.menuAction())
        self.menufile.addAction(self.actionexit)
        self.retranslatehomeUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        self.tempwindow=MainWindow
        # self.movetoqn1()
        

    def retranslatehomeUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"assignment_home", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.radioButton_dtorann.setText(QCoreApplication.translate("MainWindow", u"Dt or ANN for  diabatese data", None))
        self.radioButton_rec.setText(QCoreApplication.translate("MainWindow", u"MovieRecomendation system", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton_exithome.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file", None))


##################################### assignment 1 gui
    def setuprecUi(self, RecUI):
        if not RecUI.objectName():
            RecUI.setObjectName(u"RecUI")
        RecUI.resize(357, 488)
        self.actionexit = QAction(RecUI)
        self.actionexit.setObjectName(u"actionexit")
        self.centralwidget = QWidget(RecUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(100, 180, 256, 171))
        # select ratings button
        self.pushButton_selectrating = QPushButton(self.centralwidget)
        self.pushButton_selectrating.setObjectName(u"pushButton_selectrating")
        self.pushButton_selectrating.setGeometry(QRect(260, 10, 84, 34))
        self.pushButton_selectrating.clicked.connect(self.selectFilerating)
        
        # select movies button
        self.pushButton_selectmovies = QPushButton(self.centralwidget)
        self.pushButton_selectmovies.setObjectName(u"pushButton_selectmovies")
        self.pushButton_selectmovies.setGeometry(QRect(260, 50, 84, 34))
        self.pushButton_selectmovies.clicked.connect(self.selectFilemovies)

        self.label_rating = QLabel(self.centralwidget)
        self.label_rating.setObjectName(u"label_rating")
        self.label_rating.setGeometry(QRect(6, 6, 130, 18))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(6, 46, 128, 18))
        self.label_3_ente_moviename = QLabel(self.centralwidget)
        self.label_3_ente_moviename.setObjectName(u"label_3_ente_moviename")
        self.label_3_ente_moviename.setGeometry(QRect(6, 86, 112, 18))
        self.lineEdit_inputmoviename = QLineEdit(self.centralwidget)
        self.lineEdit_inputmoviename.setObjectName(u"lineEdit_inputmoviename")
        self.lineEdit_inputmoviename.setGeometry(QRect(6, 110, 251, 32))
        self.lineEdit_inputmoviename.setText("Forrest Gump (1994)")
        # do this later lineEntry.textChanged.connect(self.onChanged)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(6, 148, 163, 18))
        # back button
        self.pushButton_back = QPushButton(self.centralwidget)
        self.pushButton_back.setObjectName(u"pushButton_back")    
        self.pushButton_back.setGeometry(QRect(10, 380, 84, 34))
        self.pushButton_back.clicked.connect(self.goback)
        # ok button on assignment 1
        self.pushButton_ok = QPushButton(self.centralwidget)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        self.pushButton_ok.setGeometry(QRect(260, 110, 88, 34))
        self.pushButton_ok.clicked.connect(self.assignment1action)

        RecUI.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(RecUI)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 357, 30))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        RecUI.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(RecUI)
        self.statusbar.setObjectName(u"statusbar")
        RecUI.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufile.menuAction())
        self.menufile.addAction(self.actionexit)
        self.retranslaterecUi(RecUI)
        QMetaObject.connectSlotsByName(RecUI)
        # self.selectFile()

    def retranslaterecUi(self, RecUI):
        RecUI.setWindowTitle(QCoreApplication.translate("RecUI", u"Recommendation System", None))
        self.actionexit.setText(QCoreApplication.translate("RecUI", u"exit", None))
        self.pushButton_selectrating.setText(QCoreApplication.translate("RecUI", u"Select file", None))
        self.pushButton_selectmovies.setText(QCoreApplication.translate("RecUI", u"Select file", None))
        self.label_rating.setText(QCoreApplication.translate("RecUI", u"Select Ratings.csv file", None))
        self.label_2.setText(QCoreApplication.translate("RecUI", u"Select movies.csv file", None))
        self.label_3_ente_moviename.setText(QCoreApplication.translate("RecUI", u"Enter movie name", None))
        self.label_4.setText(QCoreApplication.translate("RecUI", u"Recommended movies are", None))
        self.pushButton_back.setText(QCoreApplication.translate("RecUI", u"Back", None))
        self.pushButton_ok.setText(QCoreApplication.translate("RecUI", u"ok", None))
        self.menufile.setTitle(QCoreApplication.translate("RecUI", u"file", None))

    def movetoqn(self):
        if self.radioButton_rec.isChecked() == True :
            self.setuprecUi(self.tempwindow)
        if self.radioButton_dtorann.isChecked() == True:
            self.setupassignment2Ui(self.tempwindow)
    # custom methods
    def goback(self):
        self.setuphomeUi(self.tempwindow)
    # assignment 1 
    def selectFilerating(self):
        self.fileNameratings =QFileDialog.getOpenFileName(self.tempwindow,"ratingCSV file(*.csv)")
        print("ratings : ",self.fileNameratings[0])
        pass 
    def selectFilemovies(self):
        self.fileNamemovies =QFileDialog.getOpenFileName(self.tempwindow,"moviesCSV file(*.csv)")
        print("movies",self.fileNamemovies[0])
        pass 
    # this function does the assignment 1
    def assignment1action(self):
        inputname=self.lineEdit_inputmoviename.text()
        print(inputname[0])  
        ratings_data = pd.read_csv(self.fileNameratings[0])
        movie_names = pd.read_csv(self.fileNamemovies[0])
        movie_data = pd.merge(ratings_data, movie_names, on='movieId')
        ratings_mean_count=pd.DataFrame(movie_data.groupby('title')['rating'].mean())
        ratings_mean_count['rating_counts']=pd.DataFrame(movie_data.groupby('title')['rating'].count())
        user_movie_rating=movie_data.pivot_table(index='userId',columns='title',values='rating')
        raiting_count=50
        input_movie_ratings = user_movie_rating['Forrest Gump (1994)']
        movieslike_input_movie=user_movie_rating.corrwith(input_movie_ratings)
        corr_input_movie=pd.DataFrame(movieslike_input_movie,columns=['correlation'])
        corr_input_movie.dropna(inplace=True)
        corr_input_movie = corr_input_movie.join(ratings_mean_count['rating_counts'])
        res=corr_input_movie[corr_input_movie ['rating_counts']>raiting_count].sort_values('correlation', ascending=False).head()
        print(res)
        res = res.index.tolist()
        for i in res:
            print(i) 
            self.listWidget.addItem(i)
# now for the asssignment 2----------------------------------------------------------------------
    # assignment 2 gui

    def setupassignment2Ui(self, diabatese):
        if not diabatese.objectName():
            diabatese.setObjectName(u"diabatese")
        diabatese.resize(419, 331)
        self.actionexit = QAction(diabatese)
        self.actionexit.setObjectName(u"actionexit")
        self.actiondid_not_finish_lol = QAction(diabatese)
        self.actiondid_not_finish_lol.setObjectName(u"actiondid_not_finish_lol")
        self.centralwidget = QWidget(diabatese)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_selectfile = QLabel(self.centralwidget)
        self.label_selectfile.setObjectName(u"label_selectfile")

        self.gridLayout.addWidget(self.label_selectfile, 0, 0, 1, 4)

        self.pushButton_selectdiabatese = QPushButton(self.centralwidget)
        self.pushButton_selectdiabatese.setObjectName(u"pushButton_selectdiabatese")

        self.gridLayout.addWidget(self.pushButton_selectdiabatese, 0, 5, 1, 2)

        self.radioButton_useANN = QRadioButton(self.centralwidget)
        self.radioButton_useANN.setObjectName(u"radioButton_useANN")

        self.gridLayout.addWidget(self.radioButton_useANN, 1, 0, 1, 5)

        self.label_enter = QLabel(self.centralwidget)
        self.label_enter.setObjectName(u"label_enter")

        self.gridLayout.addWidget(self.label_enter, 2, 0, 1, 2)

        self.label_listentry = QLabel(self.centralwidget)
        self.label_listentry.setObjectName(u"label_listentry")

        self.gridLayout.addWidget(self.label_listentry, 3, 0, 1, 7)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 4, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 4, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 4, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 4, 3, 1, 1)

        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 4, 4, 1, 1)

        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 4, 5, 1, 1)

        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 4, 6, 1, 1)

        self.checkBox_dt = QCheckBox(self.centralwidget)
        self.checkBox_dt.setObjectName(u"checkBox_dt")

        self.gridLayout.addWidget(self.checkBox_dt, 5, 0, 1, 7)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 6, 2, 1, 2)

        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout.addWidget(self.lineEdit_8, 6, 4, 1, 1)

        self.pushButton_back = QPushButton(self.centralwidget)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.clicked.connect(self.goback)

        self.gridLayout.addWidget(self.pushButton_back, 7, 0, 1, 2)

        diabatese.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(diabatese)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 419, 30))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        diabatese.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(diabatese)
        self.statusbar.setObjectName(u"statusbar")
        diabatese.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menufile.menuAction())
        self.menufile.addAction(self.actionexit)
        self.menufile.addAction(self.actiondid_not_finish_lol)

        self.retranslateassignment2Ui(diabatese)

        QMetaObject.connectSlotsByName(diabatese)
    # setupUi

    def retranslateassignment2Ui(self, diabatese):
        diabatese.setWindowTitle(QCoreApplication.translate("diabatese", u"Asiignment2", None))
        self.actionexit.setText(QCoreApplication.translate("diabatese", u"exit", None))
        self.actiondid_not_finish_lol.setText(QCoreApplication.translate("diabatese", u"did not finish lol", None))
        self.label_selectfile.setText(QCoreApplication.translate("diabatese", u"Select Diabates .csv fileloc", None))
        self.pushButton_selectdiabatese.setText(QCoreApplication.translate("diabatese", u"Select file", None))
        self.radioButton_useANN.setText(QCoreApplication.translate("diabatese", u"Use ANN (needs more tuning)", None))
        self.label_enter.setText(QCoreApplication.translate("diabatese", u"Enter values", None))
        self.label_listentry.setText(QCoreApplication.translate("diabatese", u"Pregnant    insulin      bmi          age        glucose     bp        pedigree", None))
        self.checkBox_dt.setText(QCoreApplication.translate("diabatese", u"Set criterion=\"entropy\" and max_depth=3 in dt model", None))
        self.label.setText(QCoreApplication.translate("diabatese", u"Result", None))
        self.pushButton_back.setText(QCoreApplication.translate("diabatese", u"Back", None))
        self.menufile.setTitle(QCoreApplication.translate("diabatese", u"file", None))




app=QApplication(sys.argv) # the application and internal system config
win=QMainWindow()  # initialize the main QT window
mainui=Ui_MainWindow()
mainui.setuphomeUi(win) # initializing the custom ui on the main window
win.show()
app.exec_()