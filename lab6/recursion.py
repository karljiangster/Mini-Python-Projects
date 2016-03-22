'''
Lab 6 code 
Jiang, Karl 
''' 

import math
from math import sin

def is_power_of_two(n): 
    if n == 2: 
        return True 
    if n % 2 != 0: 
        return False 
    else: 
        return is_power_of_two(n / 2)

#tests
'''
print(4, is_power_of_two(4))
print(3, is_power_of_two(3))
print(1024, is_power_of_two(1024))
'''

def fib(n): 
    if n == 0: 
        return 1
    if n == 1: 
        return 1 
    else: 
        return fib(n-1) + fib(n-2)

#tests 
n = 7
''' 
print(fib(n) == fib(n - 1) + fib(n-2))
'''

def find_root_sqrt2(epsilon, a, b): 
    c = (a + b)/2 
    if math.fabs(sqrt2(c)) < math.fabs(epsilon): 
        return c 
    elif sqrt2(c) > 0: 
        return find_root_sqrt2(epsilon, -sqrt2(c), a)
    elif sqrt2(c) < 0: 
        return find_root_sqrt2(epsilon, b, sqrt2(c))
    print("NOOOOO YOU SHOULDNT BE HEREEE YOU FAILED SMH")

def sqrt2(x): #root2 according to the lab 
    return x ** 2 - 2


def find_root(f, epsilon, a, b): 
    c = (a + b)/ 2
    if math.fabs(f(c)) < math.fabs(epsilon): 
        return c 
    elif f(c) > 0:
        return find_root(f, epsilon, -f(c), a)
    else: 
        return find_root(f, epsilon, b, f(c))

print(find_root(lambda x: x**2 - 2, 0.01, 0, 2))
print(find_root(lambda x: sin(x) - 0.5, 0.01, 0, 1))