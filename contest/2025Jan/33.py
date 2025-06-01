import sys
#sys.stdin = open("3.in")

N = int(input().strip())
a = [int(e) for e in input().strip().split()]
b = [int(e) for e in input().strip().split()]

count = 0 # without any operations, how many cows will be checked
for i in range(N):
    if a[i] == b[i]:
        count += 1


ans = [0] * (N + 1)
# ans[count] >= N

for c in range(N): # brute force the center
    # if there is one center
    newCount = count
    for i in range(N): # every i is one range
        #[c - i, c + i]
        if c - i < 0 or c + i >= N:
            break
        if a[c - i] == b[c - i]:
            newCount -= 1
        if a[c + i] == b[c + i]:
            newCount -= 1
        if a[c - i] == b[c + i]:
            newCount += 1
        if a[c + i] == b[c - i]:
            newCount += 1
        ans[newCount] += 1


    # if there's no center ( center with 2 points ) where c is the left one
    newCount = count
    for i in range(N):
        if c - i < 0 or c + i + 1 >= N:
            break
        if a[c - i] == b[c - i]:
            newCount -= 1
        if a[c + 1 + i] == b[c + 1 + i]:
            newCount -= 1
        if a[c - i] == b[c + 1 + i]:
            newCount += 1
        if a[c + 1 + i] == b[c - i]:
            newCount += 1
        ans[newCount] += 1


for a in ans:
    print(a)
