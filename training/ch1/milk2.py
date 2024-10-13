"""
ID: boopioz1
LANG: PYTHON3
TASK: milk2
"""

milkingTimes = []

# read input
with open("milk2.in", "r") as fIn:
    N = int(fIn.readline().strip())
    for _ in range(N):
        line = fIn.readline().strip() # "300" "1000" -> ["300", "1000"]
        timeRange = [int(word) for word in line.split()] #["300", "1000"] -> [300, 1000]
        milkingTimes.append(timeRange)


# sort by start
milkingTimes.sort()

# merge time range
combinedTimes = []

maxGap = 0

curS, curE = milkingTimes[0]

for i in range(1, N):
    s, e = milkingTimes[i]
    if s <= curE: #overlapping
        curE = max(curE, e)
    else: # not overlapping
        combinedTimes.append([curS, curE]) # finalize a merging range
        gap = s - curE
        maxGap = max(maxGap, gap)
        #start a new merging range
        curS = s
        curE = e

combinedTimes.append([curS, curE])

maxMilkingTime = 0
for s, e in combinedTimes:
    maxMilkingTime = max(maxMilkingTime, e - s)

#write output
with open("milk2.out", "w") as fOut:
    fOut.write(f"{maxMilkingTime} {maxGap}\n")