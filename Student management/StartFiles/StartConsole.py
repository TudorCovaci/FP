
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
from Repos.StudentTextFileRepo import StudentTextFileRepo
from Repos.DisciplineTextFileRepo import DisciplineTextFileRepo
from Repos.GradeTextFileRepo import GradeTextFileRepo
from Repos.StudentBinaryFileRepo import StudentBinaryFileRepo
from Repos.DisciplineBinaryFile import DisciplineBinaryFileRepo
from Repos.GradeBinaryFile import GradeBinaryFileRepo


def readSettings():
    settings = {}
    f = open("settings.properties", "r")
    s = f.read()
    lines = s.split("\n")
    for line in lines:
        tokens = line.split("=")
        settings[tokens[0].strip()] = tokens[1].strip()
    f.close()
    return settings


settings = readSettings()
if settings["repo_type"] == "memory":
    studentRepo = StudentRepo()
    disciplineRepo = DisciplineRepo()
    gradeRepo = GradeRepo()
elif settings["repo_type"] == "text":
    studentRepo = StudentTextFileRepo(settings["student_repo_file"])
    disciplineRepo = DisciplineTextFileRepo(settings["discipline_repo_file"])
    gradeRepo = GradeTextFileRepo(settings["grade_repo_file"])
elif settings["repo_type"] == "binary":
    studentRepo = StudentBinaryFileRepo(settings["student_repo_file"])
    disciplineRepo = DisciplineBinaryFileRepo(settings["discipline_repo_file"])
    gradeRepo = GradeBinaryFileRepo(settings["grade_repo_file"])



studentValidator = StudentValidator(studentRepo)
gradeValidator = GradeValidator(studentRepo, disciplineRepo)
disciplineValidator = DisciplineValidator(disciplineRepo)
undoController = UndoController()
disciplineController = DisciplineController(disciplineRepo, disciplineValidator)
studentController = StudentController(studentRepo, studentValidator)
gradeController = GradeController(gradeRepo, gradeValidator)
if settings["repo_type"] == "memory":
    studentController.initStudent()
    disciplineController.initDisciplines()
    gradeController.initGrades(studentController.getRepo())
statController = StatisticsController(studentController, disciplineController, gradeController)
consoleUI = ConsoleUI(studentController, disciplineController, gradeController, statController, undoController)
consoleUI.start()

