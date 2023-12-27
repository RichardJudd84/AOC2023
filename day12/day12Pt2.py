import queue
import re
#with open("testData.txt", "r" ) as data:
#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

############################################### helpers ###############################################
def findAllPositions(sqVals, sqI, ln:str, i):
    hashPos = None
    validPositions = []
    sqVal = sqVals[sqI]
    minLnRemaining = sum(sqVals[sqI+1:]) + len(sqVals[sqI+1:])
    sumRemainingSq = sum(sqVals[sqI+1:])

    
    while minLnRemaining < len(ln[i+sqVal:]):        
        subLn = ln[i:i+sqVal]
        next = ln[i+sqVal]
        previous = ln[i-1]
        
        if not hashPos and '#' in subLn:
            hashPos = i+subLn.find('#')

        elif hashPos and i > hashPos:
            return validPositions
        
        if '.' not in subLn and next != '#' and previous != '#':
            remainingLn = ln[i+sqVal:]
            hashesRemaining = len(re.findall('#', remainingLn))
            if hashesRemaining <=  sumRemainingSq:
                validPositions.append((i, i+sqVal))
        i += 1
    return validPositions

def addListToDict(primaryDict: dict(), listToAdd: list(), multiple=1):
    for key in listToAdd:
        if key in primaryDict:
            primaryDict[key] += multiple
        else:
            primaryDict[key] = multiple


############################################### execution ###############################################
            
nCopies = 4
answer = 0

for row in res:
    row = row.strip().split()
    sequence = [int(e) for e in row[1].split(',')]
    line = row[0]
    sequenceCopy = sequence.copy()

    # fold out map with n folds
    for rep in range(nCopies):
        line += '?' + row[0]
        sequence += sequenceCopy

    # clean up line by replacing multiple '...' with '.'
    ln = '.' + line +'.'
    ln = re.sub('[.]+', '.', ln)

    # for each sequence val find all valid possisions and add to dictionary of next possible positions with their multiples
    currentPositions = dict()
    initialPositions = findAllPositions(sequence, 0, ln,1)
    addListToDict(currentPositions, initialPositions, 1)

    for i in range(1,len(sequence)):
        nextPositions = dict()
        for pos in currentPositions: 
            addListToDict(nextPositions,findAllPositions(sequence, i, ln, pos[1]+1),currentPositions[pos])
        currentPositions = nextPositions
    
    answer += sum(currentPositions.values())
print(answer)
