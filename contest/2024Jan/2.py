import sys
#sys.stdin = open('2.in')

# read input
N, S = [int(e) for e in input().strip().split()]
S -= 1 # make start 0-based
V = 1
ans = 0
qv = [] # list of [q, v] -> [[q1, v1], [q2, v2]...]

for i in range(N):
    qv.append([int(e) for e in input().strip().split()])

lzjp = False # last jump pad is zero velocity

while True: # while S >= 0 and S < N
    if S < 0 or S >= N:
        break
    power = abs(V)
    dir = V // power
    
    cur_qv = qv[S]
    if cur_qv[0] == 1: # if current position is a normal target
        if cur_qv[1] <= power: # break it
            ans += 1
            cur_qv[0] = 2 # 2 means it's a broken target
    elif cur_qv[0] == 0: # if current position is a jump pad
        power += cur_qv[1]
        dir *= -1
        V = power * dir
        if cur_qv[1] == 0:
            if not lzjp:
                lzjp = True
            else:
                break
        else:
            lzjp = False
    else: # if current position is a broken target
         pass
    S += V
    
print(ans)