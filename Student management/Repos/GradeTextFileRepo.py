from Repos.GradeRepo import GradeRepo
from domain.Grade import Grade


class GradeTextFileRepo(GradeRepo):

    def __init__(self, fileName="grades.txt"):
        GradeRepo.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def add(self, grade):
        GradeRepo.add(self, grade)
        self._saveFile()

    def remove(self, grade):
        GradeRepo.remove(self, grade)
        self._saveFile()

    def clear(self):
        GradeRepo.clear(self)
        self._saveFile()

    def _saveFile(self):
        file = open(self._fileName, "w")
        for grade in self.getAll():
            file.write(str(grade.studID) + "," + str(grade.disciID) + "," + str(grade.value) + "\n")
        file.close()

    def _loadFile(self):
        try:
            file = open(self._fileName, "r")
            entry = file.readline()
            while len(entry) > 2:
                entryList = entry.split(',')
                GradeRepo.add(self, Grade(int(entryList[0]), entryList[1], entryList[2][:-1]))
                entry = file.readline()
        except FileNotFoundError as fnfe:
            raise ValueError("Cannot open file " + str(fnfe))
        finally:
            file.close()

