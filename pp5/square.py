#!/usr/bin/python

#!/usr/bin/python

# Skeleton code for problem https://uchicago.kattis.com/problems/uchicago%3Ampcs%3Asquare
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the square function.
# Do not modify any other code.

# This function takes a pair of integers x and y and returns x raised
# to the power y.  
#
# Your solution must be recursive!


import sys

def exp(x,n):
    # replace the 1 with an appropriate return value
    return 1


### The following code handles the input and output tasks for
### this problem.  Do not modify it!

tokens = sys.stdin.read().split()

x = int(tokens[0])
n = int(tokens[1])

print(exp(x, n))

