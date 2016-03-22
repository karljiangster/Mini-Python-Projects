# CS121 Lab 3: Functions

import math
import numpy
import pylab

def sinc(x):
    '''
    Real valued sinc function  f(x) == sin(x)/x

    Inputs:
        x: float

    Return: float
    '''
    # Make sure we don't divide by zero  
    if x != 0:
        return math.sin(x) / x
    else:
        # sin(0) / 0 == 1
        return 1.0

def square(x): 
    return x * x 

def plot_square(left_boundary, right_boundary, dx):
    '''
    Plot the square function from from left_boundary...right_boundary
    with increments of size dx.
    '''
    xs = numpy.arange(left_boundary, right_boundary, dx) 

    # apply the sinc function onto the xs list
    ys = []
    for x in xs:
        ys.append(square(x))
                
    # plot the figure
    plot(xs,ys)


def plot_sinc(left_boundary, right_boundary, dx):
    '''
    Plot the sinc function from from left_boundary...right_boundary
    with increments of size dx.
    '''
    xs = numpy.arange(left_boundary, right_boundary, dx) 

    # apply the sinc function onto the xs list
    ys = []
    for x in xs:
        ys.append(sinc(x))
                
    # plot the figure
    plot(xs,ys)

def plot(xs,ys, name = "Graph", ylabel = "y-axis", xlabel = "x-axis"): 

    pylab.figure()
    pylab.plot(xs,ys)
    pylab.title(name)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.show()

def go():
    dx = .01
    left_boundary = -10
    right_boundary = 10 

    plot_sinc(left_boundary, right_boundary, dx)
