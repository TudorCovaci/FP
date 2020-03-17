from domain.Student import Student


class StudentValidator:
    """
    This class is used to validate a student
    """
    def __init__(self, repo):
        self._repo = repo

    def validate(self, student):
        """
        Validates if the given student is valid
        Input:
            - client - the object that needs to be validated
        Output:
            - List of errors containing the errors that occurred.
              An empty error list means the object is valid.
        """
        if not isinstance(student, Student):
            raise TypeError("Error: student is not a Student-class type object!")
        errors = []
        try:
            student.id = int(student.id)
        except:
            raise ValueError("Error: Invalid id!")
        if student.id < 0:
            errors.append("Error: Invalid id!")
        elif self._repo.find(student.id) is not False:
            errors.append("Error: ID already exists!")
        if student.name == "":
            errors.append("Error: Invalid name!")
        if len(errors):
            raise ValueError(errors)
