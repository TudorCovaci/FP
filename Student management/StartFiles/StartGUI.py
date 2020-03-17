
from Controllers.StudentController import StudentController
from Controllers.GradeController import GradeController
from Controllers.DisciplineController import DisciplineController
from Repos.DisciplineRepo import DisciplineRepo
from Repos.StudentRepo import StudentRepo
from Repos.GradeRepo import GradeRepo
from domain.GradeValidator import GradeValidator
from domain.DisciplineValidator import DisciplineValidator
from domain.StudentValidator import StudentValidator
from UserInterface.ConsoleUI import ConsoleUI
from Statistics.StatisticsController import StatisticsController
from Controllers.UndoController import UndoController
import sys
from PyQt5 import QtCore, QtDesigner, QtWidgets
from UserInterface.GUI import UI_MainWindow
studentRepo = StudentRepo()
disciplineRepo = DisciplineRepo()
gradeRepo = GradeRepo()
studentValidator = StudentValidator(studentRepo)
gradeValidator = GradeValidator(studentRepo, disciplineRepo)
disciplineValidator = DisciplineValidator(disciplineRepo)
undoController = UndoController()
disciplineController = DisciplineController(disciplineRepo, disciplineValidator)
studentController = StudentController(studentRepo, studentValidator)
gradeController = GradeController(gradeRepo, gradeValidator)
statController = StatisticsController(studentController, disciplineController, gradeController)
#studentController.initStudent()
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = UI_MainWindow()
ui.setupUi(MainWindow, studentController, disciplineController, gradeController, statController, undoController)
MainWindow.show()
sys.exit(app.exec_())


