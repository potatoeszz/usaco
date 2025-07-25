import sys
# sys.stdin = open('3.in')

# read input
N = int(input().strip())
a = [int(e) for e in input().strip().split()]

da = a.copy()
for x in range(1, N):
    da[x]= a[x] - a[x - 1]

dda = da.copy()
for x in range(1, N):
    dda[x]= da[x] - da[x - 1]

ans = 0
for e in dda:
    ans += abs(e)

ans = 0
sumOfApps = 0
# make a[i] be 0 one by one from left to right
for i in range(0, N): # x is the position of the patch
    if i == 0:
        a[i] = a[i]
    else:
        a[i] = a[i - 1] + da[i] + sumOfApps
    apps = -a[i]
    a[i] += apps
    ans += abs(apps)
    sumOfApps += apps

print(str(ans))

        
