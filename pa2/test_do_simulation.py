#  CS121:: Schelling Model of Housing Segregation
#
#  Test code for do_simulation
#
#  Anne Rogers
#  Summer 2015


from schelling import do_simulation
import pytest
import utility

TEST_DIR="tests/"

def helper_check_relocations(input_filename, expected_filename, R, threshold, max_num_steps):
    '''
    Do one simulation with the specified parameters (R, threshold,
    max_num_steps) starting from the specified input file.  Match
    actual grid generated with the expected grid.
    '''

    grid = utility.read_grid(TEST_DIR + input_filename)
    do_simulation(grid, R, threshold, max_num_steps)

    expected_grid = utility.read_grid(TEST_DIR + expected_filename)

    # compare the actual state of the city against the expected state
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            expected = expected_grid[i][j]
            # strip unsatisfied indicator from the expected file,
            # if necessary
            expected = expected if "U" not in expected else expected[1]
            if grid[i][j] != expected:
                s = "actual and expected values do not match at location ({:d}, {:d})\n".format(i, j)
                s = s + "got {}, expected {}".format(grid[i][j], expected)
                pytest.fail(s)


def helper_check_steps(input_filename, R, threshold, max_num_steps, expected_num_steps):
    '''
    Do one simulation with the specified parameters (R, threshold,
    max_num_steps) starting from the specified input file.  Compare
    the actual number of steps taken to the expected number of steps.
    '''

    grid = utility.read_grid(TEST_DIR + input_filename)
    actual = do_simulation(grid, R, threshold, max_num_steps)
    assert(actual == expected_num_steps)

# example from the assignment description
def test_relocations_0():
    # check no steps
    helper_check_relocations("grid4.txt", "grid4.txt", 1, .51, 0)

def test_steps_0():
    # check no steps
    helper_check_steps("grid4.txt", 1, .51, 0, 0)    

def test_relocations_1():
    # check relocations for sample grid from assignment description
    # after 1 step
    helper_check_relocations("grid4.txt", "grid4-1-51-1-3.txt", 1, .51, 1)

def test_steps_1():
    # check step count for sample grid from assignment description
    # after 1 step
    helper_check_steps("grid4.txt", 1, .51, 1, 1)    

def test_relocations_2():
    # check relocations for sample grid from assignment description
    # after 2 steps
    helper_check_relocations("grid4.txt", "grid4-1-51-2-2.txt", 1, .51, 2)

def test_relocations_3():
    # check relocations for sample grid from assignment description
    # after 3 steps
    helper_check_relocations("grid4.txt", "grid4-1-51-3-final.txt", 1, .51, 3)

def test_relocations_4():
    # check relocations for sample grid from assignment description
    # after 4 steps
    helper_check_relocations("grid4.txt", "grid4-1-51-4-final.txt", 1, .51, 4)

def test_steps_4():
    # check step count for sample grid from assignment description
    # after 4 steps

    helper_check_steps("grid4.txt", 1, .51, 4, 4)    

def test_steps_5():
    # check to make sure that the simulation stops after
    # a step with no moves.
    helper_check_steps("grid4.txt", 1, .51, 5, 4)    

def test_relocations_6():
    # check grid with no unsatisfied homeowners at start
    helper_check_relocations("grid4.txt", "grid4.txt", 1, .49, 1)

def test_steps_6():
    # check steps for a grid with no unsatisfied homeowners at start
    helper_check_steps("grid4.txt", 1, .49, 2, 1)

def test_relocations_7():
    # test larger value for R
    helper_check_relocations("grid4.txt", "grid4-2-51-7-final.txt", 2, 0.51, 7)

def test_steps_7():
    # test larger value for R
    helper_check_steps("grid4.txt", 2, 0.51, 7, 7)

def test_steps_8():
    # test larger value for R
    helper_check_steps("grid4.txt", 2, 0.51, 8, 7)

def test_relocations_9():
    # test larger value for R
    helper_check_relocations("grid4.txt", "grid4-3-51-5-final.txt", 3, 0.51, 5)

def test_steps_10():
    # test larger value for R
    helper_check_steps("grid4.txt", 3, 0.51, 5, 5)

def test_steps_11():
    # test larger value for R
    helper_check_steps("grid4.txt", 3, 0.51, 6, 5)

# some tests with larger grid with R = 1, 2, 3
def test_large_relocations_0():
     helper_check_relocations("grid-150-40-40.txt", "grid-150-40-40-1-51-100-final.txt", 1, 0.51, 100)

def test_large_relocations_1():
    helper_check_relocations("grid-150-40-40.txt", "grid-150-40-40-2-51-100-final.txt", 2, 0.51, 100)

def test_large_relocations_2():
    helper_check_relocations("grid-150-40-40.txt", "grid-150-40-40-3-51-100-final.txt", 3, 0.51, 100)







    
