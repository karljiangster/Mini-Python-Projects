import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/ferryloading4
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

<<<<<<< HEAD
def solve(l, m, cars, side = "left"): 
    
    if len(cars) <= 0 : 
        return 0

    #get the max you can get on your side 
    i = 0 
    filled = 0  
    while i < len(cars): 
        if cars[i][1] == side: 
            if cars[i][0] + filled <= l * 100: 
                filled += cars[i][0]
                cars.pop(i)
            else: 
                break 
        else: 
            i += 1 

    return 1 + solve(l, m, cars, switch_sides(side) ) #move to the next side


def switch_sides(side): 
    if side == "left": 
        return "right"
    return "left"
=======

def solve(l, m, cars):
    # Your code here
    return 0
>>>>>>> 7d55802b2f6743c7ffa2502be0f3a062f47c2f81

if __name__ == "__main__":
    tokens = sys.stdin.read().split()

    ntests = int(tokens.pop(0))

    for i in range(ntests):
        l = int(tokens.pop(0))
        m = int(tokens.pop(0))
        cars = []
        for j in range(m):
            cars.append( (int(tokens.pop(0)), tokens.pop(0)) )

        print(solve(l, m, cars))


