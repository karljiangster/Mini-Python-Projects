# CS121 A'15: Polling places
#
# Karl Jiang
#
# file for representing a precinct 


import json
import math
import os
import random
import sys
import time
from queue import PriorityQueue
from voter_sample import Voter_List, Voter


class Precinct(object): 
    ''' 
    Represents a precinct with N number of booths. Capable of  
    adding voters to and removing (in increasing order of departure time) 
    voters from voting booths.

    Also contains an attribute that can track voters who are currently 
    occupying booths and determine which voters should be departing next. 

    Note each voter's priority is its departure time.  
    (voters with earlier departure times get removed first)
    '''

    def __init__(self, num_booths): 
        ''' 
        Constructs the precinct. 

        Inputs: 
            num_booths: max number of booths for voters. If full, 
            then voters are going to have to wait. 
        ''' 

        self.booths = PriorityQueue(maxsize = num_booths)

        @property 
        def booths(self): 
            return self._booths

        @booths.setter
        def booths(self, booths): 
            self._booths = booths 


    def add_voter(self, departure_time, voter): 
        '''
        Adds a voter to one of the booths. Note that the priority 
        parameter in queue.put function is the departure_time
        of the voter

        Inputs: 
            voter: a voter to be added. 
        '''
        self.booths.put((departure_time, voter))
        

    def remove_voter(self): 
        '''
        Removes the voter from the booths PriorityQueue by the earliest 
        departure_time

        return: 
            tuple of (time voter was removed, the voter that was removed) 
        ''' 

        return self.booths.get()

    def booths_full(self): 
        '''
        Returns true if all the booths are occupied.
        '''
        return self.booths.full()

    def booths_is_empty(self): 
        '''
        Returns true if all the booths are empty. 
        '''
        return self.booths.empty()

    def __str__(self): 
        return str(self.booths)



