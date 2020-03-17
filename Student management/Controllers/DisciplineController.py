
from domain.Discipline import Discipline


class DisciplineController:
    """
    Class for discipline controllers
    """
    def __init__(self, repo, validator):
        self._repo = repo
        self._validator = validator

    def initDisciplines(self):
        """
        Initializes the discipline data base
        """
        self.create(1, "math")
        self.create(2, "physics")
        self.create(3, "geography")
        self.create(4, "biology")
        self.create(5, "music")
        self.create(6, "physical education")
        self.create(7, "history")
        self.create(8, "computer science")
        self.create(9, "english")
        self.create(10, "french")
        return True

    def getDisciplineCount(self):
        """
        Returns the length of the database
        """
        return len(self._repo)

    def __str__(self):
        """
        String format of the repository
        """
        return str(self._repo)

    def create(self, disciplineID, disciplineName):
        """
        Creates, validates and adds a new discipline to the discipline repository
        Input:
            - disciplineID - integer, discipline's id
            - disciplineName - string, discipline's name
        """
        discipline = Discipline(disciplineID, disciplineName)
        self._validator.validate(discipline)
        self._repo.add(discipline)
        return True

    def remove(self, disciSearch):
        """
        Removes a discipline from the repository
        """
        return self._repo.remove(disciSearch)

    def update(self, oldDisciplineID, newID, newName):
        """
        Updates the discipline with oldDisciplineID to newDiscipline
        """
        newDiscipline = Discipline(newID, newName)
        self._validator.validate(newDiscipline)
        return self._repo.update(oldDisciplineID, newDiscipline)



    def find(self, disciplineID):
        """
        Finds the discipline with disciplineID in repository
        """
        return self._repo.find(disciplineID)

    def findPartial(self, disciplineName):
        """
        Finds all disciplines that partially match
        """
        return self._repo.findAllDisciplines(disciplineName)

    def clear(self):
        """
        Clears the repository
        """
        self._repo.clear()
        return True

    def getRepo(self):
        """
        Returns the repository
        """
        return self._repo.getAll()
