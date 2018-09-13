# implementation of a set of integers abstraction called IntSet

class IntSet(object):
    """an IntSet is a set of integers""" #describes the abstraction
    #information about the implementation:
    #value if the set is represented as a list of ints, self.vals
    #each int in the set occurs in self.vals exactly once

    def __init__(self):
        """create an empty set of integers"""
        self.vals = []

    def insert(self,e):
        """assumes e is an integer and inserts e into self"""
        if e not in self.vals:
            self.vals.append(e)

    def member(self,e):
        """returns true if e is in self, and false otherwise"""
        return e in self.vals

    def remove(self,e):
        """Assumes e is an integer and removes e from self
        raises ValueError if e not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e)+' not found')

    def getMembers(self):
        """Returns a list containing the elements of self"""
        return self.vals[:]

    def __str__(self):
        """returns a string representation of self"""
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] +'}' #-1 ommits last comma
