#Karl Jiang 
import sys
import csv
import os.path
import operator
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from collections import Counter 
import numpy as np


# Candidate information (as described in assignment writeup)
CANDIDATE_NAMES = {"bush":      "Jeb Bush",
                   "carson":    "Ben Carson",
                   "christie":  "Chris Christie",
                   "cruz":      "Ted Cruz",
                   "fiorina":   "Carly Fiorina",
                   "gilmore":   "Jim Gilmore",
                   "graham":    "Lindsey Graham",
                   "huckabee":  "Mike Huckabee",
                   "jindal":    "Bobby Jindal",
                   "kasich":    "John Kasich", 
                   "pataki":    "George Pataki",
                   "paul":      "Rand Paul",
                   "perry":     "Rick Perry", 
                   "rubio":     "Marco Rubio", 
                   "santorum":  "Rick Santorum", 
                   "trump":     "Donald Trump", 
                   "walker":    "Scott Walker",
                   "chafee":    "Lincoln Chafee",
                   "clinton":   "Hillary Clinton",
                   "omalley":   "Martin O'Malley",
                   "sanders":   "Bernie Sanders",
                   "webb":      "Jim Webb"}

GOP_CANDIDATES = ['bush', 'carson', 'christie', 'cruz', 'fiorina', 'gilmore', 'graham', 'huckabee', 
                  'jindal', 'kasich', 'pataki', 'paul', 'perry', 'rubio', 'santorum', 'trump', 'walker']

DEM_CANDIDATES = ['chafee', 'clinton', 'omalley', 'sanders', 'webb']

ALL_CANDIDATES = GOP_CANDIDATES + DEM_CANDIDATES


# Size of the figures (these are the values you should pass
# in parameter "figsize" of matplotlib's "figure" function)
# Note: For task 4, use FIGWIDTH*2
FIGWIDTH = 12
FIGHEIGHT = 8


# Start and end time (in seconds) of the debate
DEBATE_START = 86400
DEBATE_END = 97200
# Maximum time (in seconds) of the dataset
MAX_TIME = 183600


# This function generates colors that can be passed to matplotlib functions
# that accept a list of colors. The function takes one parameter: the number
# of colors to generate. Using this function should result in the same colors
# shown in the assignment writeup.
def get_nice_colors(n_colors):
    return cm.Accent( [1 - (i/n_colors) for i in range(n_colors)] )



################################################
#
# Your functions go here
#
# Call your functions from the __main__ block
#
################################################

class Tweets:
  

  def __init__(self, candidates, seconds):
    
    self.candidates = candidates
    self.seconds = seconds


  def get_total_mentions(self, gop = False, dem = False): 
    '''
    Returns total mentions. Filter for gop or dem if they are True. 
    ''' 
    count = 0 
    for c in self.candidates: 
      mentions = c.split("|")
      if gop: 
        for cand in mentions: 
          if cand in GOP_CANDIDATES: 
            count += 1 
      elif dem: 
        for cand in mentions: 
          if cand in DEM_CANDIDATES: 
            count += 1
      else: 
        count += len(mentions)

    return count 


  def mentions_count(self): 
    '''
    Returns dictionary of counts of mentions. At index is the mentions - 1. 
    ''' 
    counts = {} 
    for c in self.candidates: 
      mentions = len( c.split("|") )
      if counts.get(mentions, None): 
        counts[mentions] += 1 
        if ( not counts.get(mentions - 1, None) ) and mentions != 1: 
          counts[mentions - 1] = 0 
      else: 
        counts[mentions] = 1 

    return counts  

  def combs_count(self, n, gop = False): 
    '''
    Returns all the counts of the n length combinations of mentioned 
    candidates in tweets. 
    If GOP = True, will only inclde GOP combinations
    (Returns dictionary with the candidate(s) as key)
    '''
    counts = {}
    for cands in self.candidates:
      c = cands.split("|") 
      if len(c) >= n: 
        combs = combinations(c, n)
        Tweets.increment_combinations(counts, combs, gop)
    return counts

  def top_pairs(self, n, gop = False): 
    '''
    Returns the top n pairs. For Task 2
    '''
    pairs = Counter( self.combs_count(2, gop) )
    return pairs.most_common(n)


  def get_percent_mentions(self, gop, p_threshold = 0.03): 
    '''
    Returns dictionary of the percent mentions of each candidate.
    If < 3%, gets lumped into other. For Task 3 
    ''' 

    total_mentions = self.get_total_mentions(gop)
    counts = self.combs_count(1, gop)
    percentages = {"other" : 0.0} 

    total = 0 
    for k, v in counts.items():
      percent = v / total_mentions 
      if percent < p_threshold: #less than 3%
        percentages["other"] += percent  
      else: 
        percentages[k] = percent 
      total += percent 

    return Counter(percentages).most_common(len(list(percentages.keys())))


  @staticmethod
  def increment_combinations(c_counts, candidates, gop): 
    '''
    Determines if the list of candidate combinations is qualified, which is 
    dependnet in gop status and if gop status even matters.
    Then increments c_counts dictionary. 

    Inputs: 
      c_counts: dictionary with keys as viable pairs of candidates 
      candidates: list with all possible combinations of candidates in a tweet 
      gop: boolean indicating if filtering for gop candidates 
    ''' 
    for c in candidates: 
      accept = True
      if gop: 
        for candidate in c: 
          if candidate not in GOP_CANDIDATES: 
            accept = False 
            break 
      if accept:
        c = sorted(c)
        key = "" 
        for candidate in c: 
          key += candidate + "|"
        if c_counts.get(key, None): 
          c_counts[key] += 1 
        else: 
          c_counts[key] = 1


  def gen_mentions_per(self, cands, interval): 
    '''
    Returns dictionary with key as the interval (ie min 0 - 9 will have key 0)
    and the value as a dictionary (key cand name and val number of mentions)

    Inputs: 
      cands: list of candidates 
      interval: int representing length of interval, in minutes 
    ''' 

    data = {} 

    for i, c in enumerate(self.candidates): 

      s = float(self.seconds[i])
      c_list = c.split("|")
      time_span = (s // (interval * 60) ) * interval

      if not data.get(time_span, None): #initialize the values in data 
        Tweets.init_values_per_min(data, time_span, cands, interval)

      for candidate in data[time_span]: #increment the values in data 
        if candidate in c_list: 
          data[time_span][candidate] += 1 
  
    return data 

  @staticmethod
  def init_values_per_min(data, time_span, cands, interval): 
    '''
    Used when key value in gen_mentions_per dict has not been generated.
    Edits data (the big dictionary that holds candidate tweet counts 
      at some time AKA the gen_mentions_per return value) 
    Note that it covers when there are no mentions of a particular 
    candidate at a certan time t. 
    ''' 

    cand_counts = {} 

    if (not data.get(time_span - interval, None) ) and time_span != 0:
      cand_counts_before = {} 
      for candidate in cands: 
        cand_counts[candidate] = 0 
        cand_counts_before[candidate] = 0
      data[time_span] = cand_counts
      data[time_span - interval] = cand_counts_before[candidate]
    else: 
      for candidate in cands: 
        cand_counts[candidate] = 0 
      data[time_span] = cand_counts



  def get_candidate_mentions_per_minute(self, cands, interval, period): 
    '''
    Returns a dictionary of key candidates and list values representing
    the number of mentions in some interval. Used for 4a

    Note: period is a range value of (start, end)
    '''
    data = self.gen_mentions_per(cands, interval)
    cands_mentions = {} 

    for t in period: 
      for candidate in cands: 
        if not cands_mentions.get(candidate, None): 
          if not data.get(t, None): 
            cands_mentions[candidate] = [0] 
          else: 
            cands_mentions[candidate] = [data[t][candidate]]
        else: 
          if not data.get(t, None): 
            cands_mentions[candidate].append(0)
          else: 
            cands_mentions[candidate].append(data[t][candidate])

    return cands_mentions


  def mention_minute_percent(self, cands, interval, period): 
    '''
    Returns dictionary from get_candidate_mentions_per_minute
    expressed as percents. For task 4b. 
    ''' 
    c_dict = self.get_candidate_mentions_per_minute(cands, interval, period)

    for time in range(len(period)): 
      total_mentions = 0 
      for c in c_dict: 
        total_mentions += c_dict[c][time] #jhave to run same loop twice to get total
      for c in c_dict: 
        if total_mentions != 0: 
          c_dict[c][time] = c_dict[c][time] / total_mentions

    return c_dict


def read_csv(file): 
  '''
  Reads CSV given the filename f (String), and returns Tweet class  
  ''' 
  with open(file) as f: 
    reader = csv.DictReader(f) 
    candidates = [] 
    seconds = [] 
    for row in reader: 
      candidates.append(row["candidates"])
      seconds.append(row["seconds"])

    return Tweets(candidates, seconds)


def combinations(lst,k):
    ''' 
    Returns all the combinations of length k in a list
    ''' 
    n = len(lst)
    if n == k:
        return [lst]
    if k == 1:
        return [[lst[i]] for i in range(n)]

    v1 = combinations(lst[:-1], k-1)
    v1new = [ i.append(lst[n-1]) for i in v1]
    v2 = combinations(lst[:-1], k)

    return v1+v2


def plot_mentions_count(tweets, save_to = None):
  '''
  Plots the counts of the number of mentions given a Tweets class.
  Note: used for task 1.  
  ''' 
  counts = tweets.mentions_count()

  fig = plt.figure(figsize = (FIGWIDTH, FIGHEIGHT))  
  plt.bar(range(len(counts)), counts.values(), log = True)
  plt.xticks(range(len(counts)), list(counts.keys()))

  plt.title("Number of Candidate Mentions per Tweet")
  plt.xlabel("Number of Mentions")
  plt.ylabel("Number of Tweets")

  plt.show()
  if save_to: 
    fig.savefig(save_to)



def plot_top_candidates(tweets, n, gop, save_to = None): 
  '''
  Plots the counts of top n candidate pair mentions given a Tweets class.
  Note: used for task 2.  
  ''' 
  counts = tweets.top_pairs(n, gop)

  pairs = [] 
  mentions = [] 
  for pair, ment in counts: 
    p = pair.split("|")
    c0 = CANDIDATE_NAMES[ p[0] ] 
    c1 = CANDIDATE_NAMES[ p[1] ]
    pairs.append(c0 + "\n" + c1)
    mentions.append(ment)

  

  fig = plt.figure(figsize = (FIGWIDTH, FIGHEIGHT)) 
  plt.bar(range(len(counts)), mentions)
  plt.xticks(range(len(counts)), pairs, rotation = 'vertical')

  if gop: 
    plt.title("Pairs of GOP Candidates Mentioned most Frequently together")
  else: 
    plt.title("Pairs of Candidates Mentioned most Frequently together")
  plt.xlabel("Number of Mentions")
  plt.ylabel("Number of Tweets")

  plt.show()
  if save_to: 
    fig.savefig(save_to)


def plot_percent_mentions(tweets, gop = False, save_to = None):
  '''
  Plots the percent mentions of each candidate (filtered for party)
  Used for Task 3.
  ''' 

  percents = tweets.get_percent_mentions(gop)

  candidates = [] 
  mentions = [] 
  for c, ment in percents:
    if c == "other": 
      other_v = ment 
    else:   
      candidates.append(CANDIDATE_NAMES[c[:-1]])
      mentions.append(ment)
  candidates.append("other")
  mentions.append(other_v)

  fig = plt.figure(figsize = (FIGWIDTH, FIGHEIGHT)) 

  plt.pie(mentions, labels = candidates, autopct='%1.1f%%')
  if gop: 
    plt.title("Percent of Mentions per GOP candidate")
  else: 
    plt.title("Percent of Mentions per candidate")
 
  plt.show() 
  if save_to: 
    fig.savefig(save_to)


def plot_per_min_debate(tweets, cands, interval, \
  start = DEBATE_START // 60, end = DEBATE_END // 60, tic_inc = 15, save_to = None): 
  '''
  Plots data from beg of debate to end. For Task 4a. 
  Note: start and end should be in minutes, not seconds
  '''

  fig = plt.figure(figsize = (FIGWIDTH, FIGHEIGHT))

  period = range(start, end, interval)
  c_dict = tweets.get_candidate_mentions_per_minute(cands, interval, period)

  y = np.row_stack()
  for candidate in c_dict: 
    plt.plot(period, c_dict[candidate], label = CANDIDATE_NAMES[candidate])

  if interval == 1: 
    plt.title("Mentions per Minute During Debate")
  else: 
    plt.title("Mentions per {} minutes before, during, and after debate".\
      format(interval))
  plt.xlabel("Time")
  plt.ylabel("Number of Tweets")
  plt.legend()

  ticks_range = range(start, end, tic_inc)
  labels = list(map(lambda x: str(x - start) + " min", ticks_range))
  plt.xticks(ticks_range, labels, rotation = 'vertical')
  plt.xlim( (start, end) )
  
  if save_to: 
    fig.savefig(save_to)
  plt.show()

def plot_stack_candidates(tweets, cands, interval, start = 0, \
  end = MAX_TIME // 60, tic_inc = 120, save_to = None): 
  '''
  Plots stackplot for the candidates in list cands over the time interval
  ''' 

  period = range(start, end, interval)
  percent_dict = tweets.mention_minute_percent(cands, interval, period)

  y = [] 
  fig = plt.figure(figsize = (FIGWIDTH, FIGHEIGHT))
  legends = [] 
  for candidate in percent_dict:
    y.append(percent_dict[candidate]) 
    legends.append(CANDIDATE_NAMES[candidate])
  plt.stackplot(period, y)

  plt.title("Percentage of Mentions per {} minutes before, during, \
    and after debate".format(interval))
  plt.xlabel("Time")
  plt.ylabel("Number of Tweets")
  plt.legend(y, legends)

  ticks_range = range(start, end, tic_inc)
  labels = list(map(lambda x: str(x - start) + " min", ticks_range))
  plt.xticks(ticks_range, labels, rotation = 'vertical')
  plt.xlim( (start, end) )
  plt.ylim( (0.0, 1.0))
  
  if save_to: 
    fig.savefig(save_to)
  plt.show()


if __name__ == "__main__":

    # The following code parses the command-line parameters. 
    # There is one required parameter (the CSV file) and an optional
    # parameter (the directory where the PNG files will be created;
    # if not specified, this defaults to "output/").
    #
    # This code results in two variables:
    #
    #  - csv_file: The data file to read
    #  - output_dir: The directory where the images should be generated

    if not 2 <= len(sys.argv) <= 3:
        print("Usage: python3 {} <data file> [<output directory>]".format(sys.argv[0]))
        sys.exit(1)
    else:
        csv_file = sys.argv[1]
        if not os.path.exists(csv_file) or not os.path.isfile(csv_file):
            print("{} does not exist or is not a file.".format(csv_file))
            sys.exit(1)
        if len(sys.argv) == 3:
            output_dir = sys.argv[2]
            if not os.path.exists(output_dir) or not os.path.isdir(output_dir):
                print("{} does not exist or is not a directory.".format(output_dir))
                sys.exit(1)
        else:
            output_dir = "./output"

    # Use the following file names to generate the plots
    TASK1_FILE = "{}/bar_num_mentions.png".format(output_dir)

    TASK2_GOP_FILE = "{}/bar_candidates_together_gop.png".format(output_dir)
    TASK2_ALL_FILE = "{}/bar_candidates_together_all.png".format(output_dir)

    TASK3_GOP_FILE = "{}/candidates_gop.png".format(output_dir)
    TASK3_ALL_FILE = "{}/candidates_all.png".format(output_dir)

    TASK4A_DURING_FILE = "{}/mentions_over_time_during.png".format(output_dir)
    TASK4A_FULL_FILE = "{}/mentions_over_time.png".format(output_dir)

    TASK4B_FILE = "{}/stackplot.png".format(output_dir)


    # Your code goes here, BUT NOT **ALL** YOUR CODE.
    #
    # You should write functions that do all the work, and then
    # call them from here.

    tweets = read_csv(csv_file)
    #Task 1 
    #plot_mentions_count(tweets, save_to = TASK1_FILE)
    #Task 2 
    #plot_top_candidates(tweets, 10, False, save_to = TASK2_ALL_FILE)
    #plot_top_candidates(tweets, 10, True, save_to = TASK2_GOP_FILE)
    #Task 3 
    #plot_percent_mentions(tweets, False, save_to = TASK3_ALL_FILE)
    #plot_percent_mentions(tweets, True, save_to = TASK3_GOP_FILE)
    #Task 4a
    '''
    plot_per_min_debate(tweets, ["trump", "fiorina", "bush", "carson"], 1, \
      save_to = TASK4A_DURING_FILE)
    plot_per_min_debate(tweets, ["trump", "fiorina", "bush", "carson"], 10 \
      ,start = 0, end = MAX_TIME // 60, tic_inc = 120, save_to = TASK4A_DURING_FILE)
    
    '''
    #Task 4b
    cands = ["trump", "fiorina", "bush", "carson", "cruz", "paul", "rubio"]
    plot_stack_candidates(tweets, cands, 10, save_to = TASK4B_FILE)
    
    #a = tweets.mentions_count()
    #b = tweets.get_candidate_mentions_per_minute(["carson", "trump", "bush"], 1)
    #c = tweets.gen_mentions_per(["carson"], 1)
    #print(max(list(c.keys())))
    #plot_per_min_debate(tweets, ["trump", "fiorina", "bush", "carson"], 1)
    


