import math
import pylab
import numpy

def sinc(x):
    if x != 0:
        return math.sin(x) / x;
    else:
        return 1;

def plot_sinc(increment):
    X = numpy.arange(-10, 10, increment) # Compute Xs using range or numpy.arange
    Y = [] # Compute Ys using a loop
    for i in X:
        Y.append(sinc(i))
    pylab.plot(X, Y) # Call plot
    pylab.show() # Call show 
    # remove the next line

