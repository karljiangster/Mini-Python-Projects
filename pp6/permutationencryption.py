import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/permutationencryption
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.


def encrypt(message, permutations):
    # Your code here
    return ""

if __name__ == "__main__":
    tokens = sys.stdin.readline().split()

    while int(tokens[0]) != 0:
        n = int(tokens[0])
        permutations = [int(x) for x in tokens[1:]]
        assert(len(permutations) == n)

        message = sys.stdin.readline().strip()
    
        print("'{}'".format(encrypt(message, permutations)))
        
        tokens = sys.stdin.readline().split()
    
