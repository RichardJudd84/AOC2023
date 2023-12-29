import queue
import re
#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

patterns = []
currentPattern = []
for line in res:
    line = line.strip()
    if line == "":
        patterns.append(currentPattern)
        currentPattern=[]
    else:
        currentPattern.append(line)
patterns.append(currentPattern)

####################################### part 1 #######################################

def validateMirror(pattern: list[str], breakPoints:(str,str)):
    top = pattern[:breakPoints[1]]
    top.reverse()
    bottom = pattern[breakPoints[1]:]
    length = min([len(top), len(bottom)])

    for i in range(length):
        if top[i] != bottom[i]:
            return False
        
    return True


def findHorizontalMirror(pattern: list[str]):
    previousRow = pattern[0]

    for i in range(1, len(pattern)):
        currentRow = pattern[i]
        if currentRow == previousRow:
            breakPoints = (i-1, i)
            if validateMirror(pattern, breakPoints):
                return breakPoints
        previousRow = currentRow

    return None


def findVerticalMirror(pattern: list[str]):
    transposedPattern = transposePattern(pattern)
    return findHorizontalMirror(transposedPattern)


def transposePattern(pattern: list[str]):
    transposedPattern = []

    for col in range(len(pattern[0])):
        newRow = ""
        for row in range(len(pattern)):
            newRow += pattern[row][col]
        transposedPattern.append(newRow)

    return transposedPattern


def findResult(pattern: list[str]):
    res = findHorizontalMirror(pattern)

    if res:
        return res[1]*100
    else:
        res = findVerticalMirror(pattern)
        return res[1]
    
         
answer = 0
for pattern in patterns:
    res = findResult(pattern)
    answer += res

print(answer)


####################################### part 2 #######################################

def CheckForSmudge(pattern: list[str], rowI: int):
    top = pattern[:rowI]
    top.reverse()
    bottom = pattern[rowI:]
    length = min([len(top), len(bottom)])
    nDifferences = 0

    for i in range(length):
        if nDifferences > 1:
            return False 
        if top[i] != bottom[i]:
            for rI in range(len(top[i])):                
                if top[i][rI] != bottom[i][rI]:
                    nDifferences += 1

    if nDifferences == 1:
        return True
    
    return False


def findHorizontalSmudge(pattern: list[str]):
    for row in range(len(pattern)):
        if CheckForSmudge(pattern, row):
            return row
        
    return False


def findVerticalSmudge(pattern: list[str]):
    transposedPattern = transposePattern(pattern)
    res = findHorizontalSmudge(transposedPattern)

    return res


def findResult2(pattern: list[str]):
    res = findHorizontalSmudge(pattern)

    if res:
        return (res)*100
    else:
        res = findVerticalSmudge(pattern)
        return res
    

answer = 0
for pattern in patterns:
    res = findResult2(pattern)
    answer += res

print(answer)