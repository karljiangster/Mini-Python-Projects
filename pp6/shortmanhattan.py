#!/usr/bin/python3

import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/shortmanhattan
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the find_paths() function.  Do not
# modify any other code.

# This function takes four parameters: x0, y0, x1, y1 (as defined
# in the problem statement)
#
# The function must return a list of all the shortest paths from (x0,y0) to
# (x1, y1). For example:
#
#    find_paths(0,0,1,1) would return [["right", "up"], ["up", "right"]]
#    find_paths(1,1,0,0) would return [["left", "down"], ["down", "left"]]
#
# Note: The order of the paths is not important. e.g., the first call could
#       return [["up", "right"], ["right", "up"]] and it would also be correct.
#
# Note (2): If there are no shortest paths (because you're finding the path from
#           one point to itself, the function must return [[]] (i.e., a list with
#           just one path: the empty path.
<<<<<<< HEAD
def find_paths(x0,y0,x1,y1, vert = "up ", hor = "right ", inc_vert = 1, inc_hor = 1):
    # your code goes here
    
    if y1 < y0: 
        inc_vert = -1
        vert = "down "
    if x1 < x0: 
        inc_hor = -1 
        hor = "left "

    if x0 == x1: 
        return [[vert] * (y1 - y0)]
    if y0 == y1: 
        return [[hor] * (x1 - x0)]

    paths = []

    ver_perms = find_paths(x0, y0 + inc_vert, x1, y1)
    hor_perms = find_paths(x0 + inc_hor, y0, x1, y1

    paths.extend( list( map( lambda s: [vert] + s, ver_perms ) ) )
    paths.extend( list( map( lambda s: [hor] + s, hor_perms ) ) )
    
    return paths
=======
def find_paths(x0,y0,x1,y1):
    # your code goes here
    return []
>>>>>>> 7d55802b2f6743c7ffa2502be0f3a062f47c2f81

if __name__ == "__main__":
    x0, y0, x1, y1 = sys.stdin.read().split()

    paths = find_paths(int(x0), int(y0), int(x1), int(y1))

    if len(paths) == 1 and len(paths[0]) == 0:
        print("NONE")
    else:
        for p in paths:
            print(" ".join(p))

    
