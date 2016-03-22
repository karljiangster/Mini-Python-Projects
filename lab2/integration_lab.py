def f(x):
    '''
    Real valued square function  f(x) == x^2 
    '''

    return x*x

def integrate():
    # Your code here
    n = 1000 # decide on the number of rectangles  
    dx = 1/n # compute the width of the rectangles
    totalArea = 0 # use a loop to compue the total area
    for i in range(n):
        height = f(i * dx) 
        width = dx
        totalArea = totalArea + (height * width)
    # print the result
    print(totalArea)
    # remove the next line




