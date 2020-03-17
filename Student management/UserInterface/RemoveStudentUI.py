# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RemoveStudentUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from Controllers.UndoController import *
class Ui_RemoveStudUI(object):
    def setupUi(self, RemoveStudWindow, studCtrl, gradeCtrl, undoCtrl):
        RemoveStudWindow.setObjectName("RemoveStudWindow")
        RemoveStudWindow.resize(399, 314)
        self.centralwidget = QtWidgets.QWidget(RemoveStudWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RemoveStudButt = QtWidgets.QPushButton(self.centralwidget)
        self.RemoveStudButt.setGeometry(QtCore.QRect(170, 220, 93, 28))
        self.RemoveStudButt.setObjectName("RemoveStudButt")
        self.RemoveStudButt.clicked.connect(partial(self.removeStudent, studCtrl,gradeCtrl, undoCtrl))
        self.ClearButt = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButt.setGeometry(QtCore.QRect(280, 220, 93, 28))
        self.ClearButt.setObjectName("ClearButt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(92, 100, 221, 21))
        self.lineEdit.setObjectName("lineEdit")
        RemoveStudWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RemoveStudWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 399, 26))
        self.menubar.setObjectName("menubar")
        RemoveStudWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RemoveStudWindow)
        self.statusbar.setObjectName("statusbar")
        RemoveStudWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RemoveStudWindow)
        QtCore.QMetaObject.connectSlotsByName(RemoveStudWindow)

    def retranslateUi(self, RemoveStudWindow):
        _translate = QtCore.QCoreApplication.translate
        RemoveStudWindow.setWindowTitle(_translate("RemoveStudWindow", "Remove Student..."))
        self.RemoveStudButt.setText(_translate("RemoveStudWindow", "Remove"))
        self.ClearButt.setText(_translate("RemoveStudWindow", "Clear"))
        self.label.setText(_translate("RemoveStudWindow", "Name/ID"))

    def removeStudent(self, studCtrl, gradeCtrl ,undoCtrl):
        studSearch = self.lineEdit.text()
        student = studCtrl.find(studSearch)
        if student is False:
            raise ValueError("Error: The student was not found!")
        studCtrl.remove(student.id)
        cascadeRemove = CascadeOperation()
        redoFunction = FunctionCall(studCtrl.remove, student.id)
        undoFunction = FunctionCall(studCtrl.create, student.id, student.name)
        undoRemove = Operation(undoFunction, redoFunction)
        cascadeRemove.add(undoRemove)
        listOfGrades = gradeCtrl.findAllGradesForStudent(student.id)
        for grade in listOfGrades:
            gradeCtrl.remove(grade)
            redoFunction = FunctionCall(gradeCtrl.remove, grade)
            undoFunction = FunctionCall(gradeCtrl.create, grade.studID, grade.disciID, grade.value)
            undoRemove = Operation(undoFunction, redoFunction)
            cascadeRemove.add(undoRemove)
        undoCtrl.addOperation(cascadeRemove)
        return True