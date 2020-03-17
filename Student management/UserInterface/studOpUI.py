# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudOp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from UserInterface.addStudentUI import Ui_addStudentUI
from UserInterface.RemoveStudentUI import Ui_RemoveStudUI

class Ui_studWindow(object):
    def openAddStudentUI(self, controller, undoCtrl):
        self.window = QtWidgets.QMainWindow()
        self.addStudentUI.setupUi(self.window, controller, undoCtrl)
        self.window.show()

    def openRemoveStudentUI(self, studCtrl, gradeCtrl, undoCtrl):
        self.window = QtWidgets.QMainWindow()
        self.removeStudentUI.setupUi(self.window, studCtrl, gradeCtrl, undoCtrl)
        self.window.show()

    def setupUi(self, studWindow, studCtrl, gradeCtrl, undoCtrl):
        studWindow.setObjectName("studWindow")
        studWindow.resize(800, 600)
        studWindow.setAnimated(True)
        studWindow.setDocumentMode(False)
        studWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        studWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(studWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 70, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.addStudentUI = Ui_addStudentUI()
        self.addStudentBut = QtWidgets.QPushButton(self.centralwidget)
        self.addStudentBut.setGeometry(QtCore.QRect(150, 150, 161, 51))
        self.addStudentBut.setObjectName("addStudentBut")

        #addStudent Button operation
        self.addStudentBut.clicked.connect(partial(self.openAddStudentUI, studCtrl, undoCtrl))

        self.removeStudentUI = Ui_RemoveStudUI()
        self.removeStudentBut = QtWidgets.QPushButton(self.centralwidget)
        self.removeStudentBut.setGeometry(QtCore.QRect(150, 210, 161, 51))
        self.removeStudentBut.setObjectName("removeStudentBut")

        #removeStudent Button operation
        self.removeStudentBut.clicked.connect(partial(self.openRemoveStudentUI, studCtrl, gradeCtrl, undoCtrl))

        self.updateStudentBut = QtWidgets.QPushButton(self.centralwidget)
        self.updateStudentBut.setGeometry(QtCore.QRect(150, 280, 161, 51))
        self.updateStudentBut.setObjectName("updateStudentBut")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(460, 150, 161, 51))
        self.addButton.setObjectName("addButton")
        self.dispGradesBut = QtWidgets.QPushButton(self.centralwidget)
        self.dispGradesBut.setGeometry(QtCore.QRect(460, 210, 161, 51))
        self.dispGradesBut.setCheckable(True)
        self.dispGradesBut.setChecked(False)
        self.dispGradesBut.setObjectName("dispGradesBut")
        self.searchStudBut = QtWidgets.QPushButton(self.centralwidget)
        self.searchStudBut.setGeometry(QtCore.QRect(460, 280, 161, 51))
        self.searchStudBut.setObjectName("searchStudBut")
        self.displayStudentsBut = QtWidgets.QPushButton(self.centralwidget)
        self.displayStudentsBut.setGeometry(QtCore.QRect(300, 360, 161, 51))
        self.displayStudentsBut.setObjectName("displayStudentsBut")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 420, 741, 121))
        self.listWidget.setObjectName("studList")
        self.displayStudentsBut.clicked.connect(partial(self.displayStudents, self.listWidget, studCtrl))
        studWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(studWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuExit_student_operations = QtWidgets.QMenu(self.menubar)
        self.menuExit_student_operations.setObjectName("menuExit_student_operations")
        studWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(studWindow)
        self.statusbar.setObjectName("statusbar")
        studWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuExit_student_operations.menuAction())

        self.retranslateUi(studWindow)
        QtCore.QMetaObject.connectSlotsByName(studWindow)

    def retranslateUi(self, studWindow):
        _translate = QtCore.QCoreApplication.translate
        studWindow.setWindowTitle(_translate("studWindow", "Student Operations"))
        self.label.setText(_translate("studWindow", "Student Operations"))
        self.addStudentBut.setText(_translate("studWindow", "Add Student"))
        self.removeStudentBut.setText(_translate("studWindow", "Remove Student"))
        self.updateStudentBut.setText(_translate("studWindow", "Update Student"))
        self.addButton.setText(_translate("studWindow", "Grade Student"))
        self.dispGradesBut.setText(_translate("studWindow", "Display grades for a student"))
        self.searchStudBut.setText(_translate("studWindow", "Search for a student"))
        self.displayStudentsBut.setText(_translate("studWindow", "Display students"))
        self.menuExit_student_operations.setTitle(_translate("studWindow", "Exit student operations"))

    def displayStudents(self, location, controller):
        location.clear()
        if len(controller.getRepo()) == 0:
            location.addItem("No students in repo!")
        location.addItem(str(controller))
        return True