from schelling import is_satisfied
import utility

TEST_DIR="tests/"

def helper(filename, R, i, j, num_homes, same, empty, expected):
    # set threshold to be just a bit below (when expected is true) or
    # above (when expected is false) the ratio of the satisfaction
    # score and the number of homes.
    threshold = (same + 0.5*empty)/num_homes + (-0.01 if expected else 0.01)
    grid = utility.read_grid(TEST_DIR + filename)
    actual = is_satisfied(grid, R, threshold, (i, j))
    assert(actual == expected)

def test_0a():
    # top left corner, R=1
    # partial neighborhood
    helper("grid4.txt", 1, 0, 0, 3, 2, 1, False)

def test_0b():
    # top left corner, R=1
    # partial neighborhood
    helper("grid4.txt", 1, 0, 0, 3, 2, 1, True)  

def test_0c():
    # top left corner, R=2
    # partial neighborhood
    helper("grid4.txt", 2, 0, 0, 6, 3, 2, False)

def test_0d():
    # top left corner, R=2
    # partial neighborhood
    helper("grid4.txt", 2, 0, 0, 6, 3, 2, True)

def test_1a():
    # top right corner, R=1
    # partial neighborhood
    helper("grid4.txt", 1, 0, 4, 3, 2, 0, False)

def test_1b():
    # top right corner, R=1
    # partial neighborhood
    helper("grid4.txt", 1, 0, 4, 3, 2, 0, True)

def test_1c():
    # top right corner, R=2
    # partial neighborhood
    helper("grid4.txt", 2, 0, 4, 6, 3, 1, False)

def test_1d():
    # top right corner, R=2
    helper("grid4.txt", 2, 0, 4, 6, 3, 1, True)

def test_2a():
    # lower left corner, R=1
    # partial neighborhood
    helper("grid4.txt", 1, 4, 0, 3, 1, 1, False)

def test_2b():
    # lower left corner, R=1
    # partial neighborhood
    helper("grid4.txt", 1, 4, 0, 3, 1, 1, True)

def test_2c():
    # lower left corner, R=2
    # partial neighborhood
    helper("grid4.txt", 2, 4, 0, 6, 3, 1, False)

def test_2d():
    # lower left corner, R=2
    # partial neighborhood
    helper("grid4.txt", 2, 4, 0, 6, 3, 1, True)

def test_3a():
    # full neighborhood at R=1
    helper("grid4.txt", 1, 1, 1, 5, 2, 1, False)

def test_3b():
    # full neighborhood at R=1
    helper("grid4.txt", 1, 1, 1, 5, 2, 1, True)

def test_3c():
    # partial neighborhood at R=2
    helper("grid4.txt", 2, 1, 1, 11, 4, 2, False)

def test_3d():
    # partial neighborhood at R=2
    helper("grid4.txt", 2, 1, 1, 11, 4, 2, True)

# removed test4's because they did not add coverage.

def test_5a():
    # interior neighborhood
    helper("grid-no-neighbors.txt", 1, 2, 2, 5, 1, 4, False)

def test_5b():
    # interior neighborhood
    helper("grid-no-neighbors.txt", 1, 2, 2, 5, 1, 4, True)

def test_5c():
    # interior neighborhood
    helper("grid-no-neighbors.txt", 2, 2, 2, 13, 4, 9, False)

def test_5d():
    # interior neighborhood
    helper("grid-no-neighbors.txt", 2, 2, 2, 13, 4, 9, True)

def test_6a():
    # lower right corner, no neighbors when R=1
    helper("grid-no-neighbors.txt", 1, 4, 4, 3, 1, 2, False)

def test_6b():
    # lower right corner, no neighbors when R=1
    helper("grid-no-neighbors.txt", 1, 4, 4, 3, 1, 2, True)

def test_6c():
    # lower right corner, a few neighbors when R=2
    helper("grid-no-neighbors.txt", 2, 4, 4, 6, 1, 3, False)

def test_6d():
    # lower right corner, a few neighbors when R=2
    helper("grid-no-neighbors.txt", 2, 4, 4, 6, 1, 3, True)

def test_7a():
    # All red city except for one blue, R=1
    helper("grid-lone-blue-sea-red.txt", 1, 3, 3, 5, 1, 0, False)

def test_7b():
    # All red city except for one blue, R=1
    helper("grid-lone-blue-sea-red.txt", 1, 3, 3, 5, 1, 0, True)

def test_7c():
    # All red city except for one blue, R=2
    helper("grid-lone-blue-sea-red.txt", 2, 3, 3, 11, 1, 0, False)

def test_7d():
    # All red city except for one blue, R=2
    helper("grid-lone-blue-sea-red.txt", 2, 3, 3, 11, 1, 0, True)

def test_8a():
    # test R=3
    helper("grid4.txt", 3, 2, 2, 21, 9, 4, False)

def test_8b():
    # test R=3
    helper("grid4.txt", 3, 2, 2, 21, 9, 4, True)
