import pickle
from Repos.GradeRepo import GradeRepo


class GradeBinaryFileRepo(GradeRepo):
    def __init__(self, fileName="grades.pickle"):
        GradeRepo.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def _saveFile(self):
        file = open(self._fileName, "wb")
        pickle.dump(GradeRepo.getAll(self), file)
        file.close()

    def add(self, grade):
        GradeRepo.add(self, grade)
        self._saveFile()

    def remove(self, grade):
        GradeRepo.remove(self, grade)
        self._saveFile()

    def clear(self):
        GradeRepo.clear(self)
        self._saveFile()

    def _loadFile(self):

        try:
            file = open(self._fileName, "rb")
            result = pickle.load(file)
            for grade in result:
                GradeRepo.add(self, grade)
            file.close()
        except Exception:
            raise ValueError("Cannot open file!")
