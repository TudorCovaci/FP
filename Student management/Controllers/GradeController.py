from domain.Grade import Grade
from domain.GradeValidator import GradeValidator
from Repos.GradeRepo import GradeRepo
from random import randint
from Repos.GradeTextFileRepo import GradeTextFileRepo

class GradeController:

    def __init__(self, gradeRepo, gradeValidator):
        if not(isinstance(gradeRepo, GradeRepo) and isinstance(gradeValidator, GradeValidator)):
            raise TypeError("Error: Invalid repo/validator passed as arguments!")
        self._repo = gradeRepo
        self._validator = gradeValidator

    def __str__(self):
        return str(self._repo)

    def initGrades(self, studList):
        """
        Initilaizes grade database
        """
        for student in studList:
            for i in range(1, 11):
                for j in range(3):
                    self.create(student.id, i, randint(3, 10))
        return True

    def getSize(self):
        """
        Returns the size of the repository
        """
        return len(self._repo)

    def create(self, studentID, disciplineID, gradeValue):
        """
        Adds a new grade to the grade repo
        """
        grade = Grade(studentID, disciplineID, gradeValue)
        self._validator.validate(grade)
        self._repo.add(grade)
        return grade

    def clear(self):
        """
        Clears the repository
        """
        return self._repo.clear()
    def remove(self, grade):
        """
        Removes a grade from the database
        """
        return self._repo.remove(grade)

    def findAllGradesForStudent(self, studentID):
        """
        Finds all grades for a student
        """
        return self._repo.findAllGradesForStudent(studentID)

    def findAllGradesForDiscipline(self, disciplineID):
        """
        Finds all grades for a student
        """
        return self._repo.findAllGradesForDiscipline(disciplineID)
