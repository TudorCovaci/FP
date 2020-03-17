from domain.Lab9Module import filter
from domain.Lab9Module import sorted

from domain.Lab9Module import sorted


class StatisticsController:
    """
    Class used for statistics
    """
    def __init__(self, studController, disciController, gradeController):
        self._studControl = studController
        self._disciControl = disciController
        self._gradeControl = gradeController

    def studentsEnrolledAtDiscipline(self, disciSearch):
        """
        Finds students enrolled at a given discipline
        """
        discipline = self._disciControl.find(disciSearch)
        listOfEnrolledStudents = []
        if discipline is False:
            raise ValueError("Error: The discipline was not found!")
        listOfGrades = self._gradeControl.findAllGradesForDiscipline(discipline.id)
        for grade in listOfGrades:
            student = self._studControl.find(grade.studID)
            if student not in listOfEnrolledStudents:
                listOfEnrolledStudents.append(student)
        return listOfEnrolledStudents

    def computeAverage(self, studentID, disciplineID):
        """
        Computes the average grade of a student at a discipline
        """
        listOfGrades = self._gradeControl.findAllGradesForStudent(studentID)
        sumOfGrades = 0
        count = 0
        for grade in listOfGrades:
            if grade.disciID == disciplineID:
                sumOfGrades += grade.value
                count += 1
        if count:
            return sumOfGrades / count
        return -1

    def isFailing(self, studentID):
        """
        Checks if a student is failing at one or more disciplines.
        """
        averageGrade = 0
        for discipline in self._disciControl.getRepo():
            averageGrade = self.computeAverage(studentID, discipline.id)
            if averageGrade != -1 and averageGrade < 5:
                return [True, averageGrade]
        return [False, averageGrade]

    def failingStudents(self):
        """
        Generates the list of failing students
        """
        listOfFailingStudents = []
        for student in self._studControl.getRepo():
            studentStruct = self.isFailing(student.id)
            if studentStruct[0]:
                listOfFailingStudents.append([student, studentStruct[1]])
        return listOfFailingStudents

    def bestSchoolSituation(self):

        rankList = filter(self._studControl.getRepo(), self.contFunction, self.studStructure)
        sorted(rankList, self.cmpFunction)
        return rankList

    def computeDisciplineAverage(self, disciplineID, studentID):
        """
        Compute the average grade at a discipline
        """
        listOfGrades = self._gradeControl.findAllGradesForDiscipline(disciplineID)
        sumOfGrades = 0
        count = 0
        for grade in listOfGrades:
            if grade.studID == studentID:
                sumOfGrades += grade.value
                count += 1
        if count:
            return sumOfGrades / count
        return -1

    def activeDisciplines(self):
        disciplineRank = []
        for discipline in self._disciControl.getRepo():
            aggAverageGrade = 0
            studentCount = 0
            for student in self._studControl.getRepo():
                averageGrade = self.computeDisciplineAverage(discipline.id, student.id)
                if averageGrade != -1:
                    aggAverageGrade += averageGrade
                    studentCount += 1
            if studentCount:
                aggAverageGrade = aggAverageGrade / studentCount
                disciplineRank.append([discipline, aggAverageGrade])
        disciplineRank.sort(key=lambda x: x[1], reverse=True)
        return disciplineRank

    def contFunction(self, student):

        aggAverageGrade = 0
        disciCount = 0
        for discipline in self._disciControl.getRepo():
            averageGrade = self.computeAverage(student.id, discipline.id)
            if averageGrade != -1:
                aggAverageGrade += averageGrade
                disciCount += 1
        if disciCount:
            aggAverageGrade = aggAverageGrade / disciCount
            studList = self.studStructure(student, aggAverageGrade)
            return studList
        return 0

    def studStructure(self, student, avgGrade):
        return [student, avgGrade]

    def cmpFunction(self, stddStruct1, stddStruct2):
        return stddStruct1[1] < stddStruct2[1]
