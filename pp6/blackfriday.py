import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/blackfriday
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.


def solve(rolls):
    # Your code here.
    return None


if __name__ == "__main__":
    tokens = sys.stdin.read().split()

    n = int(tokens.pop(0))
    rolls = [int(tokens.pop(0)) for i in range(n)]

    rv = solve(rolls)
    if rv is None:
        print("none")
    else:
        print(rv)
    
