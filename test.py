# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assignment 2 uiXyYMJb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import sys,os


class Ui_diabatese(object):
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
    # retranslateUi


app=QApplication(sys.argv) 
win=QMainWindow()  
mainui=Ui_diabatese()
mainui.setupassignment2Ui(win)
win.show()
app.exec_()
