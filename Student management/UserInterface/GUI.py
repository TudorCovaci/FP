from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from UserInterface import supportGUI
from UserInterface.studOpUI import Ui_studWindow
from UserInterface.discUI import Ui_disciWindow
from UserInterface.statUI import Ui_statWindow
class UI_MainWindow(object):

    def openStudUI(self, studCtrl, gradeCtrl, undoCtrl):
        self.window = QtWidgets.QMainWindow()
        self.studUI.setupUi(self.window, studCtrl, gradeCtrl, undoCtrl)
        self.window.show()

    def openDiscUI(self, disciCtrl):
        self.window = QtWidgets.QMainWindow()
        self.disciUI.setupUi(self.window, disciCtrl)
        self.window.show()

    def openStatUI(self, statCtrl):
        self.window = QtWidgets.QMainWindow()
        self.statUI.setupUi(self.window, statCtrl)
        self.window.show()

    def setupUi(self, MainWindow, studCtrl, disciCtrl, gradeCtrl, statCtrl, undoCtrl):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(320, 30, 450, 350))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.studUI = Ui_studWindow()
        self.disciUI = Ui_disciWindow()
        self.statUI = Ui_statWindow()
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(350, 350))
        self.listWidget.setProperty("isWrapping", True)
        self.listWidget.setObjectName("listWidget")
        self.StudOpButton = QtWidgets.QPushButton(self.centralwidget)
        self.StudOpButton.setGeometry(QtCore.QRect(40, 110, 161, 51))
        self.StudOpButton.setObjectName("StudOpButton")
        """
        Stud Operations Button"""
        self.StudOpButton.clicked.connect(partial(self.openStudUI, studCtrl, gradeCtrl, undoCtrl))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.DisciOpButton = QtWidgets.QPushButton(self.centralwidget)
        self.DisciOpButton.setGeometry(QtCore.QRect(40, 170, 161, 51))
        self.DisciOpButton.setObjectName("DisciOpButton")
        """
        Disci Operation Button
        """
        self.DisciOpButton.clicked.connect(partial(self.openDiscUI, disciCtrl))


        self.StatisticsButton = QtWidgets.QPushButton(self.centralwidget)
        self.StatisticsButton.setGeometry(QtCore.QRect(40, 230, 161, 51))
        self.StatisticsButton.setObjectName("StatisticsButton")
        """
        Statistics Button
        """
        self.StatisticsButton.clicked.connect(partial(self.openStatUI, statCtrl))

        self.UndoButton = QtWidgets.QPushButton(self.centralwidget)
        self.UndoButton.setGeometry(QtCore.QRect(40, 290, 161, 51))
        self.UndoButton.setObjectName("UndoButton")
        self.UndoButton.clicked.connect(partial(self.undoOp, undoCtrl))
        self.RedoButton = QtWidgets.QPushButton(self.centralwidget)
        self.RedoButton.setGeometry(QtCore.QRect(40, 350, 161, 51))
        self.RedoButton.setObjectName("RedoButton")
        self.RedoButton.clicked.connect(partial(self.redoOp, undoCtrl))
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(40, 410, 161, 51))
        self.ExitButton.setObjectName("ExitButton")
        """
        comanda buton "EXIT"
        """
        self.ExitButton.clicked.connect(supportGUI.exitApp)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuStudent = QtWidgets.QMenu(self.menubar)
        self.menuStudent.setObjectName("menuStudent")
        self.menuDiscipline = QtWidgets.QMenu(self.menubar)
        self.menuDiscipline.setObjectName("menuDiscipline")
        self.menuGrade = QtWidgets.QMenu(self.menubar)
        self.menuGrade.setObjectName("menuGrade")
        self.menuUndo = QtWidgets.QMenu(self.menubar)
        self.menuUndo.setObjectName("menuUndo")
        self.menuRedo = QtWidgets.QMenu(self.menubar)
        self.menuRedo.setObjectName("menuRedo")
        self.menuStatistics = QtWidgets.QMenu(self.menubar)
        self.menuStatistics.setObjectName("menuStatistics")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionRemove = QtWidgets.QAction(MainWindow)
        self.actionRemove.setObjectName("actionRemove")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionAddDisci = QtWidgets.QAction(MainWindow)
        self.actionAddDisci.setObjectName("actionAddDisci")
        self.actionRemoveDisci = QtWidgets.QAction(MainWindow)
        self.actionRemoveDisci.setObjectName("actionRemoveDisci")
        self.actionAddGrade = QtWidgets.QAction(MainWindow)
        self.actionAddGrade.setObjectName("actionAddGrade")
        self.actionRemoveGrade = QtWidgets.QAction(MainWindow)
        self.actionRemoveGrade.setObjectName("actionRemoveGrade")
        self.actionUpdateDisci = QtWidgets.QAction(MainWindow)
        self.actionUpdateDisci.setObjectName("actionUpdateDisci")
        self.menuFile.addAction(self.actionExit)
        self.menuStudent.addAction(self.actionAdd)
        self.menuStudent.addAction(self.actionRemove)
        self.menuStudent.addAction(self.actionUpdate)
        self.menuDiscipline.addAction(self.actionAddDisci)
        self.menuDiscipline.addAction(self.actionRemoveDisci)
        self.menuDiscipline.addAction(self.actionUpdateDisci)
        self.menuGrade.addAction(self.actionAddGrade)
        self.menuGrade.addAction(self.actionRemoveGrade)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuStudent.menuAction())
        self.menubar.addAction(self.menuDiscipline.menuAction())
        self.menubar.addAction(self.menuGrade.menuAction())
        self.menubar.addAction(self.menuUndo.menuAction())
        self.menubar.addAction(self.menuRedo.menuAction())
        self.menubar.addAction(self.menuStatistics.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StudOpButton.setText(_translate("MainWindow", "Student Operations"))
        self.label.setText(_translate("MainWindow", "Menu"))
        self.DisciOpButton.setText(_translate("MainWindow", "Discipline Operations"))
        self.StatisticsButton.setText(_translate("MainWindow", "Statistics"))
        self.UndoButton.setText(_translate("MainWindow", "Undo"))
        self.RedoButton.setText(_translate("MainWindow", "Redo"))
        self.ExitButton.setText(_translate("MainWindow", "Exit"))
        self.menuFile.setTitle(_translate("MainWindow", "File.."))
        self.menuStudent.setTitle(_translate("MainWindow", "Student..."))
        self.menuDiscipline.setTitle(_translate("MainWindow", "Discipline..."))
        self.menuGrade.setTitle(_translate("MainWindow", "Grade..."))
        self.menuUndo.setTitle(_translate("MainWindow", "Undo"))
        self.menuRedo.setTitle(_translate("MainWindow", "Redo"))
        self.menuStatistics.setTitle(_translate("MainWindow", "Statistics"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))
        self.actionRemove.setText(_translate("MainWindow", "Remove"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionAddDisci.setText(_translate("MainWindow", "Add"))
        self.actionRemoveDisci.setText(_translate("MainWindow", "Remove"))
        self.actionAddGrade.setText(_translate("MainWindow", "Add"))
        self.actionRemoveGrade.setText(_translate("MainWindow", "Remove"))
        self.actionUpdateDisci.setText(_translate("MainWindow", "Update"))

    def undoOp(self,controller):
        controller.undo()
        self.listWidget.addItem("Undo successful!")
        return True

    def redoOp(self,controller):
        controller.redo()
        self.listWidget.addItem("Redo successful!")
        return True