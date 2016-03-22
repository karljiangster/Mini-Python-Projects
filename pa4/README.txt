CS 121: Polling places

simulate.py: skeleton code for the simulator

params.json: same as data/params0.json. Included to provide a default
  parameters file for use by simlate.py.

data: sample precincts and voter samples.

test_simulate_election_day.py: original code for testing your simulator

************* 

These test files are new.  All implementations should be able to pass
test_simulate_one_election_day.py.  

Which test you should use for simulating multiple days depend on the
way in which you choose to generate voters.

Let M be the number of voters who will be allowed to vote on election
day and N be the number of voters specified in the parameters file for
the precinct.  There are at least three ways to generate the voters:

EXACT: The exact method generates M voters and will draw one extra
       random number for the gap if M < N, that is, if at least one
       voter arrives late.

       Use test_exact_voter_simulate_multiple_elections_days.py to test
       your code if your solution works this way.

INTERMEDIATE: The intermediate method generates M voters if all the
              voters arrive before the polls and will generate one
              extra voter if at least one voter arrives late.  (That
              is, will draw both the gap and the voting time and will
              use up on ID in the voter class.)

              Use test_intermediate_voter_simulate_multiple_elections_days.py to
              test your code if your solution works this way.

EXTRA: The extra method generates always generates M+1 voters.

       Use test_extra_voter_simulate_multiple_elections_days.py to
       test your code if your solution works this way.

README.txt: this file

