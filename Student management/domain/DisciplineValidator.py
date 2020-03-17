from domain.Discipline import Discipline


class DisciplineValidator:

    def __init__(self, repo):
        self._repo = repo

    def validate(self, discipline):
        if not isinstance(discipline, Discipline):
            raise TypeError("Error: Not an instance of Discipline class!")
        errors = []
        try:
            discipline.id = int(discipline.id)
        except:
            raise ValueError("Error: Invalid id!")
        if discipline.id < 0 or self._repo.find(discipline.id) is not False:
            errors.append("Error: Invalid ID!")
        if discipline.name == "":
            errors.append("Error: Invalid name!")
        if len(errors):
            raise ValueError(errors)
        return True
