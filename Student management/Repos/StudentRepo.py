
from domain.Lab9Module import IterableDataType
from domain.Lab9Module import switch

class StudentRepo(IterableDataType):
    """
    Class for student repositories
    """


    def add(self, student):
        """
        Adds a student to the repository
        """
        self.append(student)
        return True

    def find(self, searchCrit):
        try:
            searchCrit = int(searchCrit)
        except:
            print(searchCrit)
            searchCrit = searchCrit.title()
        if type(searchCrit) == int:
            if searchCrit < 0:
                raise ValueError("Error: Invalid id!")
            for student in self:
                if student.id == searchCrit:
                    return student
        elif type(searchCrit) == str:
            if searchCrit == "":
                raise ValueError("Error: Invalid name!")
            for student in self:
                if student.name == searchCrit:
                    return student
        return False

    def update(self, oldStudent, newStudent):
        """
        Updates a student
        """
        self.remove(oldStudent.id)
        self.add(newStudent)
        return True

    def remove(self, studentID):
        """
        Removes a student from the repo.
        """
        student = self.find(studentID)
        if student is False:
            raise ValueError("Error: Student not found!")
        self.removeObj(student)
        return True

    def getData(self):
        return self._data






