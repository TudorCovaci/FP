# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddStudentUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from Controllers.UndoController import *
class Ui_addStudentUI(object):
    def setupUi(self, addStudentUI, controller, undoController):
        addStudentUI.setObjectName("addStudentUI")
        addStudentUI.resize(530, 420)
        self.centralwidget = QtWidgets.QWidget(addStudentUI)
        self.centralwidget.setObjectName("centralwidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(310, 320, 93, 28))
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(partial(self.addStudent, controller, undoController))
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(420, 320, 93, 28))
        self.clearButton.setObjectName("clearButton")
        self.clearButton.clicked.connect(self.clearLines)
        self.idLine = QtWidgets.QLineEdit(self.centralwidget)
        self.idLine.setGeometry(QtCore.QRect(180, 150, 241, 31))
        self.idLine.setObjectName("idLine")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 150, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.nameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLine.setGeometry(QtCore.QRect(180, 210, 241, 31))
        self.nameLine.setObjectName("nameLine")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        addStudentUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(addStudentUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 26))
        self.menubar.setObjectName("menubar")
        addStudentUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(addStudentUI)
        self.statusbar.setObjectName("statusbar")
        addStudentUI.setStatusBar(self.statusbar)

        self.retranslateUi(addStudentUI)
        QtCore.QMetaObject.connectSlotsByName(addStudentUI)

    def retranslateUi(self, addStudentUI):
        _translate = QtCore.QCoreApplication.translate
        addStudentUI.setWindowTitle(_translate("addStudentUI", "Add student..."))
        self.addButton.setText(_translate("addStudentUI", "Add"))
        self.clearButton.setText(_translate("addStudentUI", "Clear"))
        self.label.setText(_translate("addStudentUI", "ID"))
        self.label_2.setText(_translate("addStudentUI", "Name"))
        self.label_3.setText(_translate("addStudentUI", "Add Student"))

    def addStudent(self, controller, undoController):
        studID = self.idLine.text()
        studName = self.nameLine.text()
        controller.create(studID, studName)
        undoFunction = FunctionCall(controller.remove, studID)
        redoFunction = FunctionCall(controller.create, studID, studName)
        undoCreate = Operation(undoFunction, redoFunction)
        undoController.addOperation(undoCreate)
        print(str(controller))

    def clearLines(self):
        self.idLine.clear()
        self.nameLine.clear()



