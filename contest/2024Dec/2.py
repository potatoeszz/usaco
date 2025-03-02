#import sys
#sys.stdin = open("2.in")

# read the input
N, Q = [int(e) for e in input().strip().split()]

xRow = {}
yRow = {}
zRow = {}

ans = 0
for _ in range(Q):
    x, y, z = [int(e) for e in input().strip().split()]
    # handle x row
    key = (y, z) # Tuple
    if key in xRow:
        xRow[key] += 1
    else:
        xRow[key] = 1
    if xRow[key] == N:
        ans += 1

    # handle y row
    key = (x, z)
    if key in yRow:
        yRow[key] += 1
    else:
        yRow[key] = 1
    if yRow[key] == N:
        ans += 1

    # hand z row
    key = (x, y)
    if key in zRow:
        zRow[key] += 1
    else:
        zRow[key] = 1
    if zRow[key] == N:
        ans += 1

    print(ans)