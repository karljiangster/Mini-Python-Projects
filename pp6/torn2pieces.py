import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/torn2pieces
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.


def solve(pieces, start, end):
    # Your code here
    return None

if __name__ == "__main__":
    npieces = int(sys.stdin.readline())

    pieces = []
    for i in range(npieces):
        piece = sys.stdin.readline().strip().split()
        pieces.append(piece)

    start, end = sys.stdin.readline().strip().split()

    route = solve(pieces, start, end)
    if route is None:
        print("no route found")
    else:
        print(" ".join(route))

