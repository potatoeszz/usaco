import sys
sys.stdin = open("1.in")

from collections import defaultdict

N, M = [int(e) for e in input().strip().split()]

# put info into a list (might be redundant since it's a loop)
key = []
for _ in range(N):
    key.append(list(input().strip()))

# matches = []
# for e in range(M):
#     matches.append(list(input().strip().split()))

loseSymbols = defaultdict(set)

# find losing symbols for each symbol - filling loseSymbols dict
for r in range(N):
    for c in range(r + 1):
        if key[r][c] == "L":
            loseSymbols[r + 1].add(c + 1)
        elif key[r][c] == 'W':
            loseSymbols[c + 1].add(r+1)


# solve single match - print the output as well
# Input: one match from E: list of 2 elements: 1 for each play
def solveSingle(match):
    global key, N
    e1 = int(match[0])
    e2 = int(match[1])
    
    S1 = loseSymbols[e1]
    S2 = loseSymbols[e2]

    ws = S1.intersection(S2)
    w = len(ws)
    return (w * N * 2 - w * w)

for m in range(M):
    p1, p2 = [int(e) for e in input().strip().split()]
    print(solveSingle((p1, p2)))