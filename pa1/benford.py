# CS121 A'15: Benford's Law
#
# Functions for evaluating data using Benford's Law.
#
# Karl Jiang

import math

def extract_leading_digits_single(amount, num_digits):
    '''
    Given a positive floating point number and a number of 
    digits, extract the specified number of leading digits

    Inputs:
        amount: float
        num_digits: the number of leading digits to 
        extract from the amount.

    Returns:
        integer
    '''
    assert(num_digits > 0)
    assert(amount > 0)

    a = math.trunc(10**(-math.floor(math.log10(amount)) + num_digits - 1) * amount)

    return a


def extract_leading_digits_from_list(dollar_amounts, num_digits):
    '''
    New list that contains the leading digits for each item 
    in the input list as integers.
    
    Inputs:
        dollar_amounts - takes a list of strings that 
        represent positive amounts in dollars 
        num_digits - number of digits to extract from 
        dollar_amounts

    returns - list of integers
    '''
    dollar_amounts_int = [] 

    if(len(dollar_amounts) == 0): 
        return dollar_amounts

    for x in dollar_amounts:
        float_dollar = float(x[1:len(x)]) #convert to float value
        dollar_lead = extract_leading_digits_single(float_dollar, num_digits)
        dollar_amounts_int.append(dollar_lead) 
    
    return dollar_amounts_int


def compute_expected_benford_dist(num_digits):
    '''
    List of floats with the expected distribution (benford)
    Each index in this list corresponds to the expected 
    frequency of [lowest num with num_digits: highest num 
    with num_digits] as a leading digit.

    Inputs: 
        num_digits - is the number of digits 
    
    Returns: 
        List of floats
    '''
    list_dist = [] #empty list for distribution

    min = 10 ** (num_digits - 1) #min number of num_digits
    max = 10 ** num_digits #max number of num_digits

    for x in range(min, max): #assign floats to dist list
        list_dist.append(math.log10(1 + 1/x))
    return list_dist


def compute_benford_dist(dollar_amounts, num_digits):
    '''
    Given dollar_amounts and num_digits, returns list of 
    probabillity of each leading digit of each 
    element of dollar_amounts[i]

    Inputs: 
        dollar_amounts - non empty list strings 
        num_digits - number of digits 
    
    Returns: 
        List of floats
    '''

    assert num_digits > 0
    assert len(dollar_amounts) > 0

    min = 10 ** (num_digits - 1) 
    max = 10 ** num_digits 

    amounts_list = extract_leading_digits_from_list(dollar_amounts, num_digits) 
    count = [0] * len(range(min, max)) 
    for i in amounts_list: #get counts of each leading digit
        count[i - min] = count[i - min] + 1 # i - min to adjust indexes 
    frequency = [x / len(amounts_list) for x in count] 
    
    return frequency


def compute_benford_MAD(dollar_amounts, num_digits):
    '''
    The mean absolute difference (MAD) between the 
    Benford distribution and the frequencies of
    dollar_amounts

    Inputs: 
        dollar_amounts - list of strings that represent 
        positive amounts in dollars
        num_digits - number of leading digits
    
    Returns:
            float
    '''
    
    input_list = compute_benford_dist(dollar_amounts, num_digits)
    expected = compute_expected_benford_dist(num_digits)
    mean_abs_difference = 0 
    for i in range(len(input_list)):
        mean_abs_difference = mean_abs_difference + math.fabs(input_list[i] - expected[i]) 

    mean_abs_difference = mean_abs_difference / len(input_list)
    return mean_abs_difference



