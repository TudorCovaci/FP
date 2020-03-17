from Repos.DisciplineRepo import DisciplineRepo
from domain.Discipline import Discipline


class DisciplineTextFileRepo(DisciplineRepo):

    def __init__(self, fileName="disciplines.txt"):
        DisciplineRepo.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def add(self, discipline):
        DisciplineRepo.add(self, discipline)
        self._saveFile()

    def remove(self,discipline):
        DisciplineRepo.remove(self, discipline)
        self._saveFile()

    def update(self, oldDisciplineID, newDiscipline):
        DisciplineRepo.update(self, oldDisciplineID, newDiscipline)
        self._saveFile()

    def clear(self):
        DisciplineRepo.clear(self)
        self._saveFile()

    def _saveFile(self):
        file = open(self._fileName, "w")
        for discipline in self.getAll():
            file.write(str(discipline.id) + "," + discipline.name + "\n")
        file.close()

    def _loadFile(self):
        try:
            file = open(self._fileName, "r")
            entry = file.readline()
            while len(entry) > 2:
                entryList = entry.split(',')
                DisciplineRepo.add(self, Discipline(int(entryList[0]), entryList[1][:-1]))
                entry = file.readline()
        except FileNotFoundError as fnfe:
            raise ValueError("Cannot open file " + str(fnfe))
        finally:
            file.close()

