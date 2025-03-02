# import sys
# sys.stdin = open('2.in')

N = int(input().strip())
a = [int(e) for e in input().strip().split()]

times = [0] * (N + 1)
for n in a:
    times[n] += 1

for i in range(N + 1):
    ans = 0
    mex = i
    for j in range(mex):
        if times[j] == 0:
            ans += 1

    if mex in a:
        if ans < times[mex]:
            ans = times[mex]

    print(ans)
