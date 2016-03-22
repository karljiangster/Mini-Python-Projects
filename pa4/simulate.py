# CS121 A'15: Polling places
#
# Karl Jiang
#
# Main file for polling place simulation

import json
import math
import os
import random
import sys
import time
from voter_sample import Voter_List, Voter
from precinct import Precinct


def simulate_election_day(params):
    '''
    Simulate a single election day.

    Input:
        params: configuration to simulate

    Output:
        True if the specified configruation was suffient to meet the
        threshold for one simulated election day, false otherwise.
   
    '''

    voter_sample = Voter_List(params)
    precinct = Precinct(params["number_of_booths"])
    count_overtime = 0
    count_voted = 0

    
    t = voter_sample.get_first_voter().arrival_time

    for voter in voter_sample.voters: 
        if precinct.booths_full(): 
            t = precinct.remove_voter()[0] 
        t = max(t, voter.arrival_time)
        if t - voter.arrival_time > params["target_waiting_time"]: 
            count_overtime += 1 
        departure_time = t + voter.voting_time
        precinct.add_voter(departure_time, voter)
    
    return count_overtime * 100 < params["threshold"] * voter_sample.get_num_voters()
    

def run_trials(params):
    '''
    Run trials on the configuration specified by the parameters file.

    Inputs: 
        params: simulation parameters
    
    Result:
        Likelihood that the given number of machines is sufficient for
        the specified configuration.
    '''
    count = 0.0
    for t in range(params["num_trials"]):
        if simulate_election_day(params):
            count = count + 1.0
    
    return count/params["num_trials"]


def setup_params(params_filename, num_booths):
    '''
    Set up the paramaters data structure and set the
    seed for the random number generator

    Inputs:
        params_filename: name of the simulation parameters file
        num_booths: the number of booths to simulate
    '''
    if not os.path.isfile(params_filename):
        print("Error: cannot open parameters file " + params_filename)
        sys.exit(0)

    if num_booths <= 0:
        print("Error: the number of voting booths must be positive")
        sys.exit(0)

    params = json.load(open(params_filename))
    params["number_of_booths"] = num_booths

    if "seed" in params:
        seed = params["seed"]
    else:
        seed = int(time.time())
        params["seed"] = seed

    random.seed(seed)

    return params


if __name__ == "__main__":
    usage_str = "usage: python {0} [parameters filename] [number of voting booths]".format(sys.argv[0])
    # process arguments
    num_booths = 1
    params_filename = "params.json"
    if len(sys.argv) == 2:
        params_filename = sys.argv[1]
    elif len(sys.argv) == 3:
        params_filename = sys.argv[1]
        num_booths = int(sys.argv[2])
    elif len(sys.argv) > 3:
        print(usage_str)
        sys.exit(0)

    params = setup_params(params_filename, num_booths)
    rv = run_trials(params)

    # print the parameters and the result
    for key in sorted(params):
        print(key + ": " + str(params[key]))
    print()
    print("result: " + str(rv))


        



            
            
            

    
