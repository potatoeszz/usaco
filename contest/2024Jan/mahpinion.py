#import sys
#sys.stdin = open("mahpinion.in")

def solve(N, cows):
    majority = set()
    if N == 2:
        if cows[0] == cows[1]:
            return [cows[0]]
        else:
            return [-1]
    for i in range(N - 2):
        if cows[i] == cows[i + 1]:
            majority.add(cows[i])
        elif cows[i] == cows[i + 2]:
            majority.add(cows[i])
        elif cows[i + 1] == cows[i + 2]:
            majority.add(cows[i + 1])

    if len(majority) == 0:
        return [-1]
    
    return sorted(list(majority))

# read input
t = int(input().strip())

for i in range(t):
    n = int(input().strip())
    cows = [int(i) for i in input().strip().split()]
    sol = (solve(n, cows))
    print(' '.join([str(e) for e in sol]))