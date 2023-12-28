from enum import Enum
import re
#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

platform = [line.strip() for line in res]

####################################### part 1 #######################################

def printPlatform(platform):
    for line in platform:
        print(line)

def transposePlatform(platform: list[str]):
    transposedPlatform = []

    for col in range(len(platform[0])):
        newRow = ""
        for row in range(len(platform)):
            newRow += platform[row][col]
        transposedPlatform.append(newRow)

    return transposedPlatform

def tipNorth(platform): 
    transposedPlatform = transposePlatform(platform)
    tippedNorthPlatform = []

    for line in transposedPlatform:
        newLine = ""
        sections = re.findall('[O.]+|[#]+', line)
        for section in sections:
            start = ""
            end = ""
            if '#' in section:
                newLine += section
                continue
            for ch in section:
                if ch == 'O':
                    start += ch
                elif ch == '.':
                    end += ch
            newLine += start + end
        tippedNorthPlatform.append(newLine)

    return transposePlatform(tippedNorthPlatform)

def calculateAnswer(tippedPlatform: list[str]):
    answer = 0
    nrRows = len(tippedPlatform)

    for row in tippedPlatform:
        nrOs = row.count('O')
        answer += nrOs * nrRows
        nrRows -= 1

    print(answer)

tippedNorthPlatform = tipNorth(platform)
calculateAnswer(tippedNorthPlatform)


####################################### part 2 #######################################

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

def tipPlatform(platform: list[str], direction: Direction):
    trpose = False
    tippedPlatform = []

    if direction in [Direction.NORTH, Direction.SOUTH]:
        trpose = True 

    if trpose: 
        platform = transposePlatform(platform)

    
    for line in platform:
        newLine = ""
        sections = re.findall('[O.]+|[#]+', line)
        for section in sections:
            start = ""
            end = ""
            if '#' in section:
                newLine += section
                continue
            for ch in section:
                if ch == 'O':
                    if direction in [Direction.NORTH, Direction.WEST]:
                        start += ch
                    else:
                        end += ch
                elif ch == '.':
                    if direction in [Direction.NORTH, Direction.WEST]:
                        end += ch
                    else:
                        start += ch
            newLine += start + end
        tippedPlatform.append(newLine)

    if trpose: 
        tippedPlatform = transposePlatform(tippedPlatform)

    return tippedPlatform

def cyclePlatform(platform, spins = 1):
    for x in range(spins):
        for dir in [Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST]:
            platform = tipPlatform(platform, dir)

    return platform

# find recuring loop in pattern sequence and use modulus to find answer
previousCycles=[]
currentCycle = cyclePlatform(platform)
spins = 1

while currentCycle not in previousCycles and spins < 1000000000 :
    previousCycles.append(currentCycle)
    currentCycle = cyclePlatform(currentCycle)
    spins += 1

for i in range(len(previousCycles)):
    if previousCycles[i] == currentCycle:
        startOfLoop = i

loop = previousCycles[startOfLoop:]
lengthOfLoop=len(loop)
iPos = (1000000000-1 - len(previousCycles)) % len(loop)

calculateAnswer(loop[iPos])