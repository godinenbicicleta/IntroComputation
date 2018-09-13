def findAnEven(L):
    """assumes L is a list of integers
    returns the first even number in L
    Raises ValueError if L does ont contain an even number"""
    for k in L:
        if k % 2 == 0 and k>0:
            return k
            break
    raise ValueError('no even numbers provided')
