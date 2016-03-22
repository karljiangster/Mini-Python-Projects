import pytest
import simulate


def sed_helper(params_filename, num_booths, expected):
    params = simulate.setup_params(params_filename, num_booths)
    actual = simulate.simulate_election_day(params)
    assert(actual == expected)

def test_0():
    sed_helper("data/params0.json", 1, False)

def test_1():
    sed_helper("data/params0.json", 2, False)

def test_2():
    sed_helper("data/params0.json", 4, True)

def test_3():
    sed_helper("data/params2.json", 6, False)

def test_4():
    sed_helper("data/params2.json", 7, True)

def test_5():
    sed_helper("data/params2.json", 8, True)


def rt_helper(params_filename, num_booths, expected):
    params = simulate.setup_params(params_filename, num_booths)
    actual = simulate.run_trials(params)
    if abs(actual - expected) > 0.000001:
        pytest.fail("Actual and expected results do not match.  {:.5f} != {:.5f}".format(actual, expected))

def test_6():
    rt_helper("data/params1.json", 1, 1/3.0)

def test_7():
    rt_helper("data/params1.json", 2, 1.0)

def test_8():
    rt_helper("data/params1.json", 4, 1.0)


def test_9():
    rt_helper("data/params2.json", 6, 0.11000)

def test_10():
    rt_helper("data/params2.json", 7, 0.80000)

def test_11():
    rt_helper("data/params2.json", 8, 0.99000)


