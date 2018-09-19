import datetime

class Person(object):

    def __init__(self,name):
        """create a person"""
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthDay = None

    def getName(self):
        """returns self's name"""
        return self.name

    def getLastName(self):
        """returns self's last name"""
        return self.lastName

    def setBirthday(self, birthdate):
        """assumes birthdate is of type datetime.date
        sets self's birthday to birthdate"""
        self.birthday = birthdate

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError('birthdate not defined')
        return (datetime.date.today()-self.birthday).days

    def __lt__(self,other):
        """returns True if self precedes other in alphabetical
        order, False otherwise. Comparison is based on last names,
        but if these are the same, full names are compared"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """returns sef's name"""
        return self.name



class MITPerson(Person):
    
    nextIdNum = 0 #identification number

    def __init__(self,name):
        Person.__init__(self,name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self,other):
        return self.idNum < other.idNum


class Student(MITPerson):
    pass


class UG(Student):

    def __init__(self,name,classYear):
        MITPerson.__init__(self,name)
        self.year = classYear

    def getClass(self):
        return self.year


class Grad(Student):
    pass


class TransferStudent(Student):
    
    def __init__(self, name, fromSchool):
        MITPerson.__init__(self,name)
        self.fromSchool = fromSchool

    def getOldSchool(self):
        return self.fromSchool

class Grades(object):
    
    def __init__(self):
        """create empty grade book"""
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """Assumes: student is of type Student
        add student to grade book"""
        if student in self.students:
            raise ValueError('Duplicate Student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """assumes grade is a float
        add grade to list of grades of student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def getGrades(self, student):
        """return a list of grades for student"""
        try: #return copy of list of students grades
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('student not in maping')

    def getStudents(self):
        """return sorted list of students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] # return copy of list of students



def gradeReport(course):
    """Assumes course is of type Grades"""
    report = ''
    for s in course.getStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report = report +'\n'\
                    +str(s) +'\'s mean grade is ' + str(average)
        except ZeroDivisionError:
            report = report+'\n'\
                + str(s) + ' has no grades'
    return report

ug1 = UG('Jane Doe', '2014')
ug2 = UG('John Doe', '2015')
ug3 = UG('David Henry', '2003')
g1 = Grad('Billi Buckner')
g2 = Grad('Bucky F. Dent')

sixHundred = Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)

for s in sixHundred.getStudents():
    sixHundred.addGrade(s,75)


sixHundred.addGrade(g1,25)
sixHundred.addGrade(g1,100)
sixHundred.addStudent(ug3)

print(gradeReport(sixHundred))
