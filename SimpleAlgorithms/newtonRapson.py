# -*- coding: utf-8 -*-
"""
Find an approximation to the square root of 25 using newton rapson method

Newton proved that if a value: guess is an approximation to a root of a
polynomial, then guess-p(guess)/p'(guess) is a better approximation

for square roots:
    x*x - k = 0
    take a guess... then:
    better_guess = guess -(guess**2-k)/(2*guess)
"""
# find square root of k
epsilon = 0.01
k = 25.0
numGuesses = 0
guess = k/2.0
while abs( guess**2-k) >= epsilon:
    guess = guess -(guess**2-k)/(2*guess)
    numGuesses+=1

print('square root of ',k, ' is: ', guess)
print('number of guesses: ', numGuesses)


# Compare newton vs bisection vs Exhaustive enumeration

#newton:
epsilon = 0.01
k = int(input("Enter an integer: "))
numGuesses = 0
guess = k/2.0
while abs( guess**2-k) >= epsilon:
    guess = guess -(guess**2-k)/(2*guess)
    numGuesses+=1


print('Newton number of guesses: ', numGuesses)

"""
#Exhaustive
numGuesses = 0
ans = 0.0
step = epsilon**2
while abs( ans**2 - k ) >= epsilon and ans*ans <= k:
    ans += step
    numGuesses += 1


print(f'Exhaustive Number of guesses = {numGuesses}')
"""

#bisection
numGuesses = 0
low = 0
high = max(1.0,k)
ans = (high + low)/2.0
while abs( ans**2 -k ) >= epsilon:
    numGuesses +=1
    if ans**2 < abs(k):
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0


print('bisection number of guesses: ', numGuesses)
