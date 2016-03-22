import pytest
import simulate
import csv


def rt_helper(prefix, num_booths, expected):
    params_filename = prefix + ".json"
    params = simulate.setup_params(params_filename, num_booths)
    expected = [eval(row[0]) for row in csv.reader(open(prefix + "-extra-expected-" + str(num_booths) + ".txt"))]

    error_str = "Results of trial {} do not match.  Expected: {}     Got: {}"
    for t in range(params["num_trials"]):
        actual = simulate.simulate_election_day(params)
        print((t, expected[t], actual))
        if expected[t] != actual:
            pytest.fail(error_str.format(t, expected[t], actual))

def test_6():
    rt_helper("data/params1", 1, 1/3.0)

def test_7():
    rt_helper("data/params1", 2, 1.0)

def test_8():
    rt_helper("data/params1", 4, 1.0)


def test_9():
    rt_helper("data/params2", 6, 0.11000)

def test_10():
    rt_helper("data/params2", 7, 0.80000)

def test_11():
    rt_helper("data/params2", 8, 0.99000)


