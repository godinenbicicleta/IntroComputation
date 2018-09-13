#Using exceptions

def sumDigits(s):
    """assumes s is a string and returns the sum of the
    decimal digits in s. For example if s is 'a2b3c' it returns 5"""
    suma = sum([int(c) for c in s if c in '0123456789'])
    return suma

print(sumDigits('a2b3c'))

#now using exceptions:
def sumaDigits(s):
    """assumes s is a string and returns the sum of the
    decimal digits in s. For example if s is 'a2b3c' it returns 5"""
    suma = 0
    for c in s:
        try:
            suma+=int(c)
        except ValueError:
            continue
    return suma

print(sumaDigits('a2b3c4d5e'))
