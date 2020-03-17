import pickle
from Repos.StudentRepo import StudentRepo


class StudentBinaryFileRepo(StudentRepo):
    def __init__(self, fileName="students.pickle"):
        StudentRepo.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def _saveFile(self):
        file = open(self._fileName, "wb")
        pickle.dump(StudentRepo.getAll(self), file)
        file.close()

    def remove(self, studentID):
        StudentRepo.remove(self, studentID)
        self._saveFile()

    def add(self, student):
        StudentRepo.add(self, student)
        self._saveFile()

    def update(self, oldStudent, newStudent):
        StudentRepo.update(self, oldStudent, newStudent)
        self._saveFile()

    def clear(self):
        StudentRepo.clear(self)
        self._saveFile()

    def _loadFile(self):

        try:
            file = open(self._fileName, "rb")
            result = pickle.load(file)
            for student in result:
                StudentRepo.add(self, student)
            file.close()
        except Exception:
            raise ValueError("Cannot open file!")
