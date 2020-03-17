import pickle
from Repos.DisciplineRepo import DisciplineRepo


class DisciplineBinaryFileRepo(DisciplineRepo):
    def __init__(self, fileName="disciplines.pickle"):
        DisciplineRepo.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def _saveFile(self):
        file = open(self._fileName, "wb")
        pickle.dump(DisciplineRepo.getAll(self), file)
        file.close()

    def remove(self, disciplineID):
        DisciplineRepo.remove(self, disciplineID)
        self._saveFile()

    def add(self, student):
        DisciplineRepo.add(self, student)
        self._saveFile()

    def update(self, oldDisciplineID, newDiscipline):
        DisciplineRepo.update(self, oldDisciplineID, newDiscipline)
        self._saveFile()

    def clear(self):
        DisciplineRepo.clear(self)
        self._saveFile()

    def _loadFile(self):

        try:
            file = open(self._fileName, "rb")
            result = pickle.load(file)
            for student in result:
                DisciplineRepo.add(self, student)
            file.close()
        except Exception:
            raise ValueError("Cannot open file!")
