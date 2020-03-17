import unittest


from domain.Discipline import Discipline
from domain.Grade import Grade
from domain.Student import Student
from domain.StudentValidator import StudentValidator
from domain.DisciplineValidator import DisciplineValidator
from domain.GradeValidator import GradeValidator


from Controllers.DisciplineController import DisciplineController
from Controllers.StudentController import StudentController
from Controllers.GradeController import GradeController
from Controllers.UndoController import *

from Repos.DisciplineRepo import DisciplineRepo
from Repos.StudentRepo import StudentRepo
from Repos.GradeRepo import GradeRepo

from Statistics.StatisticsController import StatisticsController

class TestDiscipline(unittest.TestCase):

    def testDiscipline(self):
        discipline1 = Discipline(1, "math")
        discipline2 = Discipline(1, "mAth")
        self.assertTrue(discipline1 == discipline2)
        self.assertEqual(str(discipline1), str(discipline2))
        discipline3 = Discipline(1, "Mathematics")
        self.assertTrue(discipline3.partialMatch(discipline2.name))
        self.assertTrue(discipline3.partialMatch(discipline1.name))
        discipline3.id = 12
        self.assertTrue(discipline3.id == 12)


class TestStudent(unittest.TestCase):

    def testStudent(self):
        student1 = Student(1, "Tudor")
        student2 = Student(1, "tUdOr")
        self.assertTrue(str(student1) == str(student2))
        self.assertTrue(student1 == student2)
        student3 = Student(2, "tudor")
        self.assertFalse(student1 == student3)
        student4 = Student(1, "tudor covaci")
        self.assertFalse(student2 == student4)
        student1.id = 12
        student1.name = "Mihai"
        self.assertTrue(str(student1) == str(Student(12, "Mihai")))
        self.assertTrue(student1.partialMatch("hai") is True)


class TestGrade(unittest.TestCase):

    def testGrade(self):
        grade1 = Grade(1, 2, 3)
        grade2 = Grade(3, 2, 1)
        self.assertFalse(grade1 == grade2)
        self.assertEqual(grade1.studID, 1)
        self.assertEqual(grade1.disciID, 2)
        self.assertEqual(grade1.value, 3)
        self.assertTrue(str(grade1) == "Student ID: 1\tDiscipline ID: 2\tGrade: 3\n")


class TestDisciplineValidator(unittest.TestCase):

    def testValidator(self):

        disciplineRepo = DisciplineRepo()
        disciplineValidator = DisciplineValidator(disciplineRepo)
        disciplineRepo.add(Discipline(1, "Math"))
        with self.assertRaises(ValueError):
            disciplineValidator.validate(Discipline(1, "English"))
        with self.assertRaises(ValueError):
            disciplineValidator.validate(Discipline(-1, "Math"))
        with self.assertRaises(ValueError):
            disciplineValidator.validate(Discipline(44, ""))
        with self.assertRaises(ValueError):
            disciplineValidator.validate(Discipline('ab', "abs"))
        with self.assertRaises(TypeError):
            disciplineValidator.validate(1)


class TestGradeValidator(unittest.TestCase):

    def testValidator(self):
        studentRepo = StudentRepo()
        disciplineRepo = DisciplineRepo()
        with self.assertRaises(TypeError):
            GradeValidator(1, disciplineRepo)
        gradeValidator = GradeValidator(studentRepo, disciplineRepo)
        with self.assertRaises(ValueError):
            gradeValidator.validate(Grade(-1, -1, -1))
        gradeValidator = GradeValidator(studentRepo, disciplineRepo)
        with self.assertRaises(TypeError):
            gradeValidator.validate(1)


class TestStudentValidator(unittest.TestCase):

    def testStudentValidator(self):
        studentRepo = StudentRepo()
        studentValidator = StudentValidator(studentRepo)
        studentRepo.add(Student(1, "Tudor"))
        with self.assertRaises(TypeError):
            studentValidator.validate(1)
        with self.assertRaises(ValueError):
            studentValidator.validate(Student(-1, ""))
        with self.assertRaises(ValueError):
            studentValidator.validate(Student("abc", "abs"))


class TestDisciplineRepo(unittest.TestCase):

    def testDisciplineRepo(self):
        disciplineRepo = DisciplineRepo()
        discipline1 = Discipline(1, "Math")
        discipline2 = Discipline(2, "Mathematics")
        disciplineRepo.add(discipline1)
        self.assertTrue(len(disciplineRepo) == 1)
        disciplineRepo.add(discipline2)
        self.assertTrue(len(disciplineRepo) == 2)
        self.assertTrue(len(disciplineRepo.findAllDisciplines("math")) == 2)
        self.assertRaises(ValueError, disciplineRepo.remove, 3)
        disciplineRepo.remove(2)
        self.assertFalse(discipline2 in disciplineRepo.getAll())
        disciplineRepo.clear()
        discipline1 = Discipline(1, "Math")
        disciplineRepo.add(Discipline(1, "Math"))
        self.assertRaises(ValueError, disciplineRepo.find, -1)
        self.assertRaises(ValueError, disciplineRepo.find, "")
        self.assertTrue(str(disciplineRepo) == (str(discipline1)+"\n"))
        newDiscipline = Discipline(11, "Geography")
        disciplineRepo.add(Discipline(13, "Math"))
        with self.assertRaises(ValueError):
            disciplineRepo.update(12, newDiscipline)
        disciplineRepo.update(1, newDiscipline)
        self.assertTrue(disciplineRepo.find("geography") == newDiscipline)
        self.assertTrue(disciplineRepo.find(13) == Discipline(13, "Math"))


class TestStudentRepo(unittest.TestCase):
    def testStudentRepo(self):
        studRepo = StudentRepo()
        student1 = Student(1, "Tudor")
        student2 = Student(2, "Tudor Covaci")
        studRepo.add(student1)
        self.assertTrue(len(studRepo) == 1)
        studRepo.add(student2)
        self.assertTrue(len(studRepo) == 2)
        student3 = Student(3, "Mihai")
        studRepo.update(student2, student3)
        self.assertTrue(studRepo.getAll()[1] == student3)
        studRepo.remove(student1.id)
        self.assertFalse(student1 in studRepo.getAll())
        studRepo.clear()
        self.assertTrue(len(studRepo) == 0)
        student = Student(1, "Tudor")
        studRepo.add(student)
        self.assertTrue(str(studRepo) == (str(student) + "\n"))
        with self.assertRaises(ValueError):
            studRepo.remove(100)
        self.assertRaises(ValueError, studRepo.find, -1)
        self.assertRaises(ValueError, studRepo.find, "")
        self.assertTrue(studRepo.find("tudor") == student)


class TestGradeRepo(unittest.TestCase):

    def testGradeRepo(self):
        gradeRepo = GradeRepo()
        grade1 = Grade(1, 2, 3)
        grade2 = Grade(1, 4, 5)
        grade3 = Grade(2, 4, 10)
        grade4 = Grade(4, 5, 9)
        gradeRepo.add(grade1)
        gradeRepo.add(grade2)
        self.assertTrue(len(gradeRepo) == 2)
        gradeRepo.add(grade3)
        gradeRepo.add(grade4)
        self.assertTrue(len(gradeRepo) == 4)
        listOfStudentGrades = gradeRepo.findAllGradesForStudent(1)
        self.assertTrue(len(listOfStudentGrades) == 2)
        listOfDisciplineGrades = gradeRepo.findAllGradesForDiscipline(4)
        self.assertTrue(len(listOfDisciplineGrades) == 2)
        listOfStudentGrades = gradeRepo.findAllGradesForStudent(4)
        self.assertTrue(len(listOfStudentGrades) == 1)
        gradeRepo.clear()
        grade = Grade(12, 11, 10)
        gradeRepo.add(grade)
        self.assertTrue(str(gradeRepo) == (str(grade) + "\n"))


class TestStudentController(unittest.TestCase):

    def testStudentController(self):
        studentRepo = StudentRepo()
        studentValidator = StudentValidator(studentRepo)
        studentController = StudentController(studentRepo, studentValidator)
        studentController.create(1, "Tudor")
        studentController.create(2, "Tudor Covaci")
        self.assertTrue(studentController.getStudentCount() == 2)
        studentController.create(3, "Mihai")
        studentController.create(4, "Misu")
        self.assertTrue(studentController.getStudentCount() == 4)
        studentController.remove(3)
        self.assertTrue(studentController.getStudentCount() == 3)
        studentController.remove(1)
        self.assertTrue(studentController.getStudentCount() == 2)
        studentController.update(2, "Tudor Covaci", 2, "Tudor")
        self.assertFalse(Student(2, "Tudor Covaci") in studentController.getRepo())
        self.assertTrue(studentController.find(2) == Student(2, "Tudor"))
        studentController.create(10, "Tudor Arghezi")
        self.assertTrue(len(studentController.findPartial("tu")) == 2)
        studentController.clear()
        self.assertTrue(str(studentController) == "")
        studentController.initStudent()
        self.assertTrue(len(studentController.idLists()) == 100)


class TestDisciplineController(unittest.TestCase):

    def testDisciplineController(self):
        disciplineRepo = DisciplineRepo()

        disciplineValidator = DisciplineValidator(disciplineRepo)
        disciplineController = DisciplineController(disciplineRepo, disciplineValidator)
        disciplineController.initDisciplines()
        self.assertTrue(disciplineController.getDisciplineCount() == 10)
        disciplineController.clear()
        self.assertTrue(str(disciplineController) == "")
        disciplineController.create(1, "Math")
        disciplineController.remove("Math")
        self.assertTrue(disciplineController.getDisciplineCount() == 0)
        disciplineController.create(2, "Math")
        self.assertTrue(disciplineController.getDisciplineCount() == 1)
        with self.assertRaises(ValueError):
            disciplineController.create(2, "Math")
        disciplineController.create(3, "Mathematics")
        print(len(disciplineController.findPartial("ma")))
        self.assertTrue(len(disciplineController.findPartial("ma")) == 2)
        disciplineController.remove(3)
        self.assertTrue(disciplineController.getDisciplineCount() == 1)
        self.assertTrue(disciplineController.update(2, 4, "Music") is True)
        self.assertFalse(disciplineController.find(1))
        self.assertTrue(disciplineController.find(4))
        disciplineController.clear()
        self.assertTrue(str(disciplineController) == "")
        self.assertTrue(disciplineController.getRepo() == disciplineRepo.getAll())


class TestGradeController(unittest.TestCase):

    def testGradeController(self):
        gradeRepo = GradeRepo()
        studentRepo = StudentRepo()
        disciplineRepo = DisciplineRepo()
        studentValidator = StudentValidator(studentRepo)
        studentController = StudentController(studentRepo, studentValidator)
        disciplineValidator = DisciplineValidator(disciplineRepo)
        disciplineController = DisciplineController(disciplineRepo, disciplineValidator)
        studentController.initStudent()
        disciplineController.initDisciplines()
        gradeValidator = GradeValidator(studentRepo, disciplineRepo)
        gradeController = GradeController(gradeRepo, gradeValidator)
        gradeController.initGrades(studentRepo.getAll())
        studentController.create(1, "Tudor")
        with self.assertRaises(TypeError):
            GradeController(1, gradeValidator)
        self.assertTrue(gradeController.getSize() == 3000)
        self.assertTrue(str(gradeController) == str(gradeRepo))
        gradeController.clear()
        self.assertTrue(gradeController.getSize() == 0)
        gradeController.create(1, 8, 10)
        self.assertTrue(gradeController.getSize() == 1)
        gradeController.remove(Grade(1, 8, 10))
        self.assertTrue(gradeController.getSize() == 0)
        gradeController.create(1, 10, 8)
        gradeController.create(1, 9, 8)
        self.assertTrue(len(gradeController.findAllGradesForStudent(1)) == 2)
        self.assertTrue(len(gradeController.findAllGradesForDiscipline(10)) == 1)
        gradeController.remove(Grade(1, 10, 8))
        gradeController.remove(Grade(1, 9, 8))
        self.assertTrue(gradeController.getSize() == 0)
        self.assertTrue(str(gradeController) == "")


class TestUndoController(unittest.TestCase):

    def testUndoController(self):
        def rv():
            raise ValueError("test")

        def rt():
            raise TypeError("test")

        def exampleTrue():
            return True

        def exampleFalse():
            return False

        functionEx = FunctionCall(rv)
        self.assertRaises(ValueError, functionEx.call)
        functionEx2 = FunctionCall(rt)
        operationEx = Operation(functionEx, functionEx2)
        self.assertRaises(ValueError, operationEx.undo)
        self.assertRaises(TypeError, operationEx.redo)
        cascadeEx = CascadeOperation()
        cascadeEx.add(operationEx)
        self.assertRaises(ValueError, cascadeEx.undo)
        self.assertRaises(TypeError, cascadeEx.redo)
        undoController = UndoController()
        undoController.addOperation(cascadeEx)
        self.assertRaises(ValueError, undoController.undo)
        self.assertRaises(ValueError, undoController.redo)
        functExample = FunctionCall(exampleTrue)
        functExample2 = FunctionCall(exampleFalse)
        operationEx2 = Operation(functExample, functExample2)
        undoController2 = UndoController()
        undoController2.addOperation(operationEx2)
        undoController2.undo()
        with self.assertRaises(ValueError):
            undoController2.undo()
        undoController2.redo()
        with self.assertRaises(ValueError):
            undoController2.redo()


class TestStatistics(unittest.TestCase):

    def testStatisticsController(self):
        gradeRepo = GradeRepo()
        studentRepo = StudentRepo()
        disciplineRepo = DisciplineRepo()
        studentValidator = StudentValidator(studentRepo)
        studentController = StudentController(studentRepo, studentValidator)
        disciplineValidator = DisciplineValidator(disciplineRepo)
        disciplineController = DisciplineController(disciplineRepo, disciplineValidator)
        gradeValidator = GradeValidator(studentRepo, disciplineRepo)
        gradeController = GradeController(gradeRepo, gradeValidator)
        statisticsController = StatisticsController(studentController, disciplineController, gradeController)
        studentController.create(1, "tudor")
        studentController.create(2, "covaci")
        disciplineController.create(1, "math")
        gradeController.create(1, 1, 10)
        gradeController.create(2, 1, 4)
        studentsEnrolled = statisticsController.studentsEnrolledAtDiscipline("math")
        self.assertTrue(len(studentsEnrolled) == 2)
        with self.assertRaises(ValueError):
            statisticsController.studentsEnrolledAtDiscipline(100)

        self.assertTrue(len(statisticsController.failingStudents()) == 1)
        gradeController.remove(Grade(1, 1, 10))
        gradeController.remove(Grade(2, 1, 4))
        self.assertTrue(len(statisticsController.studentsEnrolledAtDiscipline(1)) == 0)
        self.assertTrue(statisticsController.computeAverage(1,1) == -1)
        gradeController.create(1, 1, 10)
        gradeController.create(2, 1, 5)
        self.assertTrue(statisticsController.bestSchoolSituation()[0][0].name == "Tudor")
        disciplineController.create(2, "Biology")
        self.assertTrue(len(statisticsController.activeDisciplines()) == 1)

