# CS121 Lab 3: Functions

import math

def dist(point1, point2): 
    '''
    Takes in two points and returns 
    one value that is the distance between those 
    two points

    Inputs: 
        point1, point2: tuple of coordinates 
    returns:
        distance 
    '''

    xdist = point1[0] - point2[0]
    ydist = point1[0] - point2[0]

    return math.sqrt(xdist ** 2 + ydist ** 2)

def perimeter(point1, point2, point3):
    '''
    Returns perimeter of triangle formed by the three points
    '''

    return dist(point1, point2) + dist(point2, point3) + dist(point3, point1)


def go():
    '''
    Write a small amount of code to verify that your functions work

    Verify that the distance between the points (0, 1) and (1, 0) is
    close to math.sqrt(2)

    After that is done, verify that the triangle 
    with vertices at (0, 0), (0, 1), (1, 0) has 
    a perimeter 2 + math.sqrt(2)
    '''

    # replace the pass with code that calls your functions
    # and prints the results
    pass

if __name__ == "__main__":
    go()
    
                

