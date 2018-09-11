# -*- coding: utf-8 -*-

# find the cube root of a perfect cube

x = int(input('Enter an integer: '))
ans = 0

while ans**3 - abs(x) < 0:   #this is de decrementing function
    ans = ans + 1

if ans**3 != abs(x):
    print( x, 'is not a perfect cube')
else:
    if x < 0:
        ans *=-1
    print( f'Cube root of {x} is {ans}')

# find root and pwr such that root**pwr is equal to the integer provided

x = int(input('Enter an integer: '))

messages = []

for pwr in range(2,6):
    root = 0
    while root**pwr - abs(x) < 0:
        root+=1
    if root**pwr == abs(x):
        if x<0:
            ans*=-1
        messages.append(f'{root} to the {pwr} = {x}')
if len(messages) == 0:
    print(f'No 1<pwr<6 and root exist such that pwr**root equals {x}')
else:
    for message in messages:
        print(message)

# Exhaustive enumeration using a for loop
x = int(input('Enter an integer: '))

for ans in range(0, abs(x)+1):
    if ans**3>= abs(x):
        break
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x<0:
        ans = -ans
    print(ans, 'is the cube root of', x)
