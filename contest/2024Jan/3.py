import sys
sys.stdin = open('3.in')

# read input
N = int(input().strip())
a = [int(e) for e in input().strip().split()]

def remove(L, list, times):
    for i in range(0, L + 1):
        list[N-1-i] -= ((L-i)*times)

def add(L, list, times):
    for i in range(0, L + 1):
        list[N-1-i] += ((L-i)*times)
        
ans = 0
for i in range(0, N):
    times = abs(a[i])
    if a[i] != 0:
        L = N - i
        if a[i] > 0:
            remove(L, a, times)
        elif a[i] < 0:
            add(L, a, times)
        ans += times
    elif a[i] == 0:
        continue

print(str(ans))

        
