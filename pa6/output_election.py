# CS121 Linear regression assignment
# 
# Karl Jiang, karljiang 
#
# Generate plots and print text answers for the ELECTION data
#
import sys
from model import linear_regression, apply_beta, read_file, Model, r_squared_table\
, compute_r_squared, print_model, get_highest_pair, forward_selection_r_squared, \
output_sel, select_best_k, test_foward_select

# useful defined constants for the election data
COUNTY_DATA_COLS = range(0, 11)
VOTE_DIFFERENCE_COL = 11

<<<<<<< HEAD
file = "election"
variables, data = read_file("data/{}/training.csv".format(file))

if __name__ == "__main__":
    
        #Task 1a 
    print(file, "Task", "1A")
    print(r_squared_table(variables, data, CRIME_TOTAL_COL) )
    print() #\n

    #Task 1b
    print(file, "Task", "1B")
    model_1b = Model(variables, data, CRIME_TOTAL_COL, list(COMPLAINT_COLS) )
    r2 = compute_r_squared(model_1b.beta, model_1b.pre_col, model_1b.dep_col)
    print(print_model (model_1b.pre_var, r2) ) 
    print()#\n

    #Task 2
    print(file, "Task", "2")
    print(get_highest_pair(variables, data, list(COMPLAINT_COLS), CRIME_TOTAL_COL) )
    print() #\n

    #Task 3a
    print(file, "Task", "3a")
    sel_dict = forward_selection_r_squared(variables, data, \
        list(COMPLAINT_COLS), CRIME_TOTAL_COL)
    print(output_sel(sel_dict))
    print() #\n


    #Task 3b
    print(file, "Task", "3b")
    threshold_3b1 = 0.1
    task_3b1 = select_best_k(sel_dict, threshold_3b1)
    print( "Threshold", threshold_3b1, print_model( task_3b1[Model.VARIABLES], \
        task_3b1[Model.R2] ) )

    threshold_3b2 = 0.01
    task_3b2 = select_best_k(sel_dict, threshold_3b2)
    print( "Threshold", threshold_3b2, print_model( task_3b2[Model.VARIABLES], \
        task_3b2[Model.R2] ) )
    print() #\n


    #Task 4
    print(file, "Task", "4")
    t_variables, t_data = read_file("data/{}/testing.csv".\
        format(file) )
    sel_indexes = sel_dict[1][Model.INDEXES]
    print(test_foward_select(sel_indexes, variables, data, \
        t_data, CRIME_TOTAL_COL) )
    print() #\n 
