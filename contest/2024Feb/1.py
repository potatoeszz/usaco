import sys
# sys.stdin = open('1.in')

# read input
T = int(input().strip())

for _ in range(T):
    S = input().strip()
    iS = int(S)
    if iS % 10 == 0: # you can also use "if S[-1] == '0'"
        print("E")
    else:
        print("B")