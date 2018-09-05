# some useful string methods in python:
s = 'hola bruno como estas - '
print('s = ',s)

# counts how many times s1 occurs in s
print('s.count("o") = ',s.count('o'))

# returns index of first occurrence
print('s.find("o") = ', s.find('o'))

# same as find but from the right
print('s.rfind("o") = ', s.rfind('o'))

#
print('s.lower() = ', s.lower())

print('s.replace("o","a") = ', s.replace('o','a'))

#removes trailing white space
print('s.strip() = ', s.strip())

# splits
print('s.split("-") = ', s.split("-"))

