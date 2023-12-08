import math
import re
#with open("sampleData.txt", "r" ) as data:

with open("input.txt", "r" ) as data:
    res = data.readlines()

directions = res[0]

qTable = {}
for row in res[2:]:
    row = re.findall('[A-Z]+',row)
    qTable[row[0]] = (row[1], row[2])

pos = "AAA"
i = 0
length = len(directions)-1

while not pos == "ZZZ":   
    direction = directions[i%length]

    if direction == 'L':
        pos = qTable[pos][0]
    elif direction == 'R':
        pos = qTable[pos][1]
    else:
        print("Error, missed something!")  

    i += 1

print(i)


# part 2

#with open("sampleData2.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

directions = res[0]

qTable = {}
for row in res[2:]:
    row = re.findall('[A-Z\d]+',row)
    qTable[row[0]] = (row[1], row[2])

nodes = []
for key in qTable:
    if key[2] == 'A':
        nodes.append(key)

intervals = []
for node in nodes:
    i = 0
    length = len(directions)-1
    while not node[2] == "Z":   
        direction = directions[i%length]
        if direction == 'L':
            node = qTable[node][0]
        elif direction == 'R':
            node = qTable[node][1]
        else:
            print("Error, missed something!") 
        i += 1
    intervals.append(i)

print(math.lcm(*intervals))






