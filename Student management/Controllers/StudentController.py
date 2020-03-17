
from domain.Student import Student
from random import choice
from random import randint
from domain.Lab9Module import sorted

class StudentController:
    """
    Class for student-wise operations
    """
    def __init__(self, studentRepo, studentValidator):
        """
        Constructor
        """
        self._repo = studentRepo
        self._validator = studentValidator

    def __str__(self):
        return str(self._repo)

    def initStudent(self):
        firstNames = ["Lara", "Ayra", "Ruby", "Clementine", "Charmine",
                      "Tammy", "Ruby", "Josie", "Luna", "Erika", "Kelly",
                      "Adrian", "Luis", "Jesse", "Marcus", "Dewey", "Brent",
                      "Asher", "Tyrese", "Alton"]
        lastNames = ["Wilson", "Howell", "Clark", "Byrne", "Paul",
                     "Welch", "Ray", "Perry", "Solis", "Reed", "Wyatt",
                     "Vargas", "Kelley", "Carter", "Fleming", "Osborne",
                     "Alexander", "Hall", "Peterson", "Riley"]
        i = 0
        while i < 100:
            try:
                self.create(randint(100, 999), choice(firstNames) + " " + choice(lastNames))
            except:
                i -= 1
            i += 1

        return True

    def idLists(self):
        """
        Returns a list with all the id's in the data base
        """
        idList = []
        for student in self.getRepo():
            idList.append(student.id)
        return idList

    def create(self, studentID, studentName):
        """
        Creates a new student and adds it to the repository, if valid
        """

        student = Student(studentID, studentName)
        self._validator.validate(student)
        self._repo.add(student)
        return student

    def remove(self, studentID):
        """
        Removes the student with the given id from the repository
        """
        return self._repo.remove(studentID)

    def find(self, searchCrit):
        """
        Finds a student by id
        """
        return self._repo.find(searchCrit)



    def findPartial(self, searchedName):
        """
        Finds partial matches for the searched name
        """
        searchedName = searchedName.lower()
        results = []
        for student in self.getRepo():
            auxName = student.name.lower()
            auxStudent = Student(student.id, auxName)
            if auxStudent.partialMatch(searchedName) is True:
                results.append(student)
        return results

    def update(self, oldID, oldName, newID, newName):
        """
        Updates the old student with the new one
        """
        oldStudent = Student(oldID, oldName)
        newStudent = Student(newID, newName)
        return self._repo.update(oldStudent, newStudent)

    def getRepo(self):
        """
        Returns the whole repository
        """
        return self._repo

    def clear(self):
        """
        Clears the repository
        """
        return self._repo.clear()

    def getStudentCount(self):
        """
        Returns how many students are in the repository
        """
        return len(self._repo)

    @staticmethod
    def functionByName(item1, item2):
        return item1.name > item2.name

    def sortStudents(self):
        return sorted(self._repo, self.functionByName)



