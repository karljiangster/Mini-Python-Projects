import csv
import numpy as np
import matplotlib.pyplot as plt

#Constants for figure sizes
FIGWIDTH = 12
FIGHEIGHT = 8


def read_csv(filename, include_header):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

        rv = []
        if include_header:
            rv = [header]

        for row in reader:
            # strip the while space from around the values
            row = [x.strip() for x in row]
            rv.append(row)
        return rv

    # will only get here if the open failed.
    return None



# Function to plot histograms
def plot_histogram(histogram, min_val, max_val, filename): 
    fig, ax = plt.subplots(figsize=(FIGWIDTH, FIGHEIGHT))

    labels=[0]*len(histogram)
    for x in range(len(labels)):
        step = (max_val - min_val) / len(histogram)
        labels[x] = "[" + str(x*step + min_val)  + ", " + str(x*step+step+min_val) + ")" 

    n_groups = len(histogram)  
    index = np.arange(n_groups)
    bar_width = .5
    opacity = .5
    colors = 'b'
    rects = plt.bar(index, histogram, bar_width, alpha = opacity, color = colors)
    ax.set_xticks(index+bar_width/2)
    ax.set_xticklabels(labels, rotation='vertical')
    plt.tight_layout()

    fig.savefig(filename)

