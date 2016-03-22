# CS121 A'15: Polling places
#
# Karl Jiang
#
# Poisson file for generating voter samples
# to b used in polling place simulation

import json
import math
import os
import random
import sys
import time
from voter import Voter


class Voter_List(object): 
    '''
    Generates voter samples using a Poisson process. That is, 
    events occur continuously and independently of one another. We 
    can use the following fact to generate a voter sample: if the 
    number of arrivals in a given time interval [0,t] follows the 
    Poisson distribution, with mean t∗λ, then the gap between arrivals 
    times follow the exponential distribution with rate parameter 
    λ.
    '''

    def __init__(self, params): 
        ''' 
        Generates the voter sample given the params. See class 
        description to see how the voters generated. 

        Inputs: 
            params: dictionary with parameters such as the hours voting 
            will take place, number of voters... etc. 
        ''' 
        

        self.params = params 
        self.voters = []
        self.next_voter_index = 0 

        minutes_per_hour = 60

        minutes_open = (params["hours_open"] * minutes_per_hour) 
        arrival_rate = params["num_voters"] / minutes_open

        t = 0

        while t < minutes_open and len(self.voters) <= params["num_voters"]: 
            t += random.expovariate(arrival_rate)
        
            voting_time = random.expovariate(1/params["voting_mean"])
            voter = Voter(t, voting_time)
            self.voters.append(voter)

        self.voters.pop()
        
    @property
    def voters(self): 
        return self._voters

    @voters.setter
    def voters(self, voters): 
        self._voters = voters

    @property
    def next_voter_index(self): 
        return self._next_voter_index

    @next_voter_index.setter
    def next_voter_index(self, next_voter_index): 
        self._next_voter_index = next_voter_index


    def has_next(self): 
        '''
        Returns True if next_voter_index is not out of bounds. False 
        otherwise. 
        '''

        return self.next_voter_index < len(self.voters)

    def next_voter(self): 
        ''' 
        Gets the next voter in the voter sample. Should use has_next 
        before calling this function or else will return empty voter
        '''
        if not self.has_next(): 
            return  
        voter = self.voters[self.next_voter_index]
        self.next_voter_index += 1 

        return voter 

    def get_first_voter(self): 
        '''
        Returns the first voter in the sample.
        ''' 

        return self.voters[0]

    def get_num_voters(self): 
        '''
        Returns the total number of voters in the voter sample 
        '''

        return len(self.voters)

    def next_arrival_time(self): 
        '''
        Returns the next arrival time of the next voter 
        WITHOUT incrementing next_voter_index
        '''  

        return self.voters[next_voter_index + 1].arrival_time


    def __str__(self): 
        return self.voters.__str__()
        





            
            
            

    
