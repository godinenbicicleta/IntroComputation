# Using functions as objects
# for example as arguments of other functions

def applyToEach( L , f ):
    """Assumes L is a list, f a function, 
    mutates L by replacing each element, e of L
    by f(e)"""
    for i,_ in enumerate(L):
        L[i] = f(L[i])
L = [1,-2,3.33]
print("L = ", L)
print("apply abs to each element of L")
applyToEach(L, abs)
print("L = ",L)

"""
map behaves like applyToEach but it can also
behave like a range function
"""
for i in map(abs,[-1,-2,-3]):
    print(i)
