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

    def __init__(sellf,name,classYear):
        MITPerson.__init__(self,name)
        self.year = classYear

    def getClass(self):
        return self.year


class Grad(Student):
    pass
