# CS121 A'15: Polling places
#
# Karl Jiang
#
# file to represent voter

import json
import math
import os
import random
import sys
import time


class Voter(object): 
    '''
    A Class to represent a Voter in the Markov process. 
    Includes the time the voter arrives at the polls and 
    the amount of time the voter will take to vote. 

    For Debugging Purposes: also includes 
        - vid: unique identifier (Voter ID)
        - arrival_time: the time the voter is assigned to a voting
        booth
    ''' 

    VOTER_ID = 0 
    
    def __init__(self, arrival_time, voting_time):  
        self.vid = Voter.VOTER_ID
        Voter.VOTER_ID += 1

        self.arrival_time = arrival_time
        self.voting_time = voting_time

    @property 
    def arrival_time(self): 
        return self._arrival_time 

    @arrival_time.setter
    def arrival_time(self, arrival_time): 
        self._arrival_time = arrival_time

    @property 
    def voting_time(self): 
        return self._voting_time 

    @voting_time.setter 
    def voting_time(self, voting_time): 
        self._voting_time = voting_time

    
    def __str__(self):
        return "Voter ID: {}, arrival_time: {:4f}, voting_time: {} \n".\
            format(self.vid, self.arrival_time, self.voting_time)
    
    
    def __repr__(self):
        return str(self)


