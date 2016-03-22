# CS121 A'15: Current Population Survey (CPS) 
#
# Functions for mining CPS data 
#
# Karl Jiang

from pa3_helpers import read_csv, plot_histogram

# Constants 
HID = "h_id" 
AGE = "age"
GENDER = "gender" 
RACE = "race" 
ETHNIC = "ethnicity" 
STATUS = "employment_status"
HRWKE = "hours_worked_per_week" 
EARNWKE = "earnings_per_week" 

MORG_CODE = "morg"

GENDER_CODE = "gender_codes"
RACE_CODE = "race_codes"
ETHNIC_CODE = "ethnic_codes"
EMPLOYMENT_CODE = "employment_codes"

AGE_INDEX = 1
GENDER_INDEX = 2 
RACE_INDEX = 3 
ETHNIC_INDEX = 4 
EMPLOYMENT_INDEX = 5
HRWKE_INDEX = 6
EARNWKE_INDEX = 7 

FULLTIME_MIN_WORKHRS = 35

COLUMN_WIDTH = 18
COLUMN_SEP = "|"
PERCENT_LEN = 4 

valid_genders = ["Male", "Female", "All"]
valid_races = ["WhiteOnly","BlackOnly",
    "AmericanIndian/AlaskanNativeOnly", "AsianOnly",
    "Hawaiian/PacificIslanderOnly", "Other", "All"]
valid_ethnicities = ["Hispanic", "Non-Hispanic", "All"]

ALL = "All"
NONHISPANIC = "Non-Hispanic"
HISPANIC = "Hispanic"
OTHER = "Other"

MEAN_INDEX = 0
MEDIAN_INDEX = 1
MIN_INDEX = 2
MAX_INDEX = 3


def initialize_code(filename, need_header = True): 
    '''
    Reads the "codes.csv" filename and returns a dict based on 
    the given filename. 

    Inputs: 
        filename - string that represents one of the 
        csv code files 
        need_header - True if the header is needed, false otherwise

    Returns: 
        dictionary with codes and corresponding val 
    ''' 

    code = read_csv(filename, need_header)
    d = {code[0]: (code[1])
        for (code[0], code[1]) in 
        code[0:]}
    return d 


def format_row_data(rowdata, gender_codes_dict,
    race_codes_dict, ethnic_codes_dict, employment_codes_dict):
    '''
    Formats the row data by looking if there is 
    a numeric value with a code, and changes that code 
    to its indicated value. Also looks at each code and 
    puts it in the right format. 

    Inputs: 
        rowdata: list based on row in morg.csv
        dict (4 of them): dictionaries with keys 
        to special values 

    Returns: 
        dictionary with updated values 
    ''' 
    formatted_data = {}

    age = rowdata[AGE_INDEX]
    hours = rowdata[HRWKE_INDEX]
    earnings = rowdata[EARNWKE_INDEX]

    if len(age) > 0: 
        formatted_data[AGE] = int(age)
    else: 
        formatted_data[AGE] = ''

    if len(hours) > 0:
        formatted_data[HRWKE] = int(hours)
    else: 
        formatted_data[HRWKE] = hours

    if len(earnings) > 0:
        formatted_data[EARNWKE] = float(earnings)
    else: 
        formatted_data[EARNWKE] = earnings

    formatted_data[GENDER] = gender_codes_dict.get(
        rowdata[GENDER_INDEX], '')

    formatted_data[RACE] = race_codes_dict.get(
        rowdata[RACE_INDEX], '')

    formatted_data[ETHNIC] = ethnic_codes_dict.get(
        rowdata[ETHNIC_INDEX], 'Non-Hispanic')
    
    formatted_data[STATUS] = employment_codes_dict.get(
        rowdata[EMPLOYMENT_INDEX], '')

    return formatted_data


def build_morg_dict(input_dict):
    '''
    Build a dictionary that holds a set of CPS data 

    Inputs:
        input_dict: dict

        An example of input_dict is shown below: 
        {'morg':'data/morg_d14_mini.csv',
         'gender_codes':'data/gender_code.csv',
         'race_codes':'data/race_code.csv',
         'ethnic_codes':'data/ethnic_code.csv',
         'employment_codes':'data/employment_status_code.csv'}


    Returns:
        dict 
    '''
    gender_codes_dict = initialize_code(
        input_dict[GENDER_CODE]) 

    race_codes_dict = initialize_code(
        input_dict[RACE_CODE]) 

    ethnic_codes_dict = initialize_code(
        input_dict[ETHNIC_CODE]) 

    employment_codes_dict = initialize_code(
        input_dict[EMPLOYMENT_CODE]) 

    morg_dict = {}
    dataset = read_csv(input_dict[MORG_CODE], True)[1:]
   
    for rowdata in dataset: 
        hid_key = rowdata[0] 
        hid_dict = format_row_data(rowdata, 
            gender_codes_dict, race_codes_dict, ethnic_codes_dict, employment_codes_dict)
        morg_dict[hid_key] = hid_dict

    return morg_dict


def create_ranges(num_buckets, min_val, max_val): 
    '''
    Creates a list of ranges (tuples). To be 
    used for create_histogram. 

    Inputs: 
        num_buckets: number of buckets in the histogram
        min_val: the minimal value (lower bound) of the histogram
        max_val: the maximal value (upper bound) of the histogram 
    
    Returns: 
        List of ranges 
    '''

    ranges = [] 
    for i in range(num_buckets): 
        lower_range = i * (max_val - min_val)/ num_buckets + min_val
        upper_range = (i + 1) * (max_val - min_val)/ num_buckets + min_val
        ranges.append((lower_range, upper_range))

    return ranges


def determine_range_index(value, ranges):
    '''
    Returns the index of the range in list ranges
    that contains the value. Assumes that value falls 
    in ranges

    Inputs:
        value: any float 
        ranges: list of ranges 
    
    Returns: 
        integer indicating index of the range in ranges 
    '''
    
    for i, range in enumerate(ranges): 
        if value >= range[0] and value < range[1]:
            return i

    return -1 #value is not in ranges, should not return this

def is_working(rowdata): 
    '''
    Checks to see if the specified individual is 
    working full time. That is, employment_status 
    is Working and hours weeked is >= 35

    Inputs: 
        rowdata: the answer to the survey questions 
        of one individual via the hi_d in morg_dict

    returns: 
        True if is working full time, False otherwise 
    '''
    if not rowdata[HRWKE] and not rowdata[EARNWKE]:
        return False 
    return rowdata[HRWKE] >= FULLTIME_MIN_WORKHRS and rowdata[STATUS] == "Working"

def create_histogram(morg_dict, var_of_interest, num_buckets, 
                     min_val, max_val):
    '''
    Create a histogram using a list 

    Inputs:
        morg_dict: a MORG dictionary 
        var_of_interest: string (e.g., HRWKE or EARNW3KE)
        num_buckets: number of buckets in the histogram
        min_val: the minimal value (lower bound) of the histogram
        max_val: the maximal value (upper bound) of the histogram 

    Returns:
        list that represents a histogram 
    '''

    ranges = create_ranges(num_buckets, min_val, max_val)
    count = [0] * len(ranges)
    
    for hid in morg_dict:
        index_range = -1
        if is_working(morg_dict[hid]): 
            value = morg_dict[hid][var_of_interest]
            index_range = determine_range_index(value, ranges)
        if index_range != -1:
            count[index_range] += 1
 
    return count


def build_file_interest(var_of_interest): 
    '''
    Returns the corresponding csv code filename as a string. If the 
    var_of_interest does not have a corresponding csv filename, 
    will return "No corresponding csv file."
    '''

    filename = "No corresponding csv file."

    if var_of_interest == GENDER: 
        filename = 'data/gender_code.csv'
    if var_of_interest == RACE: 
        filename = 'data/race_code.csv'
    if var_of_interest == ETHNIC: 
        filename = 'data/ethnic_code.csv'
    if var_of_interest == STATUS: 
        filename = 'data/employment_status_code.csv'

    return filename 


def build_input_dict(filename): 
    '''
    Makes an input_dict for the given filename

    Returns: 
        dictionary input_dict where 'morg' returns the 
        filename 
    ''' 

    input_dict = {'morg': "data/" + filename,
         'gender_codes':'data/gender_code.csv',
         'race_codes':'data/race_code.csv',
         'ethnic_codes':'data/ethnic_code.csv',
         'employment_codes':'data/employment_status_code.csv'}

    return input_dict


def get_employment_status(rowdata): 
    '''
    Tells if the given individual with info from morg_dict
    is employed or not. 

    Input: 
        rowdata: an entry in morg_dict

    Returns: 
        "Employed" - is employed
        "Unemployed" - not employed
        "" - Neither 
    ''' 
    if rowdata[STATUS] == "Looking" or rowdata[STATUS] == "Layoff": 
        return "Unemployed" 
    elif rowdata[STATUS] == "Working":
        return "Employed"
    else: 
        return ""

def remove_year_duplicates(filename_list, index_year_starts = 6,
    index_year_ends = 8): 
    '''
    Removes filenames with the same year, where the bigger csv 
    dataset is chosen. 
    '''
    filename_list_2 = [filename_list[0]] 

    for filename in filename_list: 
        str_year = filename[index_year_starts:index_year_ends]
        for filename2_index, filename2 in enumerate(filename_list_2):
            if str_year not in filename2: 
                filename_list_2.append(filename)
                break
            else: 
                if ("mini" in filename2) and ("mini" not in filename): 
                    filename_list_2[filename2_index] = filename
                break

    return filename_list_2


def get_years(filename_list, index_year_starts = 6,
    index_year_ends = 8):
    '''
    Returns the years (string form) mentioned in the filename, ordered
    chrononoicaglly. Also returns the original order of that year and 
    the filename. 

    Ex. Format: [(year, former index)]

    Inputs: 
        filename_list: list of csv to extract years from 
        index_year_starts: index of string where year substring 
        begins 
        index_year_ends: index of string where year substring ends 

    Returns: 
        string of tuples in format (year, former index) 
    '''
    #first remove duplicates 

    years = [] 
    for i, filename in enumerate(filename_list): 
        former_index = i 
        str_year = filename[index_year_starts:index_year_ends]
        years.append((str_year, former_index, filename))

    years.sort()
    return years


def age_in_range(age_range, rowdata): 
    '''
    Returns: 
        True: if rowdata's age is in age_range, inclusive 
        False otherwise  
    ''' 

    age = rowdata.get(AGE, "")
    if type(age) == int: 
        return age >= age_range[0] and age <= age_range[1]
    return False


def increment_unemployed(counts_dict, rowdata, 
    var_of_interest): 
    '''
    Increments the total and the num of unemployed within 
    a certain variable of interest, given the data on a single 
    row in morg_dict. 

    Inputs: 
        counts_dict: a dictionary with values of all 
        the total and unemployed counts of each category of 
        var_of_interest.Value is list (total, unemployed)
        rowdata: dictionary with morg_dict individual data 
        var_of_interest: field in morg_dict 

    Returns: 
        Nothing, just edits counts_dict

    ''' 

    category_var = rowdata[var_of_interest]

    if get_employment_status(rowdata) == "Employed": 
        counts_dict[category_var][0] += 1

    elif get_employment_status(rowdata) == "Unemployed":
        counts_dict[category_var][0] += 1
        counts_dict[category_var][1] += 1


def get_unemployment_percents(morg_dict, age_range, var_of_interest):
    ''' 
    Filters the morg_dict via filter_morg_dict. Gives list 
    of unemployment percentages of each category 

    Inputs:
        filename_list: a list of MORG dataset file names
        age_rage: a tuple consisted of two integers
        var_of_interest: string (e.g., AGE, RACE or ETHNIC)

    Returns:
        list
    '''

    filename = build_file_interest(var_of_interest) #get all possible categories
    dict_of_interest = initialize_code(filename, False)

    counts_dict = {} 
    for code in dict_of_interest: 
        counts_dict[dict_of_interest[code]] = [0, 0] #s.t. all categories zero [total, employed]

    for hid in morg_dict: 
        if age_in_range(age_range, morg_dict[hid]): 
            increment_unemployed(counts_dict, morg_dict[hid], 
            var_of_interest)

    percentages_dict = {} 

    for category in counts_dict: 
        unemployed = counts_dict[category][1]
        total = counts_dict[category][0]
        if total == 0: #cant divide by zero
            percentages_dict[category] = "0.00"
        else: 
            percent = unemployed / total
            formatted_percent = get_format_percentage(percent)
            percentages_dict[category] = formatted_percent

    return percentages_dict

def get_format_percentage(percentage): 
    '''
    Formats the given percentage to two decimals. 

    Input: percentage: percent value float to be formated 
    '''

    formatted_percentage = str(percentage)

    if len(formatted_percentage) > PERCENT_LEN:
            formatted_percentage = "{:.2f}".format(percentage)
    if len(formatted_percentage) < PERCENT_LEN:
            formatted_percentage = formatted_percentage + "0"

    return formatted_percentage


def get_space_to_increment(value): 
    '''
    Returns a blank space whose length is COLUMN_WIDTH - length of value 

    Inputs: 
        Value: string
    ''' 

    space_to_increment = ""
    space_length = COLUMN_WIDTH - len(str(value))
    for i in range(space_length): 
        space_to_increment += " "

    return space_to_increment


def build_table(unemployment_percents):
    '''
    Starts to builds a list of strings for function calculate_unemployment_rates
    The fields of the table of strings, where the columns 
    are the years and the rows are the categories of var_of_interest. 
    Also adds the intial values based off of inputs. 
    NOTE: MAKE SURE TO ADD COL COLUMN_SEP AT THE VERY END!

    Inputs: 
        unemployment_percents: dictionary of unemployed peoples 
        by cateory 
    '''  

    table = [COLUMN_SEP + "Year" + get_space_to_increment("Year") 
    + COLUMN_SEP]
    
    category_index = list(unemployment_percents.keys())
    done = category_index.sort()
    for i in range(len(category_index)): #I dont directly use keys because alphabetical
        category = category_index[i]
        index_table = i + 1 #+1 since table[0] is the year

        category_table = category #value that will printed in table

        if(len(category) > COLUMN_WIDTH): 
            category_table = category[:COLUMN_WIDTH]

        table.append(COLUMN_SEP + category_table  
            + get_space_to_increment(category)
            + COLUMN_SEP)

    return table


def add_to_table(table, unemployment_percents, year):
    '''
    adds the data of unemployment_percents to table given the year. 

    Inputs: 
        table: an already-built table to be edited
        unemployment_percents: dictionary of unemployed peoples 
        by cateory 
        year: the year
    ''' 

    table[0] += year + get_space_to_increment(year) + COLUMN_SEP

    category_index = list(unemployment_percents.keys())
    category_index.sort()
    for i in range(len(category_index)): #I dont directly use keys because of table
        index_table = i + 1 #+1 since table[0] is the year
        category = category_index[i]
        percent = unemployment_percents[category]
        table[index_table] += percent + get_space_to_increment(percent) + COLUMN_SEP


def calculate_unemployment_rates(filename_list, age_range, var_of_interest):
    '''
    Output a nicely formatted table for the unemployment rates 
    for the specified age_rage, 
    further broken down by different categories in var_of_interest
    for the data specified in each file in filename_list 

    Inputs:
        filename_list: a list of MORG dataset file names
        age_rage: a tuple consisted of two integers
        var_of_interest: string (e.g., AGE, RACE or ETHNIC)

    Returns:
        list 
    '''

    if len(filename_list) == 0:
        return []

    filename_list_final = remove_year_duplicates(filename_list)
    years = get_years(filename_list_final)

    table = [] 

    YEAR_INDEX = 0 #in list years
    ORIGINAL_YEAR_INDEX = 1 #in list years
    
    for year in years:
        filename = filename_list_final[year[ORIGINAL_YEAR_INDEX]]
        input_dict = build_input_dict(filename) 
        morg_dict = build_morg_dict(input_dict)
        unemployment_percents = get_unemployment_percents(morg_dict,
            age_range, var_of_interest)
        if table == []:
            table = build_table(unemployment_percents)
        add_to_table(table, unemployment_percents, year[YEAR_INDEX])

    return table


def check_earnings_parameters(gender, race, ethnicity): 
    '''
    checks if the given paramters are valid

    Returns: 
        True if they are valid 
        False otherwise 
    ''' 

    return gender in valid_genders and race in valid_races and ethnicity in valid_ethnicities

def get_filtered_genders(gender): 
    '''
    Gives list of viable gender types given gender
    To be used for filtering categories for 
    calculate_weekly_earnings_stats_for_fulltime_workers. 

    Assumes gender is valid value. 

    Returns: 
        list of all viable gender categories 
    ''' 

    translated_genders = [gender] 
    if gender == ALL: 
        valid_gender_index_all = 2
        translated_genders = valid_genders[:valid_gender_index_all]
    return translated_genders


def get_filtered_race(race): 
    ''' 
    Gives list of the viable races to be included in the 
    calculate_weekly_earnings_stats_for_fulltime_workers. 
    Assume race is valid value. 

    Returns: 
        list of all viable races 
    ''' 


    translated_races = [race] 
    if race == ALL or race == OTHER: 
        race_codes_dict = initialize_code('data/race_code.csv', False) 
        translated_races = list(race_codes_dict.values())
        if race == OTHER:
            last_valid_race_index =  len(valid_races) - 2 #all,other
            for i in range(last_valid_race_index):
                translated_races.remove(valid_races[i])
    return translated_races

def get_filtered_ethnicity(ethnicity): 
    '''
    Gives a list of viable ethncities used ofr filtring in 
    calculate_weekly_earnings_stats_for_fulltime_workers. 
    Assumes ethnicity is valid. 

    Returns: 
        list of viable ethncities
    ''' 

    translated_ethnicities = ethnicity
    if ethnicity == HISPANIC or ethnicity == ALL: 
        ethnic_codes_dict = initialize_code('data/ethnic_code.csv', False) 
        translated_ethnicities = list(ethnic_codes_dict.values())
        if ethnicity == HISPANIC:
            translated_ethnicities.remove(NONHISPANIC)

    return translated_ethnicities


def translate_earnings_parameters(gender, race, ethnicity): 
    '''
    Gives a dictionary of a list of viable categories for each 
    parameter. Assume the parameters are valid. 
    '''

    translated_parameters = {GENDER: get_filtered_genders(gender),
    RACE: get_filtered_race(race), 
    ETHNIC: get_filtered_ethnicity(ethnicity)}

    return translated_parameters 

def generate_earnings_list(morg_dict, gender, race, ethnicity,
 viable_parameters):
    '''
    Returns a list of all the weekly earnings of 
    all fulltime workers who satisfy the criteria 

    Inputs: 
        morg_dict: dict 
        gender: query criteria for gender 
        race: query criteria for race 
        ethnicity: query criteria for ethnicity 
        viable_parameters: dictionary of lists of viable categories
    Returns: 
        List of earnings 
    ''' 

    list_earnings = [] 
    for hid in morg_dict: 
        individual = morg_dict[hid]
        satisfy_gender = individual[GENDER] in viable_parameters[GENDER] 
        satisfy_race = individual[RACE] in viable_parameters[RACE] 
        satisfy_ethnic = individual[ETHNIC] in viable_parameters[ETHNIC]
        
        satisfy_queries = satisfy_ethnic and satisfy_race and satisfy_gender
        if is_working(individual) and satisfy_queries: 
            list_earnings.append(morg_dict[hid][EARNWKE])

    return list_earnings


def calculate_weekly_earnings_stats_for_fulltime_workers(morg_dict, gender, 
                                                         race, ethnicity):
    '''
    Returns a 4-element list of earnings statics (mean, median, min, and max) 
    for all fulltime workers who satisfy the given query criteria 

    Inputs:
        morg_dict: dict 
        gender: query criteria for gender 
        race: query criteria for race 
        ethnicity: query criteria for ethnicity 

    Returns:
        A 4-element list
    '''

    earnings_stats = [0.0] * 4

    if not check_earnings_parameters(gender, race, ethnicity): 
        return earnings_stats
    viable_parameters = translate_earnings_parameters(gender, race, 
        ethnicity)
    earnings_list = generate_earnings_list(morg_dict, gender,
        race, ethnicity, viable_parameters)

    if len(earnings_list) == 0: 
        return earnings_stats

    earnings_stats[MEAN_INDEX] = mean_list(earnings_list)
    earnings_stats[MEDIAN_INDEX] = median_list(earnings_list)
    earnings_stats[MAX_INDEX] = max(earnings_list)
    earnings_stats[MIN_INDEX] = min(earnings_list)

    return earnings_stats


def mean_list(l): 
    '''
    Returns mean of list l. L must be of integers
    '''

    sum = 0 
    for x in l: 
        sum += x 
    return sum/len(l)

def median_list(l):
    '''
    Finds the median value of l. Must be integers list
    '''

    l.sort()
    if len(l) % 2 == 0: #magic numbers to show even... kappa
        median = (l[int(len(l)/2)] + l[int(len(l)/2 - 1)])/2
    else: 
        median = l[int(len(l)/2)]

    return median