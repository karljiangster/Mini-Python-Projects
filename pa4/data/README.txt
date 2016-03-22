# CS121: Polling place
# Sample parameter files along with some debugging output

====== ORIGINAL distribution data files ====== 

params0.json: tiny precinct (10 voters) that is open for only an hour, 1 trial run
params0-voter-sample-1.txt: state of the voters after simulating 1 election day with 1 machine
params0-voter-sample-2.txt: state of the voters after simulating 1 election day with 2 machines
params0-voter-sample-4.txt: state of the voters after simulating 1 election day with 4 machine

params1.json: same tiny precinct as params0, but with 3 trial runs
params1-voter-sample-1.txt: state of the voters after simulating 3 election days with 1 machine
params1-voter-sample-2.txt: state of the voters after simulating 3 election days with 2 machines
params1-voter-sample-4.txt: state of the voters after simulating 3 election days with 4 machines

params2.json: larger precinct that is open longer, 1 trial run
params2-voter-sample-1.txt: state of the voters after simulating 1 election day with 1 machine

params3.json: larger precinct that is open longer, 2 trial runs.  The
  second trial run should have fewer than 500 voters,
params3-voter-sample-1.txt: state of the voters after simulating 2 election days with 1 machine
params3-voter-sample-3.txt: state of the voters after simulating 2 election days with 3 machines

README.txt: this file

====== New files for exact voter generation approach  ====== 

params1-exact-expected-1.txt: expected per election day results when simulating params1 precinct with 1 machine 
params1-exact-expected-2.txt: expected per election day results when simulating params1 precinct with 2 machines
params1-exact-expected-4.txt: expected per election day results when simulating params1 precinct with 4 machines

params1-exact-voter-sample-1.txt: state of the voters after simulating params1 precinct with 1 machine 
params1-exact-voter-sample-2.txt: state of the voters after simulating params1 precinct with 2 machines 
params1-exact-voter-sample-4.txt: state of the voters after simulating params1 precinct with 4 machines 

params2-exact-expected-6.txt: expected per election day results when simulating params2 precinct with 6 machines
params2-exact-expected-7.txt: expected per election day results when simulating params2 precinct with 7 machines
params2-exact-expected-8.txt: expected per election day results when simulating params2 precinct with 8 machines

params2-exact-voter-sample-6.txt: state of the voters after simulating params2 precinct with 6 machines
params2-exact-voter-sample-7.txt: state of the voters after simulating params2 precinct with 7 machines
params2-exact-voter-sample-8.txt: state of the voters after simulating params2 precinct with 8 machines

====== New files for the approach that generates an extra voter when a voter arrives late (intermediate) generation ====== 

params1-intermediate-expected-1.txt: expected per election day results when simulating params1 precinct with 1 machine 
params1-intermediate-expected-2.txt: expected per election day results when simulating params1 precinct with 2 machines
params1-intermediate-expected-4.txt: expected per election day results when simulating params1 precinct with 4 machines

params1-intermediate-voter-sample-1.txt: state of the voters after simulating params1 precinct with 1 machine 
params1-intermediate-voter-sample-2.txt: state of the voters after simulating params1 precinct with 2 machines 
params1-intermediate-voter-sample-4.txt: state of the voters after simulating params1 precinct with 4 machines 

params2-intermediate-expected-6.txt: expected per election day results when simulating params2 precinct with 6 machines
params2-intermediate-expected-7.txt: expected per election day results when simulating params2 precinct with 7 machines
params2-intermediate-expected-8.txt: expected per election day results when simulating params2 precinct with 8 machines

params2-intermediate-voter-sample-6.txt: state of the voters after simulating params2 precinct with 6 machines
params2-intermediate-voter-sample-7.txt: state of the voters after simulating params2 precinct with 7 machines
params2-intermediate-voter-sample-8.txt: state of the voters after simulating params2 precinct with 8 machines


====== New files for extra voter generation approach  ====== 

params1-extra-expected-1.txt: expected per election day results when simulating params1 precinct with 1 machine 
params1-extra-expected-2.txt: expected per election day results when simulating params1 precinct with 2 machines
params1-extra-expected-4.txt: expected per election day results when simulating params1 precinct with 4 machines

params1-extra-voter-sample-1.txt: state of the voters after simulating params1 precinct with 1 machine 
params1-extra-voter-sample-2.txt: state of the voters after simulating params1 precinct with 2 machines 
params1-extra-voter-sample-4.txt: state of the voters after simulating params1 precinct with 4 machines 

params2-extra-expected-6.txt: expected per election day results when simulating params2 precinct with 6 machines
params2-extra-expected-7.txt: expected per election day results when simulating params2 precinct with 7 machines
params2-extra-expected-8.txt: expected per election day results when simulating params2 precinct with 8 machines

params2-extra-voter-sample-6.txt: state of the voters after simulating params2 precinct with 6 machines
params2-extra-voter-sample-7.txt: state of the voters after simulating params2 precinct with 7 machines
params2-extra-voter-sample-8.txt: state of the voters after simulating params2 precinct with 8 machines

