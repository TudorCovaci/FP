
from domain.Discipline import Discipline
from domain.Lab9Module import IterableDataType


class DisciplineRepo(IterableDataType):
    """
    Class for discipline repositories
    """


    def add(self, discipline):
        """
        Adds a discipline to the repository
        Input:
            - discipline - the discipline that needs to be added
        """
        self.append(discipline)

    def find(self, searchCrit):
        """
        Searches a discipline in the repository
        Input:
            - disciplineID - the id of the searched discipline
        Output:
            - the whole discipline object, if found
            - False - if the discipline was not found
        """
        try:
            searchCrit = int(searchCrit)
        except:
            searchCrit = searchCrit.title()
        if type(searchCrit) == int:
            if searchCrit < 0:
                raise ValueError("Error: Invalid id!")
            for discipline in self:
                if discipline.id == searchCrit:
                    return discipline
        elif type(searchCrit) == str:
            if searchCrit == "":
                raise ValueError("Error: Invalid name!")
            for discipline in self:
                if discipline.name == searchCrit:
                    return discipline
        return False

    def findAllDisciplines(self, disciplineName):
        """
        Finds all the disciplines whose name partially match
        """
        foundDisciplines = []
        for discipline in self._data:
            if discipline.partialMatch(disciplineName):
                foundDisciplines.append(discipline)
        return foundDisciplines

    def remove(self, disciSearch):
        """
        Removes a discipline from the repository
        Input:
            - disciplineID - the id of the discipline that needs to be removed
        """
        foundDiscipline = self.find(disciSearch)
        if foundDiscipline is False:
            raise ValueError("Error: Discipline not found!")
        self._data.remove(foundDiscipline)
        return foundDiscipline

    def update(self, oldDisciplineID, newDiscipline):
        """
        Updates an old discipline with a new one
        Input:
            - oldDiscipline - the discipline that needs to be updated
            - newDiscipline - the discipline that needs to be added to the repo in place of oldDiscipline
        """
        oldDiscipline = self.find(oldDisciplineID)
        if oldDiscipline is False:
            raise ValueError("Error: Old discipline not found!")
        newList = []
        for discipline in self._data:
            if discipline == oldDiscipline:
                newList.append(newDiscipline)
            else:
                newList.append(discipline)
        self._data = newList
        return True

    def clear(self):
        """
        Clears the repository
        """
        self._data.clear()
        return True

    def getAll(self):
        """
        Returns the whole repository
        """
        return self._data
