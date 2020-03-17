

class Student:
    """
    Class for student-type objects
    """
    def __init__(self, id_, name):
        """
        Constructor for Student class
        """
        self._id = id_

        self._name = name
        self._name = self._name.title()

    def __eq__(self, student):
        """
        Redefines the equality of two students
        """
        return self._name == student.name and self._id == student.id

    def __str__(self):
        """
        String format of a student
        """
        return "%-10s" % self._id + "%-20s" % self._name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @id.setter
    def id(self, id_):
        self._id = id_

    @name.setter
    def name(self, name):
        self._name = name

    def partialMatch(self, studentName):
        """
        Partial string matching for student names
        """
        if studentName.lower() in self._name.lower():
            return True
        return False

