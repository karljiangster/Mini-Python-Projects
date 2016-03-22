import pytest
import simulate

def sed_helper(params_filename, num_booths, expected):
    params = simulate.setup_params(params_filename, num_booths)
    actual = simulate.simulate_election_day(params)
    if (actual != expected):
        pytest.fail("Expected:{}  Got: {}". format(actual, expected))

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

