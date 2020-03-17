

class Discipline:
    """
    Class for discipline-type objects
    """
    def __init__(self, id_, name):
        """
        Constructor for Discipline Class
        """
        self._id = id_
        self._name = name
        self._name = self._name.title()

    def __str__(self):
        """
        String type of a discipline
        """
        return "%-10s" % self._id + "%-20s" % self._name

    def __eq__(self, discipline):
        """
        Redefines the equality for 2 disciplines
        """
        return self._id == discipline.id and self._name == discipline.name

    def partialMatch(self, disciplineName):
        """
        Partial string matching for discipline names
        """

        return disciplineName.lower() in self._name.lower()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @id.setter
    def id(self, id_):
        self._id = id_


