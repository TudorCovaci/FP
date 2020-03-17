from Repos.StudentRepo import StudentRepo
from domain.Student import Student


class StudentTextFileRepo(StudentRepo):

    def __init__(self, fileName = "students.txt"):
        StudentRepo.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def add(self, student):
        StudentRepo.add(self, student)
        self._saveFile()

    def remove(self, studentID):
        StudentRepo.remove(self, studentID)
        self._saveFile()

    def update(self, oldStudent, newStudent):
        StudentRepo.update(self, oldStudent, newStudent)
        self._saveFile()

    def clear(self):
        StudentRepo.clear(self)
        self._saveFile()

    def _saveFile(self):
        file = open(self._fileName, "w")
        for student in self.getAll():
            file.write(str(student.id) + "," + student.name + "\n")
        file.close()

    def _loadFile(self):
        file = open(self._fileName, "r")
        entry = file.readline()
        try:
            while len(entry) > 2:
                entryList = entry.split(',')
                StudentRepo.add(self, Student(int(entryList[0]), entryList[1][:-1]))
                entry = file.readline()
        except FileNotFoundError as fnfe:
            raise ValueError("Cannot open file " + str(fnfe))
        finally:
            file.close()

