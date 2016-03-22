#!/usr/bin/python

# Skeleton code for problem https://uchicago.kattis.com/problems/uchicago%3Ampcs%3Agcd
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the gcd function.
# Do not modify any other code.

# This function takes a pair of floats and returns their greatest
# common denominator.

import sys

def gcd(a,b):
    # replace 1 with an appropriate return value
    return 1

### The following code handles the input and output tasks for
### this problem.  Do not modify it!

tokens = sys.stdin.read().split()

a = int(tokens[0])
b = int(tokens[1])

print(gcd(a, b))

