

class Grade:
    """
    Class for grade-type objects
    """
    def __init__(self, stud_id, disci_id, value):
        """
        Constructor for Grade class
        """
        self._studID = int(stud_id)
        self._disciID = int(disci_id)
        self._value = int(value)

    def __str__(self):
        string = ""
        string += "Student ID: %d\t" % self.studID
        string += "Discipline ID: %d\t" % self.disciID
        string += "Grade: %d\n" % self.value
        return string

    def __eq__(self, grade):
        """
        Redefines the equality for 2 grades
        """
        return self._studID == grade.studID and self._disciID == grade.disciID and self._value == grade.value

    @property
    def studID(self):
        return self._studID

    @property
    def disciID(self):
        return self._disciID

    @property
    def value(self):
        return self._value
