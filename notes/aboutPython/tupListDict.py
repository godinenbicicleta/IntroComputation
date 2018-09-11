#----------------------------
#        TUPLES
#----------------------------
"""

Parenthesis are used to group expressions. That means:
(1) is just 1
(1,) is a tuple containing just one element

"""
#Example: Append a single element to a tuple

def intersect(t1,t2):
    """Assumes t1 and t2 are tuples
    Returns a tuple containing the elements that area in 
    both t1 and t2"""
    result = ()
    for element in t1:
        if element in t2:
            result += (element,)
    return result


#------------------------------
# LISTS
#------------------------------

#useful operations:
l = []
l1=[]
e = [1]
l.append(e) # adds e to the end of l
l.count(e) # counts occurrences of e in l
l.insert(i,e) # inserts e into l at index i
l.extend(l1) #adds  elements of list l1 to the end of l
l.index(e) # returns index of first occurence of e in l
           # exception if e not in l
l.pop(i) # removes and returns the item at index i in l
         # raises exception if l is empty
         # if i is ommited it defaults to -1, to remove
         # and return the last element of l
l.sort() # sorts elements of l in ascending order
l.reverse() #reverses the order of elements in l
