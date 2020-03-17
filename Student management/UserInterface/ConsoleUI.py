from Controllers.UndoController import *


class ConsoleUI:
    """
    Class for console-based user interface
    """
    def __init__(self, studentController, disciplineController, gradeController,
                 statisticsController, undoController):
        self._studCtrl = studentController
        self._disciplineCtrl = disciplineController
        self._gradeCtrl = gradeController
        self._statistics = statisticsController
        self._undoCtrl = undoController

    def start(self):
        options = {'1': self.studentMenu, '2': self.disciMenu,
                   '3': self.statMenu, '4': self.undoUI,
                   '5': self.redoUI}


        while True:
            #try:
                self.printMenu()
                option = input("Please enter option: ")
                if option in options:
                    isOk = options[option]()
                    if isOk:
                        print("Operation successful!")
                    else:
                        print("Operation failed!")
                elif option == '0':
                    return 0
                else:
                    raise ValueError("Error: Invalid option!")


            #except Exception as errors:
                #if type(errors.args[0]) == list:
                    #self.printErrors(errors.args)
                #else:
                    #print(errors)


    def printMenu(self):
        print("1. Student operations")
        print("2. Discipline operations")
        print("3. Statistics")
        print("4. Undo")
        print("5. Redo")
        print("0. Exit")

    def undoUI(self):
        self._undoCtrl.undo()
        return True

    def redoUI(self):
        self._undoCtrl.redo()
        return True

    def studentMenu(self):
        studCommands = {'1': self.addStudUI, '2': self.removeStudUI, '3': self.updateStudUI,
                        '4': self.gradeStudUI, '5': self.displayGradesUI,
                        '6': self.searchStudUI, '7': self.displayStudUI, '8': self.sortStudentsUI}
        print("\n1. Add student")
        print("2. Remove student")
        print("3. Update tudent")
        print("4. Grade student")
        print("5. Display grades for student")
        print("6. Search for a student")
        print("7. Display students")
        print("8. Sort students by name (Gnome Sort)")
        command = input("Please enter option: ")
        if command in studCommands:
            return studCommands[command]()
        else:
            raise ValueError("Error: Invalid command!")

    def addStudUI(self):
        ID = input("Please input the id: ")
        name = input("Please input the name: ")
        self._studCtrl.create(ID, name)
        undoFunction = FunctionCall(self._studCtrl.remove, ID)
        redoFunction = FunctionCall(self._studCtrl.create, ID, name)
        undoCreate = Operation(undoFunction, redoFunction)
        self._undoCtrl.addOperation(undoCreate)
        return True

    def removeStudUI(self):
        studSearch = input("Please enter input the id/name: ")
        student = self._studCtrl.find(studSearch)
        if student is False:
            raise ValueError("Error: The student was not found!")
        self._studCtrl.remove(student.id)
        cascadeRemove = CascadeOperation()
        redoFunction = FunctionCall(self._studCtrl.remove, student.id)
        undoFunction = FunctionCall(self._studCtrl.create, student.id, student.name)
        undoRemove = Operation(undoFunction, redoFunction)
        cascadeRemove.add(undoRemove)
        listOfGrades = self._gradeCtrl.findAllGradesForStudent(student.id)
        for grade in listOfGrades:
            self._gradeCtrl.remove(grade)
            redoFunction = FunctionCall(self._gradeCtrl.remove, grade)
            undoFunction = FunctionCall(self._gradeCtrl.create, grade.studID, grade.disciID, grade.value)
            undoRemove = Operation(undoFunction, redoFunction)
            cascadeRemove.add(undoRemove)
        self._undoCtrl.addOperation(cascadeRemove)
        return True

    def gradeStudUI(self):
        studentInput = input("Please enter student id/name: ")
        student = self._studCtrl.find(studentInput)
        if student is False:
            raise ValueError("Error: Student not found!")
        disciplineInput = input("Please enter discipline id/name: ")
        discipline = self._disciplineCtrl.find(disciplineInput)
        if discipline is False:
            raise ValueError("Error: Discipline not found!")
        value = int(input("Please enter grade value: "))
        grade = self._gradeCtrl.create(student.id, discipline.id, value)
        undoFunction = FunctionCall(self._gradeCtrl.remove, grade)
        redoFunction = FunctionCall(self._gradeCtrl.create, student.id, discipline.id, value)
        undoGrade = Operation(undoFunction, redoFunction)
        self._undoCtrl.addOperation(undoGrade)
        return True

    def displayGradesUI(self):
        studSearch = input("Please enter student id/name: ")
        student = self._studCtrl.find(studSearch)
        if student is False:
            raise ValueError("Error: Student not found!")
        print("The grades are: ")
        listOfGrades = self._gradeCtrl.findAllGradesForStudent(student.id)
        for grade in listOfGrades:
            disciplineName = self._disciplineCtrl.find(grade.disciID).name
            print(str(grade.value) + " at " + disciplineName)

    def updateStudUI(self):
        ID = input("Please enter the id: ")
        name = input("Please enter the name: ")
        newId = input("Please enter the new id: ")
        newName = input("Please enter the new name: ")
        self._studCtrl.update(ID, name, newId, newName)
        listOfGrades = self._gradeCtrl.findAllGradesForStudent(ID)
        cascadeRemove = CascadeOperation()
        undoFunction = FunctionCall(self._studCtrl.remove, newId)
        redoFunction = FunctionCall(self._studCtrl.create, ID, name)
        undoRemove = Operation(undoFunction, redoFunction)
        cascadeRemove.add(undoRemove)
        for grade in listOfGrades:
            discID = grade.disciID
            value = grade.value
            self._gradeCtrl.remove(grade)
            newGrade = self._gradeCtrl.create(newId, discID, value)
            redoFunction = FunctionCall(self._gradeCtrl.create, newId, discID, value)
            undoFunction = FunctionCall(self._gradeCtrl.remove, newGrade)
            undoRemove = Operation(undoFunction, redoFunction)
            cascadeRemove.add(undoRemove)

        return True

    def searchStudUI(self):
        studSearch = input("Please enter the name: ")
        studSearch = studSearch.title()
        partialList = self._studCtrl.findPartial(studSearch)
        print("Partial matching results: ")
        for student in partialList:
            print(str(student))
        return True

    def displayStudUI(self):
        print(str(self._studCtrl))
        return True

    def sortStudentsUI(self):
        self._studCtrl.sortStudents(functionByName)
        print(str(self._studCtrl))
        return True

    def disciMenu(self):
        disciCommands = {'1': self.addDisciUI, '2': self.removeDisciUI, '3': self.updateDisciUI,
                         '4': self.displayDisciUI, '5': self.searchDisciUI}
        print("\n1. Add discipline")
        print("2. Remove discipline")
        print("3. Update discipline")
        print("4. Display disciplines")
        print("5. Search discipline (partial matching)")
        command = input("Please enter option: ")
        if command in disciCommands:
            return disciCommands[command]()
        else:
            raise ValueError("Error: Invalid command!")

    def addDisciUI(self):
        ID = input("Plesae enter the id: ")
        name = input("please enter the name: ")
        self._disciplineCtrl.create(ID, name)
        undoFunction = FunctionCall(self._disciplineCtrl.remove, ID)
        redoFunction = FunctionCall(self._disciplineCtrl.create, ID, name)
        undoCreate = Operation(undoFunction, redoFunction)
        self._undoCtrl.addOperation(undoCreate)
        return True

    def removeDisciUI(self):
        disciSearch = input("Please enter the id/name: ")
        discipline = self._disciplineCtrl.remove(disciSearch)
        cascadeRemove = CascadeOperation()
        redoFunction = FunctionCall(self._studCtrl.remove, discipline.id)
        undoFunction = FunctionCall(self._studCtrl.create, discipline.id, discipline.name)
        undoRemove = Operation(undoFunction, redoFunction)
        cascadeRemove.add(undoRemove)
        listOfGrades = self._gradeCtrl.findAllGradesForDiscipline(discipline.id)
        for grade in listOfGrades:
            self._gradeCtrl.remove(grade)
            redoFunction = FunctionCall(self._gradeCtrl.remove, grade)
            undoFunction = FunctionCall(self._gradeCtrl.create, grade.studID, grade.disciID, grade.value)
            undoRemove = Operation(undoFunction, redoFunction)
            cascadeRemove.add(undoRemove)
        return True

    def updateDisciUI(self):
        oldDisciplineID = input("Please input the id of current discipline: ")
        newID = input("Please enter the new ID: ")
        newName = input("Please enter the new name: ")
        self._disciplineCtrl.update(oldDisciplineID, newID, newName)
        cascadeUpdate = CascadeOperation()
        undoFunction = FunctionCall(self._studCtrl.remove, oldDisciplineID)
        redoFunction = FunctionCall(self._studCtrl.create, newID, newName)
        undoUpdate = Operation(undoFunction, redoFunction)
        cascadeUpdate.add(undoUpdate)
        listOfGrades = self._gradeCtrl.findAllGradesForStudent(oldDisciplineID)
        for grade in listOfGrades:
            studID = grade.studID
            value = grade.value
            self._gradeCtrl.remove(grade)
            newGrade = self._gradeCtrl.create(studID, newID, value)
            redoFunction = FunctionCall(self._gradeCtrl.create, studID, newID, value)
            undoFunction = FunctionCall(self._gradeCtrl.remove, newGrade)
            undoRemove = Operation(undoFunction, redoFunction)
            cascadeUpdate.add(undoRemove)
        return True

    def displayDisciUI(self):
        print(str(self._disciplineCtrl))
        return True

    def searchDisciUI(self):
        disciSearch = input("Please enter the name: ")
        disciSearch = disciSearch.title()
        partialList = self._disciplineCtrl.findPartial(disciSearch)
        print("Partial matching results: ")
        for disci in partialList:
            print(str(disci))
        return True

    def statMenu(self):
        statCommands = {'1': self.enrolledAtDisciUI, '2': self.failingStudentsUI,
                        '3': self.bestSituationUI, '4': self.activeDisciplinesUI}
        print("\n1. Display enrolled students at a given disciplines")
        print("2. Display failing students")
        print("3. Display students with best situation")
        print("4. Display active disciplines")
        command = input("Please enter option: ")
        if command in statCommands:
            return statCommands[command]()
        else:
            raise ValueError("Error: Invalid command!")

    def enrolledAtDisciUI(self):
        disciSearch = input("Please input id/name: ")
        listOfEnrolledStudents = self._statistics.studentsEnrolledAtDiscipline(disciSearch)
        print("Students enrolled at the given discipline are: ")
        for student in listOfEnrolledStudents:
            print(str(student))
        return True

    def failingStudentsUI(self):
        print("The failing students are: ")
        listOfFailingStudents = self._statistics.failingStudents()
        for studentStruct in listOfFailingStudents:
            print(str(studentStruct[0]) + "\t%10.2f" % studentStruct[1])
        return True

    def bestSituationUI(self):
        print("The ranking of the students is: ")
        ranking = self._statistics.bestSchoolSituation()
        for student in ranking:
            print(str(student[0]) + "\t%10.2f" % student[1])
        return True

    def activeDisciplinesUI(self):
        print("The active disciplines are: ")
        activeDisciplines = self._statistics.activeDisciplines()
        for disciplineGroup in activeDisciplines:
            print(str(disciplineGroup[0]) + "\t%10.2f" % disciplineGroup[1])
        return True

    def printErrors(self, errors):
        errorList = list(errors)
        errorListt = errorList
        for error in errorListt[0]:
            print(error)
        return True
