from domain.Grade import Grade
from Repos.StudentRepo import StudentRepo


class GradeValidator:

    def __init__(self, studentRepo, disciplineRepo):
        if not isinstance(studentRepo, StudentRepo):
            raise TypeError("Error: Invalid repos!")
        self._studentRepo = studentRepo
        self._disciplineRepo = disciplineRepo

    def validate(self, grade):
        if not isinstance(grade, Grade):
            raise TypeError("Error: Not a grade!")
        errors = []
        if grade.studID < 0 or self._studentRepo.find(grade.studID) is False:
            errors.append("Error: Invalid Student id!")
        if grade.disciID < 0 or self._disciplineRepo.find(grade.disciID) is False:
            errors.append("Error: Invalid Discipline id!")
        if grade.value < 0 or grade.value > 10:
            errors.append("Error: Invalid grade value!")
        if len(errors):
            raise ValueError(errors)
