from enum import Enum
import queue
#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

####################################### part 1 #######################################
grid = [line.strip() for line in res]
start = (0,0)
goal = (len(grid)-1, len(grid[0])-1)

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Agent:
    position = None
    direction = None
    path = []
    heatLoss = 0
    sameDirection = 0

    def __init__(self, y:int = 0, x:int = 0, direction: Direction = Direction.EAST, path = [], heatLoss = 0, sameDirection = 0) -> (int,int):
        self.position = (y,x)
        self.direction = direction
        self.path = path
        self.heatLoss = heatLoss
        self.sameDirection = sameDirection
    
    def move(self, distance = 1) -> (int, int):
        y,x = self.position
        
        if self.direction == Direction.NORTH: 
            self.position = (y-distance, x)
        if self.direction == Direction.SOUTH: 
            self.position = (y+distance, x)
        if self.direction == Direction.WEST: 
            self.position = (y, x-distance)
        if self.direction == Direction.EAST: 
            self.position = (y, x+distance)

        y,x = self.position
        if y >= 0 and x >=0 and y < len(grid) and x < len(grid[0]) and self.position not in self.path:
            if y <0 or x<0:
                print(y,x) 
                input()
            self.path.append(self.position)            
            self.heatLoss += int(grid[y][x])
            return True
        return False
    
    def moveLeft(self):
        self.direction = Direction((self.direction.value-1)%4)
        self.sameDirection = 1
        return self.move()

    def moveRight(self):
        self.direction = Direction((self.direction.value+1)%4)
        self.sameDirection = 1
        return self.move()

    def moveAhead(self):
        if self.sameDirection < 3:
            self.sameDirection +=1
            return self.move()

        return False
    
    def copy(self):
        y,x = self.position
        return Agent(y, x, self.direction, self.path.copy() , self.heatLoss, self.sameDirection)
    
    def __eq__(self, other:'Agent'):
        return self.heatLoss == other.heatLoss
    
    def __lt__(self, other:'Agent'):
        return self.heatLoss < other.heatLoss
    
    def __gt__(self, other:'Agent'):
        return self.heatLoss > other.heatLoss
    
    def __str__(self) -> str:
        return str(self.heatLoss)



lowestAgentQue = queue.PriorityQueue()
lowestHeatlossDict = dict()

def processAgent(agent:Agent):
    key = (agent.direction, agent.sameDirection)
    pos = agent.position
    heatLoss = agent

    if pos not in lowestHeatlossDict:
        lowestHeatlossDict[pos] = {key: heatLoss}
    elif key not in lowestHeatlossDict[pos]:
        lowestHeatlossDict[pos][key] = heatLoss
    elif heatLoss < lowestHeatlossDict[pos][key]:
        lowestHeatlossDict[pos][key] = heatLoss
    else:
        return False
    
    lowestAgentQue.put(agent)
    return True

startAgent = Agent()

processAgent(startAgent)

while not lowestAgentQue.empty():
    agent:Agent = lowestAgentQue.get()
    
    nextAgent = agent.copy()
    if nextAgent.moveLeft():
        processAgent(nextAgent)
    nextAgent = agent.copy()
    if nextAgent.moveRight():
        processAgent(nextAgent)
    nextAgent = agent.copy()
    if nextAgent.moveAhead():
        processAgent(nextAgent)


answer = min(lowestHeatlossDict[goal].values())
print(answer)