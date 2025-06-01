import sys
sys.stdin = open("3.in")

N = int(input().strip())
a = [int(e) for e in input().strip().split()]
b = [int(e) for e in input().strip().split()]

count = 0 # without any operations, how many cows will be checked
for i in range(N):
    if a[i] == b[i]:
        count += 1


ans = [0] * (N + 1)
# ans[count] >= N

# return 
def reverse(l, r):
    aa = a.copy()
    for i in range(l, r + 1):
        if i == l:
            aa[i] = a[r]
        aa[i] = a[r - i + l]
    return aa

def check(a):
    count = 0
    for i in range(N):
        if a[i] == b[i]:
            count += 1
    return count

def betterCheck(aaa, l, r):
    # find within the range how much difference from the origianl
    ori = 0
    for i in range(l, r + 1):
        if a[i] == b[i]:
            ori += 1

    new = 0
    for i in range(l, r + 1):
        if aaa[i] == b[i]:
            new += 1

    return count + new - ori

for l in range(N): # brute force l
    for r in range(l, N): # brute force r
        aa = reverse(l, r)
        c = betterCheck(aa, l, r)
        ans[c] += 1

for a in ans:
    print(a)
