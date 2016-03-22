# CS121 A'15: Benford's Law
#
# Anne Rogers
# June 2015
#
# Plotting code for Benford's Law assignment

import benford
import util
import sys
import pylab as plt


def plot_benford_dist(dollar_amounts, num_digits, output_filename):
    '''
    Plot the actual and expected benford distributions

    Inputs:
        dollar_amounts: a non-empty list of positive dollar amounts as
            strings
        ub: upper bound (9 for 1 leading digit, 99 for 2 leading digits, ect)
        output_filename: the name of the file that will hold the
            generated plot
    '''
    assert(num_digits > 0)

    lb = 10**(num_digits-1)
    ub = 10**(num_digits)

    digits = range(lb,ub)

    # start a new figure
    f = plt.figure()

    # plot expected distribution
    expected = benford.compute_expected_benford_dist(num_digits)
    if len(expected) != len(digits):
        print("Length of actual result ({}) returned from compute_expected_benford_dist does not match the expected length ({})".format(len(expected), len(digits)))
        sys.exit(0)

    plt.scatter(digits, expected, color="red", zorder=1)

    # plot actual distribution
    actual = benford.compute_benford_dist(dollar_amounts, num_digits)
    if len(actual) != len(digits):
        print("Length of actual result ({}) returned from compute_benford_dist does not match the expected length ({})".format(len(actual), len(digits)))
        sys.exit(0)

    plt.bar(digits, actual, align="center", color="blue", zorder=0)

    # set hash marks for x axis.
    plt.xticks(range(lb, ub, 10**(num_digits-1)))

    # compute limits for the y axis
    max_val = max(max(expected), max(actual))
    y_ub = max_val + max_val * .1
    plt.ylim(0,y_ub)

    # add labels
    plt.title("Actual (blue) and expected (red) Benford distributions")
    if num_digits ==1: 
        plt.xlabel("Leading digit")
    else:
        plt.xlabel("Leading digits")
    plt.ylabel("Proportion")

    plt.savefig(output_filename)


if __name__=="__main__":
    if len(sys.argv) != 5:
        print("usage: python benford.py <input filename> <column number>  <num digits> <output filename>")
    else:
        input_filename = sys.argv[1]
        data = util.read_column_from_csv(input_filename, int(sys.argv[2]), True)
        num_digits = int(sys.argv[3])
        output_filename = sys.argv[4]
        plot_benford_dist(data, num_digits, output_filename)
        # print only four digits after the decimal point
        print("MAD: {0:.4}".format(benford.compute_benford_MAD(data, num_digits)))
                                   
