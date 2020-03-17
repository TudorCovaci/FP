# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DiscOp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_disciWindow(object):
    def setupUi(self, disciWindow, disciCtrl):
        disciWindow.setObjectName("disciWindow")
        disciWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(disciWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 80, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 170, 160, 51))
        self.pushButton.setObjectName("addButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 250, 160, 51))
        self.pushButton_2.setObjectName("clearButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 170, 160, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 320, 160, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 250, 160, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 410, 731, 121))
        self.textBrowser.setObjectName("textBrowser")
        disciWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(disciWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuExit_Discipline_Operations = QtWidgets.QMenu(self.menubar)
        self.menuExit_Discipline_Operations.setObjectName("menuExit_Discipline_Operations")
        disciWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(disciWindow)
        self.statusbar.setObjectName("statusbar")
        disciWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(disciWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuExit_Discipline_Operations.addAction(self.actionExit)
        self.menubar.addAction(self.menuExit_Discipline_Operations.menuAction())

        self.retranslateUi(disciWindow)
        QtCore.QMetaObject.connectSlotsByName(disciWindow)

    def retranslateUi(self, disciWindow):
        _translate = QtCore.QCoreApplication.translate
        disciWindow.setWindowTitle(_translate("disciWindow", "Discipline Operations"))
        self.label.setText(_translate("disciWindow", "Discipline Operations"))
        self.pushButton.setText(_translate("disciWindow", "Add Discipline"))
        self.pushButton_2.setText(_translate("disciWindow", "Remove Discipline"))
        self.pushButton_3.setText(_translate("disciWindow", "Update Discipline"))
        self.pushButton_4.setText(_translate("disciWindow", "Display Disciplines"))
        self.pushButton_5.setText(_translate("disciWindow", "Search Discipline"))
        self.menuExit_Discipline_Operations.setTitle(_translate("disciWindow", "File"))
        self.actionExit.setText(_translate("disciWindow", "Exit"))

