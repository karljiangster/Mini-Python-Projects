# CS121 A'15: Test code for CPS assignment
#
# Yanjing Li 
# October 2015

import pytest
from cps import * 


################## build_morg_dict tests ##################

expected_dict_2007_mini = \
{'1_666_666': {'earnings_per_week': 0.0, 'gender': 'Female', 'age': 46, 'hours_worked_per_week': 10, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '20_25624_25624': {'earnings_per_week': 711.53, 'gender': 'Female', 'age': 37, 'hours_worked_per_week': 40, 'race': 'AsianOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '20_25582_25582': {'earnings_per_week': 146.25, 'gender': 'Male', 'age': 21, 'hours_worked_per_week': 25, 'race': 'AmericanIndian/AlaskanNativeOnly', 'employment_status': 'Working', 'ethnicity': 'Salvadoran'}, '6_7346_7346': {'earnings_per_week': 2173.07, 'gender': 'Female', 'age': 54, 'hours_worked_per_week': 40, 'race': 'BlackOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '20_25289_25289': {'earnings_per_week': 327.6, 'gender': 'Female', 'age': 55, 'hours_worked_per_week': 39, 'race': 'AI-HP', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '6_6898_6898': {'earnings_per_week': 500.0, 'gender': 'Male', 'age': 67, 'hours_worked_per_week': 40, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Dominican'}, '2_1088_1088': {'earnings_per_week': '', 'gender': 'Male', 'age': 56, 'hours_worked_per_week': '', 'race': 'BlackOnly', 'employment_status': 'Looking', 'ethnicity': 'Non-Hispanic'}, '1_46_46': {'earnings_per_week': 380.0, 'gender': 'Male', 'age': 28, 'hours_worked_per_week': 40, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Dominican'}, '2_1314_1314': {'earnings_per_week': 290.5, 'gender': 'Male', 'age': 17, 'hours_worked_per_week': 35, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '24_178642_30613': {'earnings_per_week': '', 'gender': 'Female', 'age': 20, 'hours_worked_per_week': '', 'race': 'BlackOnly', 'employment_status': 'Layoff', 'ethnicity': 'Non-Hispanic'}, '19_24212_24212': {'earnings_per_week': 550.0, 'gender': 'Male', 'age': 38, 'hours_worked_per_week': 38, 'race': 'AsianOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '20_25196_25196': {'earnings_per_week': 484.4, 'gender': 'Male', 'age': 42, 'hours_worked_per_week': 40, 'race': 'White-AI', 'employment_status': 'Working', 'ethnicity': 'Mexican'}, '13_137361_18675': {'earnings_per_week': '', 'gender': 'Male', 'age': 38, 'hours_worked_per_week': '', 'race': 'WhiteOnly', 'employment_status': 'Layoff', 'ethnicity': 'Mexican'}, '1_554_554': {'earnings_per_week': 890.0, 'gender': 'Male', 'age': 29, 'hours_worked_per_week': 40, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '1_34_34': {'earnings_per_week': 538.46, 'gender': 'Female', 'age': 60, 'hours_worked_per_week': 40, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '21_26276_26276': {'earnings_per_week': 1442.3, 'gender': 'Male', 'age': 60, 'hours_worked_per_week': 50, 'race': 'AsianOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '1_1_1': {'earnings_per_week': 1250.0, 'gender': 'Female', 'age': 32, 'hours_worked_per_week': 40, 'race': 'BlackOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '9_11763_11763': {'earnings_per_week': 500.0, 'gender': 'Male', 'age': 49, 'hours_worked_per_week': 50, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '18_23481_23481': {'earnings_per_week': 512.0, 'gender': 'Female', 'age': 47, 'hours_worked_per_week': 40, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '8_9768_9768': {'earnings_per_week': 2884.0, 'gender': 'Male', 'age': 36, 'hours_worked_per_week': 50, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}}

expected_dict_2010_mini = \
{'4_2556_2556': {'earnings_per_week': 2307.69, 'gender': 'Male', 'age': 45, 'hours_worked_per_week': 45, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '1_853_853': {'earnings_per_week': 461.0, 'gender': 'Female', 'age': 59, 'hours_worked_per_week': 15, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '36_44906_44906': {'earnings_per_week': '', 'gender': 'Female', 'age': 65, 'hours_worked_per_week': '', 'race': 'WhiteOnly', 'employment_status': 'Layoff', 'ethnicity': 'PuertoRican'}, '15_19313_19313': {'earnings_per_week': 1040.0, 'gender': 'Female', 'age': 32, 'hours_worked_per_week': 40, 'race': 'W-A-HP', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '4_2251_2251': {'earnings_per_week': 1269.23, 'gender': 'Male', 'age': 25, 'hours_worked_per_week': 50, 'race': 'White-AI', 'employment_status': 'Working', 'ethnicity': 'Mexican'}, '6_8681_8681': {'earnings_per_week': 350.0, 'gender': 'Male', 'age': 28, 'hours_worked_per_week': 40, 'race': 'BlackOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '10_12575_12575': {'earnings_per_week': 576.92, 'gender': 'Female', 'age': 35, 'hours_worked_per_week': 35, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '13_17991_17991': {'earnings_per_week': 1403.84, 'gender': 'Female', 'age': 49, 'hours_worked_per_week': 50, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '12_16203_16203': {'earnings_per_week': 961.0, 'gender': 'Male', 'age': 41, 'hours_worked_per_week': 40, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Dominican'}, '9_11174_11174': {'earnings_per_week': 2375.0, 'gender': 'Female', 'age': 55, 'hours_worked_per_week': 60, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '6_8362_8362': {'earnings_per_week': 1807.69, 'gender': 'Female', 'age': 35, 'hours_worked_per_week': 40, 'race': 'AsianOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '15_19443_19443': {'earnings_per_week': 1192.3, 'gender': 'Male', 'age': 25, 'hours_worked_per_week': 40, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '6_5231_5231': {'earnings_per_week': 525.0, 'gender': 'Female', 'age': 32, 'hours_worked_per_week': 35, 'race': 'White-Black', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '5_3464_3464': {'earnings_per_week': '', 'gender': 'Male', 'age': 66, 'hours_worked_per_week': '', 'race': 'WhiteOnly', 'employment_status': 'Looking', 'ethnicity': 'Non-Hispanic'}, '2_78016_1870': {'earnings_per_week': '', 'gender': 'Male', 'age': 27, 'hours_worked_per_week': '', 'race': 'WhiteOnly', 'employment_status': 'Layoff', 'ethnicity': 'Non-Hispanic'}, '10_12120_12120': {'earnings_per_week': 585.0, 'gender': 'Female', 'age': 50, 'hours_worked_per_week': 40, 'race': 'White-Black', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '1_60_60': {'earnings_per_week': 1115.38, 'gender': 'Male', 'age': 37, 'hours_worked_per_week': 40, 'race': 'BlackOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '4_2097_2097': {'earnings_per_week': 400.0, 'gender': 'Male', 'age': 49, 'hours_worked_per_week': 40, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Mexican'}, '2_1257_1257': {'earnings_per_week': 570.0, 'gender': 'Female', 'age': 26, 'hours_worked_per_week': 30, 'race': 'AmericanIndian/AlaskanNativeOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '5_3231_3231': {'earnings_per_week': 807.0, 'gender': 'Male', 'age': 62, 'hours_worked_per_week': 40, 'race': 'AsianOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}}

expected_dict_2014_mini = \
{'6_12640_12640': {'earnings_per_week': 180.0, 'gender': 'Female', 'age': 18, 'hours_worked_per_week': 20, 'race': 'Hawaiian/PacificIslanderOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '9_16658_16658': {'earnings_per_week': 1000.0, 'gender': 'Male', 'age': 52, 'hours_worked_per_week': 40, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'PuertoRican'}, '10_17469_17469': {'earnings_per_week': 1200.0, 'gender': 'Female', 'age': 48, 'hours_worked_per_week': 38, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '6_5630_5630': {'earnings_per_week': 1057.0, 'gender': 'Male', 'age': 41, 'hours_worked_per_week': 40, 'race': 'AsianOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '9_15444_15444': {'earnings_per_week': 346.15, 'gender': 'Male', 'age': 73, 'hours_worked_per_week': 24, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '6_129443_11888': {'earnings_per_week': '', 'gender': 'Female', 'age': 17, 'hours_worked_per_week': '', 'race': 'AsianOnly', 'employment_status': 'Layoff', 'ethnicity': 'Non-Hispanic'}, '6_10034_10034': {'earnings_per_week': 1750.0, 'gender': 'Female', 'age': 85, 'hours_worked_per_week': 70, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '6_11231_11231': {'earnings_per_week': 115.38, 'gender': 'Male', 'age': 28, 'hours_worked_per_week': 40, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '6_5962_5962': {'earnings_per_week': 1346.15, 'gender': 'Female', 'age': 52, 'hours_worked_per_week': 40, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Mexican'}, '6_5532_5532': {'earnings_per_week': 307.69, 'gender': 'Male', 'age': 21, 'hours_worked_per_week': 40, 'race': 'White-HP', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '6_9460_9460': {'earnings_per_week': 1923.07, 'gender': 'Female', 'age': 39, 'hours_worked_per_week': 40, 'race': 'AsianOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '4_3828_3828': {'earnings_per_week': '', 'gender': 'Female', 'age': 68, 'hours_worked_per_week': '', 'race': 'WhiteOnly', 'employment_status': 'Layoff', 'ethnicity': 'Mexican'}, '6_5567_5567': {'earnings_per_week': 2115.38, 'gender': 'Male', 'age': 46, 'hours_worked_per_week': 40, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '5_4412_4412': {'earnings_per_week': 480.0, 'gender': 'Female', 'age': 50, 'hours_worked_per_week': 40, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Mexican'}, '6_6837_6837': {'earnings_per_week': 1615.38, 'gender': 'Male', 'age': 32, 'hours_worked_per_week': 40, 'race': 'BlackOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '6_11604_11604': {'earnings_per_week': 1458.0, 'gender': 'Male', 'age': 68, 'hours_worked_per_week': 40, 'race': 'AsianOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '8_13698_13698': {'earnings_per_week': 835.0, 'gender': 'Male', 'age': 63, 'hours_worked_per_week': 40, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}, '6_10862_10862': {'earnings_per_week': 320.0, 'gender': 'Male', 'age': 22, 'hours_worked_per_week': 40, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Mexican'}, '1_1014_1014': {'earnings_per_week': '', 'gender': 'Male', 'age': 54, 'hours_worked_per_week': '', 'race': 'WhiteOnly', 'employment_status': 'Looking', 'ethnicity': 'Non-Hispanic'}, '4_3781_3781': {'earnings_per_week': 1192.3, 'gender': 'Female', 'age': 55, 'hours_worked_per_week': 40, 'race': 'WhiteOnly', 'employment_status': 'Working', 'ethnicity': 'Non-Hispanic'}}

def helper_build_morg_dict(input_dict, expected):
    morg_dict = build_morg_dict(input_dict)
    assert morg_dict == expected

def test_build_morg_dict_2007_mini():
    input_files = {}
    input_files['morg'] = 'data/morg_d07_mini.csv'
    input_files['gender_codes'] = 'data/gender_code.csv'
    input_files['race_codes'] = 'data/race_code.csv'
    input_files['ethnic_codes'] = 'data/ethnic_code.csv'
    input_files['employment_codes'] = 'data/employment_status_code.csv'

    helper_build_morg_dict(input_files, expected_dict_2007_mini)

def test_build_morg_dict_2010_mini():
    input_files = {}
    input_files['morg'] = 'data/morg_d10_mini.csv'
    input_files['gender_codes'] = 'data/gender_code.csv'
    input_files['race_codes'] = 'data/race_code.csv'
    input_files['ethnic_codes'] = 'data/ethnic_code.csv'
    input_files['employment_codes'] = 'data/employment_status_code.csv'

    helper_build_morg_dict(input_files, expected_dict_2010_mini)

def test_build_morg_dict_2014_mini():
    input_files = {}
    input_files['morg'] = 'data/morg_d14_mini.csv'
    input_files['gender_codes'] = 'data/gender_code.csv'
    input_files['race_codes'] = 'data/race_code.csv'
    input_files['ethnic_codes'] = 'data/ethnic_code.csv'
    input_files['employment_codes'] = 'data/employment_status_code.csv'

    helper_build_morg_dict(input_files, expected_dict_2014_mini)


################## create_histogram tests ##################

expected_histogram_1 = []
expected_histogram_2 = [0, 0]
expected_histogram_3 = [1, 0, 1, 1, 9, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0]
expected_histogram_4 = [0, 0, 0, 0, 0, 1, 1, 0, 1, 2, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
expected_histogram_5 = [4, 2, 5]

def test_create_histogram_1():
    morg_dict_2007 = expected_dict_2007_mini 
    actual_histogram = create_histogram(morg_dict_2007, HRWKE, 0, 0, 40)
    assert actual_histogram == expected_histogram_1

def test_create_histogram_2():
    morg_dict_2014 = expected_dict_2014_mini 
    actual_histogram = create_histogram(morg_dict_2014, HRWKE, 2, 1000, 1001)
    assert actual_histogram == expected_histogram_2

def test_create_histogram_3():
    morg_dict_2007 = expected_dict_2007_mini 
    actual_histogram = create_histogram(morg_dict_2007, HRWKE, 20, 35, 60)
    assert actual_histogram == expected_histogram_3

def test_create_histogram_4():
    morg_dict_2010 = expected_dict_2010_mini 
    actual_histogram = create_histogram(morg_dict_2010, EARNWKE, 50, 0, 3000)
    assert actual_histogram == expected_histogram_4

def test_create_histogram_5():
    morg_dict_2014 = expected_dict_2014_mini 
    actual_histogram = create_histogram(morg_dict_2014, EARNWKE, 3, 99.5, 1500)
    assert actual_histogram == expected_histogram_5


################## calculate_unemployment_rates tests ##################
expected_unemployment_rates_str_1 = ['|Year              |10                |14                |', '|AI-Asian          |0.00              |0.00              |', '|AI-HP             |0.00              |0.00              |', '|AmericanIndian/Ala|0.00              |0.00              |', '|Asian-HP          |0.00              |0.00              |', '|AsianOnly         |0.00              |1.00              |', '|B-AI-A            |0.00              |0.00              |', '|Black-AI          |0.00              |0.00              |', '|Black-Asian       |0.00              |0.00              |', '|Black-HP          |0.00              |0.00              |', '|BlackOnly         |0.00              |0.00              |', '|Hawaiian/PacificIs|0.00              |0.00              |', '|Other3RaceCombinat|0.00              |0.00              |', '|Other4and5RaceComb|0.00              |0.00              |', '|W-A-HP            |0.00              |0.00              |', '|W-AI-A            |0.00              |0.00              |', '|W-AI-A-HP         |0.00              |0.00              |', '|W-AI-HP           |0.00              |0.00              |', '|W-B-A             |0.00              |0.00              |', '|W-B-AI            |0.00              |0.00              |', '|W-B-AI-A          |0.00              |0.00              |', '|W-B-HP            |0.00              |0.00              |', '|White-AI          |0.00              |0.00              |', '|White-Asian       |0.00              |0.00              |', '|White-Black       |0.00              |0.00              |', '|White-HP          |0.00              |0.00              |', '|WhiteOnly         |0.50              |0.00              |'] 


expected_unemployment_rates_str_2 = ['|Year              |07                |10                |14                |', '|Female            |0.12              |0.10              |0.25              |', '|Male              |0.17              |0.20              |0.09              |']

expected_unemployment_rates_str_3 = ['|Year              |10                |', '|CentralAmericanExc|0.00              |', '|Cuban             |0.00              |', '|Dominican         |0.00              |', '|Mexican           |0.00              |', '|Non-Hispanic      |0.00              |', '|OtherSpanish      |0.00              |', '|PuertoRican       |0.00              |', '|Salvadoran        |0.00              |', '|SouthAmerican     |0.00              |'] 

expected_unemployment_rates_str_4 = []

def test_calculate_unemployment_rates_1():
    actual_str = calculate_unemployment_rates(["morg_d14_mini.csv", "morg_d10_mini.csv"], (17, 30), RACE)
    assert actual_str == expected_unemployment_rates_str_1

def test_calculate_unemployment_rates_2():
    actual_str = calculate_unemployment_rates(["morg_d14_mini.csv", "morg_d10_mini.csv", "morg_d14_mini.csv", "morg_d07_mini.csv"], (17, 80), GENDER)
    assert actual_str == expected_unemployment_rates_str_2

def test_calculate_unemployment_rates_3():
    actual_str = calculate_unemployment_rates(["morg_d10_mini.csv"], (1000, 1001), ETHNIC)
    assert actual_str == expected_unemployment_rates_str_3

def test_calculate_unemployment_rates_4():
    actual_str = calculate_unemployment_rates([], (0, 1000), GENDER)
    assert actual_str == expected_unemployment_rates_str_4

################## calculate_weekly_earnings_stats_for_fulltime_workers tests ##################
expected_earnings_stats_list_1 = [880.1333333333333, 500.0, 290.5, 2884.0]
expected_earnings_stats_list_2 = [0.0, 0.0, 0.0, 0.0]
expected_earnings_stats_list_3 = [307.69, 307.69, 307.69, 307.69]

def helper_round_floats_list(list, decimal_place):
    for i in range(len(list)):
        list[i] = round(list[i], decimal_place) 

def helper_cmp_weekly_earnings_stats(actual, expected):
    # for floating point values, only compare up to 2 decimal points
    helper_round_floats_list(actual, 2)
    helper_round_floats_list(expected, 2)
    assert actual == expected

def test_calculate_weekly_earnings_stats_for_fulltime_workers_1():
    morg_dict_2007 = expected_dict_2007_mini 
    actual_list = calculate_weekly_earnings_stats_for_fulltime_workers(morg_dict_2007, 'Male', 'All', 'All')
    helper_cmp_weekly_earnings_stats(actual_list, expected_earnings_stats_list_1) 

def test_calculate_weekly_earnings_stats_for_fulltime_workers_2():
    morg_dict_2010 = expected_dict_2010_mini 
    actual_list = calculate_weekly_earnings_stats_for_fulltime_workers(morg_dict_2010, 'Female', 'AsianOnly', 'Hispanic') 
    helper_cmp_weekly_earnings_stats(actual_list, expected_earnings_stats_list_2) 

def test_calculate_weekly_earnings_stats_for_fulltime_workers_3():
    morg_dict_2014 = expected_dict_2014_mini 
    actual_list = calculate_weekly_earnings_stats_for_fulltime_workers(morg_dict_2014, 'All', 'Other', 'Non-Hispanic')
    helper_cmp_weekly_earnings_stats(actual_list, expected_earnings_stats_list_3) 
