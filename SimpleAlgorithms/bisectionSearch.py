# -*- coding: utf-8 -*-
# find and approximation for the square root of 25 using Exhaustive enumeration
x=25
epsilon = 0.01
step = epsilon**3
numGuesses = 0
ans = 0.0

while abs( ans**2 - x ) >= epsilon and ans*ans <= x:
    ans += step
    numGuesses += 1

print(f'Number of guesses = {numGuesses}')

if abs( ans**2 -x ) >= epsilon:
    print(f'Failed to find the square root of {x}')
else:
    print(f'the square root of {x} is  approximately {ans}')

#bisection search

x = 25
epsilon = 0.01
numGuesses = 0
low = 0
high = max(1.0,x)
ans = (high + low)/2.0



while abs( ans**2 -x ) >= epsilon:
    print('low: ',low, 'high: ', high, 'ans:' ,ans, 'pwr', ans**2)
    numGuesses +=1
    if ans**2 < abs(x):
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

print('number of guesses: ', numGuesses)
print(ans, 'is close to square root of', x)




# cube root of positive and negative numbers

x = 27
epsilon = 0.01
numGuesses = 0
low = min(0,x)
high = max(1.0,x)
ans = (high + low)/2.0

"""
x = -27
low = -27
high = 1
ans = 13
high = 13

ans = -7
low = -7
high = 13
ans = 6
ans = 0.5
-3.25
"""

while abs( ans**3 -x ) >= epsilon:
    print('low: ',low, 'high: ', high, 'ans:' ,ans, 'pwr', ans**2)
    numGuesses +=1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

print('number of guesses: ', numGuesses)
print(ans, 'is close to square root of', x)
