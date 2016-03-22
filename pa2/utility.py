#  CS121:: Schelling Model of Housing Segregation
#
#  Utility code for managing grids.
#
#  Anne Rogers
#  Summer 2015


import csv
import os
import sys
import schelling

def check_row(N, row, i):
    '''
    Check the format of ith row.
    '''
    if len(row) != N:
        print("Format error in line {}: row is wrong length".format(i))
        sys.exit(0)
    if set(row) - set(("R", "B", "O")) != set():
        print("Format error in line {}: row has character other than R/B/O".format(i))
        sys.exit(0)


def read_grid(filename, strip_Us=True):
    '''
    Read a grid from a text file and return the corresponding
    in-memory representation.

    filename: the name of the grid file to read

    returns: the grid contained in the specified file.
    '''

    if not os.path.isfile(filename):
        print("Bad file name:" + filename)
        sys.exit(0)


    with open(filename) as f:
        reader = csv.reader(f, delimiter = " ")
        grid = []
        i = 0
        for row in reader:
            if i == 0 and len(row) == 1:
                # old format with N in the file
                continue
            if strip_Us:
                # remove indications of unsatisfied homeowners if necessary
                row = [(x[1:] if len(x) > 0 and x[0] == "U" else x).strip() for x in row]
            if i == 0:
                N = len(row)
            check_row(N, row, i)
            grid.append(row)
            i = i + 1

        if len(grid) == 0:
            print("File is empty")
            sys.exit(0)

        return grid


def first_difference(grid0, grid1):
    '''
    Returns the first location where grid0 and grid1 differ.

    Returns None, if the two grids are the same.
    '''
    if grid0 == grid1:
        return None

    for i in range(len(grid0)):
        for j in range(len(grid1)):
            if grid0[i][j] != grid1[i][j]:
                return (i, j)
    
    return None


def print_grid(grid):
    '''
    Print a text representation of a grid. 
    '''
    print(len(grid))
    for row in grid:
        print(row)


