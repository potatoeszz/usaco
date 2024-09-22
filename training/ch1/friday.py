"""
ID: boopioz1
LANG: PYTHON3
TASK: friday
"""

def isLeapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysInWeek = [0] * 7 #[su, mo, tu, we, th, fr, sa] to remember how many days fall into the day of the week
daysPassed = 0

# read input
with open("friday.in", "r") as fIn:
    N = int(fIn.readline().strip())

# main logic here!
for y in range(1900, 1900 + N):
    leap = isLeapYear(y)
    for m in range(12):
        daysPassedOn13Th = daysPassed + 13
        wd = daysPassedOn13Th % 7
        daysInWeek[wd] += 1

        daysPassed += daysInMonth[m]
        if leap and m == 1:
            daysPassed += 1

daysInWeek = daysInWeek[-1:] + daysInWeek[:-1]

print(' '.join([str(d) for d in daysInWeek]))
with open("friday.out", "w") as fOut:
    fOut.write(' '.join([str(d) for d in daysInWeek]))
    fOut.write("\n")

"""
print(daysInWeek[6], end=' ')
for i in range (0, 6):
    print(daysInWeek[i], end=' ')
    """