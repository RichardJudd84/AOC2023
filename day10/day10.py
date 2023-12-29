import math
import re
import time
import queue
with open("testdata.txt", "r" ) as data:
#with open("input.txt", "r" ) as data:
    res = data.readlines()

maze = []
startPos = None

def printMaze():
    for row in maze:
        print(row)

# find start position 
for i in range(len(res)):
    row = res[i].strip()
    
    if 'S' in row:
        startPos = (i,row.find('S'))
    maze.append(list(row)) 

directions = {'north': (-1,0), 'east': (0,1), 'south': (1,0), 'west': (0,-1)}

nPipes = {'|': 'north', '7': 'west', 'F': 'east'}
sPipes = {'|': 'south', 'L': 'east', 'J': 'west'}
ePipes = {'-': 'east', 'J': 'north', '7': 'south'}
wPipes = {'-': 'west', 'L': 'north', 'F': 'south'}

pipes = {'north': nPipes, 'east': ePipes, 'south': sPipes, 'west': wPipes}

startDirections = []

for direction, pipe in zip(directions, pipes.values()) :
    s1,s2 = startPos
    d1,d2 = directions[direction]
    next = (s1+d1, s2+d2)
    if( next[0] >= 0 and next[0] < len(maze) and  next[1] >= 0 and next[1] < len(maze[0])):
        nPos = maze[next[0]][next[1]]
        
        if  nPos in pipe:
            startDirections.append(direction)

currentDirections = startDirections
currentPositions = [startPos, startPos]

def getnext():
    nextPositions = [] 
    nextDirections = []
    for pos, dir in zip(currentPositions, currentDirections):
        p1 , p2 = pos
        d1, d2 = directions[dir]
        np1 = p1+d1
        np2 = p2 +d2
        nextPipe = maze[np1][np2]
        nextDirection = pipes[dir][nextPipe]
        nextPositions.append((np1,np2))
        nextDirections.append(nextDirection)
    return nextDirections, nextPositions

count = 0
while True:
    currentDirections, currentPositions = getnext()
    count +=1
    if currentPositions[0] == currentPositions[1]:
        break

print(count)

# part 2
answers = []
pipeLists = []

for currentDirection in startDirections:
    mazecopy = [row.copy() for row in maze]
    currentPosition = startPos
    pipeList = []

    # find all pipes in one direction and add to list with direction
    def getnext():
        p1 , p2 = currentPosition
        d1, d2 = directions[currentDirection]
        np1 = p1+d1
        np2 = p2 +d2
        nextPipe = mazecopy[np1][np2]
        nextPosition = (np1,np2)
        if nextPipe == 'S': 
            return startDirections[0], nextPosition 
        else:
            nextDirection = pipes[currentDirection][nextPipe]    
            return nextDirection, nextPosition

    pipeSections = dict()

    while True:
        pipeList.append(currentPosition)
        pipeSections[currentPosition] = currentDirection
        currentDirection, currentPosition = getnext()
        if currentPosition == startPos:
            break
    
    pipeLists.append(pipeList)
    for move in pipeSections:
        x, y = move
        mazecopy[x][y] = 'P'

    def findFirstNorthPipe():
        for x in range(len(mazecopy)):
            for y in range(len(mazecopy[x])):
                if mazecopy[x][y] == 'P':
                    return (x,y)

    northPipe = findFirstNorthPipe()
    direction = pipeSections[northPipe]  
    if direction == 'east': # look right  
        inside =  {'north': 'east' , 'east': 'south', 'south': 'west' , 'west': 'north'} 
    elif direction == 'south': # look left
        inside = {'north': 'west' , 'east': 'north', 'south': 'east' , 'west': 'south'}           

    found = set()

    for move in pipeSections:
        dir = pipeSections[move]
        insideDir = inside[dir]
        ox, oy = directions[insideDir]
        px, py = move
        x = px+ox
        y = py+oy
        insidePos = (x,y)
        insidePosVal = mazecopy[x][y]
        if insidePosVal not in ['P']:
            found.add(insidePos)
            mazecopy[x][y] = 'X'

    found2 = set()

    def search(start):
        outQue = queue.Queue()
        outQue.put(start)

        while outQue.qsize():
            pos = outQue.get()
            px, py = pos

            for direction in directions:
                dx, dy = directions[direction]
                next = (px + dx, py + dy)
                if( next[0] >= 0 and next[0] < len(mazecopy) and  next[1] >= 0 and next[1] < len(mazecopy[0])):
                    val = mazecopy[next[0]][next[1]]
                    if val not in ['P','X']:
                        mazecopy[next[0]][next[1]] = 'X'
                        found2.add(next)
                        outQue.put(next)

    for foundpos in found:
        search(foundpos)

    answers += list(found) + list(found2)

answers  = set(answers)
print(len(answers))

# shoelace solution

def shoelace(points: list()):
    area = 0
    xpoints = [point[0] for point in points] + [points[0][0]]
    ypoints = [point[1] for point in points] + [points[0][1]]

    for i in range(len(points)):
        area += (xpoints[i]*ypoints[i+1])
        area -= (ypoints[i]*xpoints[i+1])
    return abs(area / 2)

shoelaceArea = shoelace(pipeLists[0])
internalArea = shoelaceArea-((len(pipeLists[0])/2)-1)
print(internalArea)