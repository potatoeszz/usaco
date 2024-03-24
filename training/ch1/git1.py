"""
ID: boopioz1
LANG: PYTHON3
TASK: gift1
"""
def returngive(money, peopleNum):
    return money % peopleNum

def getGivingPerPeople(money, peopleNum):
    return money // peopleNum


with open("gift1.in", "r") as fIn:
    lines = fIn.read().splitlines()

    np = int(lines[0])
    
    people = {}

for i in range(1, np + 1):
    name = lines[i]
    people[name]= 0

curLine = np + 1
while curLine < len(lines):
    giver = lines[curLine]
    curLine += 1
    money, peopleNum = map(int, lines[curLine].split())
    if peopleNum == 0:
        curLine += 1
        continue
    people[giver] -= money
    people[giver] += returngive(money, peopleNum)
    curLine += 1
    for i in range(peopleNum):
        receiver = lines[curLine]
        people[receiver] += getGivingPerPeople(money, peopleNum)
        curLine += 1

print(people)