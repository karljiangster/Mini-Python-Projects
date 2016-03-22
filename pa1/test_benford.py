# CS121 A'16: Test code for Benford's Law assignment
#
# Anne Rogers
# June 2015

import math
import pytest
from benford import *
from util import read_column_from_csv

TEST_DATA_DIR="test_data"
AMOUNTS = ["$1.01", "$2.20", "$3.333", "$44.4", "$0.000055", "$6.006", "$777.0", "$8.00", "$99999.9999", "$99"]


################## Extract leading digit of single value tests ##################

def helper_extract_leading_digits_single(num_digits, amount, expected):
    leading_digits = extract_leading_digits_single(amount, num_digits)
    assert leading_digits == expected

def test_extract_leading_digits_single_1():
    helper_extract_leading_digits_single(1, 2.34, 2)

def test_extract_leading_digits_single_2():
    helper_extract_leading_digits_single(2, 2.34, 23)

def test_extract_leading_digits_single_3():
    helper_extract_leading_digits_single(3, 2.34, 234)

def test_extract_leading_digits_single_4():
    helper_extract_leading_digits_single(2, 0.2034, 20)

def test_extract_leading_digits_single_5():
    '''floating point precision issues lead to the "wrong" answer'''
    helper_extract_leading_digits_single(3, 2.01, 200)

def test_extract_leading_digits_single_6():
    '''
    A very slightly incorrect implementation (bad negation) passes all
    other tests except this edge case.
    '''
    helper_extract_leading_digits_single(1, 1000.00, 1)


################## Extract leading digit list tests ##################
def test_extract_leading_digits_list_empty():
    leading_digits = extract_leading_digits_from_list([], 1)
    assert leading_digits == []

def test_extract_leading_digits_list_1():
    l = ["$2.34"]
    l_copy = l[:]
    expected = [2]
    leading_digits = extract_leading_digits_from_list(l, 1)
    assert expected == leading_digits
    assert l == l_copy, "Do not change the list that is passed to your function!"

def test_extract_leading_digits_list_2():
    l = ["$2.34"]
    l_copy = l[:]
    expected = [23]
    leading_digits = extract_leading_digits_from_list(l, 2)
    assert expected == leading_digits
    assert l == l_copy, "Do not change the list that is passed to your function!"


def test_extract_leading_digits_list_3():
    expected = list(range(1, 10)) + [9]
    AMOUNTS_COPY = AMOUNTS[:]
    leading_digits = extract_leading_digits_from_list(AMOUNTS, 1)
    assert expected == leading_digits
    assert AMOUNTS == AMOUNTS_COPY, "Do not change the list that is passed to your function!"

def helper_extract_leading_digits_payments(num_payments, col, num_digits):
    prefix = TEST_DATA_DIR + "/payments_" + str(num_payments) + "_"
    input_filename = prefix+"input.csv"
    amounts = read_column_from_csv(input_filename, col, True)
    amounts_copy = amounts[:]

    expected_filename = prefix + str(num_digits) + "_leading_digits.txt"
    expected = []
    for x in read_column_from_csv(expected_filename, 0, True):
        expected.append(int(x))
    leading_digits = extract_leading_digits_from_list(amounts, num_digits)
    assert leading_digits == expected
    assert amounts == amounts_copy, "Do not change the list that is passed to your function!"


# Remove the triple-quotes around the code below, if you want to check
# your function on some larger sets of data.
'''
def test_extract_leading_digits_list_50_1():
    helper_extract_leading_digits_payments(50, 2, 1)

def test_extract_leading_digits_list_50_2():
    helper_extract_leading_digits_payments(50, 2, 2)

def test_extract_leading_digits_list_50000_1():
    helper_extract_leading_digits_payments(50000, 2, 1)

def test_extract_leading_digits_list_50000_2():
    helper_extract_leading_digits_payments(50000, 2, 2)
'''


################## Floating point comparison helpers ##################

# used in floating point equality tests
EPS = 0.0000001

def compare_actual_expected(actual, expected):
    if len(actual) != len(expected):
        pytest.fail("Length of expected ({0}) and actual results ({1}) do not match".format(len(expected), len(actual)))

    for i in range(len(actual)):
        # stored and computed representations may not be identical
        if abs(expected[i] - actual[i]) > EPS:
            pytest.fail("actual and expected values do not match at element {0}".format(i))
    

def compare_actual_expected_from_file(actual, expected_filename):
    # get expected list of values from the file
    expected = []
    for x in read_column_from_csv(expected_filename, 0, True):
        expected.append(float(x))

    compare_actual_expected(actual, expected)

################## Compute expected benford distribution tests ##################

def helper_test_compute_expected_benford_dist(num_digits):
    actual = compute_expected_benford_dist(num_digits)
    expected_filename = TEST_DATA_DIR + "/expected_benford_dist_{0}_output.txt".format(num_digits)
    compare_actual_expected_from_file(actual, expected_filename)

def test_compute_expected_benford_dist_1():
    helper_test_compute_expected_benford_dist(1)

def test_compute_expected_benford_dist_2():
    helper_test_compute_expected_benford_dist(2)


################## Compute benford distribution tests ##################

def test_compute_benford_dist_1():
    l = ["$2.34"]
    l_copy = l[:]
    actual = compute_benford_dist(["$2.34"], 1)
    expected = [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    compare_actual_expected(actual, expected)
    assert l == l_copy, "Do not change the list that is passed to your function!"

def test_compute_benford_dist_10_1():
    val = 1/10.0
    expected = [val]*9
    # lb of range is 1, lists are 0-based.
    expected[9-1] = val*2
    AMOUNTS_COPY = AMOUNTS[:]
    actual = compute_benford_dist(AMOUNTS, 1)
    compare_actual_expected(actual, expected)
    assert AMOUNTS == AMOUNTS_COPY, "Do not change the list that is passed to your function!"
    
def test_compute_benford_dist_10_2():
    expected = [0]*90
    val = 1/10.0
    lb = 10
    for x in [10, 22, 33, 44, 55, 60, 77, 80]:
        expected[x-lb] = val
    expected[99-lb] = val*2
    AMOUNTS_COPY = AMOUNTS[:]
    actual = compute_benford_dist(AMOUNTS, 2)
    compare_actual_expected(actual, expected)
    assert AMOUNTS == AMOUNTS_COPY, "Do not change the list that is passed to your function!"
    

def helper_test_compute_benford_dist(prefix, col, num_digits):
    input_filename = prefix + "input.csv"
    amounts = read_column_from_csv(input_filename, col, True)
    amounts_copy = amounts[:]
    actual = compute_benford_dist(amounts, num_digits)

    expected_filename = prefix + "computed_benford_dist_{0}_output.txt".format(num_digits)
    compare_actual_expected_from_file(actual, expected_filename)
    assert amounts == amounts_copy, "Do not change the list that is passed to your function!"


def test_compute_benford_dist_50_1():
    helper_test_compute_benford_dist(TEST_DATA_DIR + "/payments_50_", 2, 1)

def test_compute_benford_dist_50_2():
    helper_test_compute_benford_dist(TEST_DATA_DIR + "/payments_50_", 2, 2)

def test_compute_benford_dist_50000_1():
    helper_test_compute_benford_dist(TEST_DATA_DIR + "/payments_50000_", 2, 1)

def test_compute_benford_dist_50000_2():
    helper_test_compute_benford_dist(TEST_DATA_DIR + "/payments_50000_", 2, 2)


################## Compute benford MAD tests ##################


def test_benford_MAD_1():
    actual = compute_benford_MAD(["$2.34"], 1)
    compare_actual_expected([actual], [0.1830908])

def test_compute_benford_MAD_10_1():
    actual = compute_benford_MAD(AMOUNTS, 1)
    compare_actual_expected([actual], [0.0671244])

def test_compute_benford_MAD_10_2():
    actual = compute_benford_MAD(AMOUNTS, 2)
    compare_actual_expected([actual], [0.0196935])

def helper_test_compute_benford_MAD(prefix, col, num_digits):
    input_filename = prefix + "input.csv"
    amounts = read_column_from_csv(input_filename, col, True)
    actual = compute_benford_MAD(amounts, num_digits)

    expected_filename = prefix + "computed_benford_mad_{0}_output.txt".format(num_digits)
    compare_actual_expected_from_file([actual], expected_filename)

def test_compute_benford_MAD_50_1():
    helper_test_compute_benford_MAD(TEST_DATA_DIR + "/payments_50_", 2, 1)

def test_compute_benford_MAD_50_2():
    helper_test_compute_benford_MAD(TEST_DATA_DIR + "/payments_50_", 2, 2)

def test_compute_benford_MAD_50000_1():
    helper_test_compute_benford_MAD(TEST_DATA_DIR + "/payments_50000_", 2, 1)

def test_compute_benford_MAD_50000_2():
    helper_test_compute_benford_MAD(TEST_DATA_DIR + "/payments_50000_", 2, 2)

