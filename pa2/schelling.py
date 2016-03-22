#   CS121: Schelling Model of Housing Segregation
#
#   Karl Jiang

#  CS121: Schelling Model of Housing Segregation
#
#   Program for simulating of a variant of Schelling's model of
#   housing segregation.  This program takes four parameters:
#    
#    filename -- name of a file containing a sample grid
#
#    R - The radius of the neighborhood: home (i, j) is in the
#        neighborhood of home (k,l) if |k-i| + |l-j| <= R.
#
#    threshold - minimum acceptable threshold for ratio of neighbor
#    value to the total number of homes in his neighborhood.
#
#    max_steps - the maximum number of passes to make over the
#    neighborhood during a simulation.
#
#  Sample use:python schelling.py tests/grid4.txt 1 0.51 3
#

import os
import sys
import utility
import math

def compute_neighborhood(grid, R, location): 
    '''
    Returns the colors of all the neighbors in a 
    given location within R. 

    grid: the grid
    R: radius for the neighborhood
    location: the coordinate of the specified location 
    on the grid. 

    returns: list of neightbors' color 
    '''
    neighborhood = []

    for x in range(location[0] - R, location[0] + R + 1):
        r = R - int(math.fabs(x - location[0])) #adjust for y values
        for y in range(location[1] - r, location[1] + r + 1):
            if within_grid(grid, (x, y)):
                neighborhood.append(grid[x][y]) 

    return neighborhood


def is_satisfied(grid, R, threshold, location, 
    theoretical_homeowner = "N/A"):

def is_satisfied(grid, R, threshold, location):
    ''' 
    Is the homeowner at the specified location satisfied?

    Inputs: 
        grid: the grid
        R: radius for the neighborhood
        threshold: satisfaction threshold
        location: a grid location
        theoretical_homeowner: used if user wants to test if 
        a homeowner will be satisfied if he/she were to be 
        theoretically placed in input "location" 
       
    Returns: 
<<<<<<< HEAD

        True, if the location's neighbor score is at or ab
        the threshold
=======
        True, if the location's satisfaction score is at or 
        above the threshold
>>>>>>> 7cf1c6205f980630c4b029fbce877b756e42b521
    '''

    if theoretical_homeowner != "N/A": #theoretically switch empty and occupied home

        relocate(grid, theoretical_homeowner, 
            location, empty_homes = None)

        neighborhood = compute_neighborhood(grid, R, location)
        color = theoretical_homeowner[2]
        same_empty = count_same_empty(neighborhood,
        color)

        relocate(grid, (location[0], location[1], color), 
            (theoretical_homeowner[0], theoretical_homeowner[1]))

    else: 
        neighborhood = compute_neighborhood(grid, R, location)
        color = grid[location[0]][location[1]]
        same_empty = count_same_empty(neighborhood, color)
    
    S = same_empty[0] #count of same 
    P = same_empty[1] #count of empty

    satisfaction_score = S + 0.5 * P 

    return (satisfaction_score / len(neighborhood)) >= threshold


def count_same_empty(neighborhood, color):
    '''
    How many locations are same color and how many empty 
    spaces are in the given neighborhood?

    Inputs:
        neighborhood: a list of locations in the neighborhood
        color: string that should be either O, R, B. 
        will look at the color of each location in 
        neighborhood and increment the count of same and 
        empty locations accordingly.  

    Returns:
        A tuple with in the form (count of same, 
            count of empty)
    '''

    countP = 0 
    countS = 0 

    for coordinate in neighborhood:
        if coordinate == color: 
            countS += 1
        if coordinate == 'O':
            countP += 1

    return (countS, countP)


def get_empty_homes(grid):
    '''
    Get a list of empty homes within a grid. Function 
    should only be run once. Assumes that a grid has 
    only O, R, B as values. 
    '''

    empty_homes = []

    for row in range(len(grid)): 
        for col in range(len(grid)): 
            if grid[row][col] == "O": 
                empty_homes.append((row, col))

    return empty_homes


def get_unsatisfied_homeowners(grid, R, threshold):
    '''
    Get a list of locations and color of an unsatisfied
    homeowner 

    Inputs: 
        grid: the grid
        R: radius for the neighborhood
        threshold: satisfaction threshold
    
    Returns: 
        List of location and color 
    '''
    
    unsatisfied_homeowners = []

    for row in range(len(grid)):
        for col in range(len(grid)):
            if not grid[row][col] == "O": #no need to count empty
                loc = (row, col)
                if not is_satisfied(grid, R, threshold, loc):
                    unsatisfied_homeowners.append((row, col, grid[row][col]))
         
    return unsatisfied_homeowners


def run_step(grid, R, threshold, empty_homes, unsatisfied_homeowners): 
    '''
    Run one step in the simulation. Finds the locations,
    color of unsatisfied homeowners and relocates each one 
    to an empty spot where the homeowner will be satisfied.

    Inputs: 
        grid: the grid
        R: radius for the neighborhood
        threshold: satisfaction threshold
        empty_homes: list of empty homes 
        unsatisfied_homeowners: list of unsatisfied_homeowners

    Returns: 
        False: if everyone is satisfied or no one else can be 
        satisfied
        True: otherwise 
        
    '''

    used_relocate = False #track to see if any changes were made
    satisfied = len(unsatisfied_homeowners) == 0
    if satisfied: 
        return False

    for homeowner in unsatisfied_homeowners:
        current_loc = (homeowner[0], homeowner[1]) 
        if is_satisfied(grid, R, threshold, current_loc):
            pass
        else:
            for location in empty_homes: 
                if is_satisfied(grid, R, threshold, location, 
                    homeowner): #theoretical test if homeowner moved
                    relocate(grid, homeowner, location, empty_homes)
                    used_relocate = True
                    break

    return used_relocate

def update_empty_homes(empty_homes, unsatisfied_homeowner, new_loc):
    '''
    Updates new list of empty homes in grid.

    Inputs: 
        empty_homes: list of empty homes
        unsatisfied_homeowner: tuple with x,y coordinates and 
        color
        new_loc: the new location that the unsatisfied_homeowner
        is moving to 
    '''

    empty_homes.insert(0, (unsatisfied_homeowner[0], 
        unsatisfied_homeowner[1]))
    empty_homes.remove(new_loc)

<<<<<<< HEAD
=======

def relocate(grid, unsatisfied_homeowner, new_loc, empty_homes = None):
    '''
    Moves homeowner (should be an unsatisfied one) to a 
    new location. Updates new list of empty homes in grid. 
    
    Inputs: 
        grid: the grid
        empty_homes: list of empty homes
        unsatisfied_homeowner: tuple with x,y coordinates and 
        color
        new_loc: the new location that the unsatisfied_homeowner
        is moving to 
    '''

    if empty_homes != None: 
        update_empty_homes(empty_homes, unsatisfied_homeowner,
        new_loc)

    grid[new_loc[0]][new_loc[1]] = unsatisfied_homeowner[2]
    grid[unsatisfied_homeowner[0]][unsatisfied_homeowner[1]] = "O"


>>>>>>> 7cf1c6205f980630c4b029fbce877b756e42b521
def do_simulation(grid, R, threshold, max_steps):
    ''' 
    Do a full simulation.
    
    grid: the grid
    R: radius for the neighborhood
    threshold: satisfaction threshold
    max_steps: maximum number of steps to do

    This function should return the number of steps executed.
<<<<<<< HEAD
    '''
    # YOUR CODE HERE
    # REPLACE 0 with an appropriate return value
    return 0
        

def compute_neighborhood(grid, R, location): 
    '''
    Returns a list of the locations in the neighborhood 
    of the given location. 
=======
    
    ''' 
    empty_homes = get_empty_homes(grid)
    num_steps = 0 
    while num_steps < max_steps: 
        unsatisfied_homeowners = get_unsatisfied_homeowners(grid, R, threshold)
        if run_step(grid, R, threshold, empty_homes, unsatisfied_homeowners): 
            num_steps += 1
        else: 
            num_steps += 1
            return num_steps
>>>>>>> 7cf1c6205f980630c4b029fbce877b756e42b521

    return num_steps

def within_grid(grid, location):
    '''
    Tells whether the given location is within the grid 

    Inputs:
        Grid: map 
        Location: given location to test 
    '''
    lower = (location[0] >= 0) and (location[1] >= 0)
    upper = (location[0] < len(grid)) and (location[1] < len(grid))

    return lower and upper

<<<<<<< HEAD
    
=======
        
>>>>>>> 7cf1c6205f980630c4b029fbce877b756e42b521
def go(args):
    usage = "usage: python schelling.py <grid file name> <R > 0> <0 < threshold <= 1.0> <max steps >= 0>\n"
    grid = None
    threshold = 0.0
    R = 0
    max_steps = 0
    MAX_SMALL_GRID = 20

    
    if (len(args) != 5):
        print(usage)
        sys.exit(0)

    # parse and check the arguments
    try:
        grid = utility.read_grid(args[1])

        R = int(args[2])
        if R <= 0:
            print("R must be greater than zero")
            sys.exit(0)

        threshold = float(args[3])
        if (threshold <= 0.0 or threshold > 1.0):
            print("threshold must be between 0.0 and 1.0 not inclusive")
            sys.exit(0)

        max_steps = int(args[4])
        if max_steps <= 0:
            print("max_steps must be greater than or equal to zero")
            sys.exit(0)

    except:
        print(usage)
        sys.exit(0)
        

    num_steps = do_simulation(grid, R, threshold, max_steps)
    if len(grid) < MAX_SMALL_GRID:
        for row in grid:
            print(row)
    else:
        print("Result grid too large to print")

    print("Number of steps simulated: " + str(num_steps))

if __name__ == "__main__":
    go(sys.argv)
  

<<<<<<< HEAD
print("FGT")

=======
>>>>>>> 7cf1c6205f980630c4b029fbce877b756e42b521
