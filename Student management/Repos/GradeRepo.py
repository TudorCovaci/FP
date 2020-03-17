

class GradeRepo:
    """
    Class for grade repositories
    """
    def __init__(self):
        """
        Constructor
        """
        self._data = []

    def __len__(self):
        """
        Returns the length of the repository
        """
        return len(self._data)

    def __str__(self):
        """
        String format of repository
        """
        string = ""
        for grade in self._data:
            string = string + str(grade) + "\n"
        return string

    def add(self, grade):
        """
        Adds a grade to the repoistory
        """
        self._data.append(grade)

    def remove(self, grade):
        """
        Removes a grade from repoistory
        """
        self._data.remove(grade)
        return True

    def getAll(self):
        """
        Returns the data
        """
        return self._data

    def findAllGradesForStudent(self, studID):
        """
        Returns the list of student's grades
        """
        listOfGrades = []
        for grade in self._data:
            if grade.studID == studID:
                listOfGrades.append(grade)
        return listOfGrades

    def clear(self):
        """
        Clears the repository
        """
        return self._data.clear()

    def findAllGradesForDiscipline(self, disciplineID):
        """
        Return the list of the grades at the given discipline
        """
        listOfGrades = []
        for grade in self._data:
            if grade.disciID == disciplineID:
                listOfGrades.append(grade)
        return listOfGrades
