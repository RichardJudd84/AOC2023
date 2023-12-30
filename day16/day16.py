from enum import Enum
import queue
#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

grid = [line.strip() for line in res]

####################################### part 1 #######################################

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Agent:
    position = None
    direction = None
    def __init__(self, y:int = 0, x:int = 0, direction: Direction = Direction.EAST) -> (int,int):
        self.position = (y,x)
        self.direction = direction
    
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
        return self.position
    
    def turnLeft(self):
        self.direction = Direction((self.direction.value-1)%4)
    
    def turnRight(self):
        self.direction = Direction((self.direction.value+1)%4)

    def copy(self, direction: Direction = None):
        if not direction:
            direction = self.direction 
        y,x = self.position
        return Agent(y=y, x=x, direction=direction )
    
    def setDirection(self, direction: Direction):
        self.direction = direction
    
    def setPosition(self, y: int, x: int):
        self.position = (y,x)


def findEnergisedTiles(y:int = 0, x:int= 0, direction: Direction =  Direction.EAST ):
    agents = queue.Queue()

    def addAgent(agent: Agent):
        y,x = agent.position
        if y >= 0 and x >=0 and y < len(grid) and x < len(grid[0]):
            agents.put(agent) 

    addAgent(Agent(y,x,direction))

    positions = set()
    explored = set()

    while not agents.empty():
        agent = agents.get()
        y,x = agent.position
        positions.add(agent.position)
        entity = grid[y][x]
        if (agent.position, agent.direction) in explored:
            continue
        else:
            explored.add((agent.position, agent.direction))

        if entity == '/':
            if agent.direction in [Direction.EAST, Direction.WEST]:
                agent.turnLeft()
            else:
                agent.turnRight()
            
        elif entity == '\\':
            if agent.direction in [Direction.EAST, Direction.WEST]:
                agent.turnRight()
            else:
                agent.turnLeft()

        elif entity == '|':
            if agent.direction in [Direction.EAST, Direction.WEST]:
                splitAgent = agent.copy()
                splitAgent.turnLeft()
                splitAgent.move()
                addAgent(splitAgent)            
                agent.turnRight()

        elif entity == '-':
            if agent.direction in [Direction.NORTH, Direction.SOUTH]:
                splitAgent = agent.copy()
                splitAgent.turnLeft()
                splitAgent.move()
                addAgent(splitAgent)            
                agent.turnRight()

        agent.move()
        addAgent(agent)
    return len(positions)


answer = findEnergisedTiles()
print(answer)


####################################### part 2 #######################################

mostEnegrised = 0

for y in range(len(grid)):
    x = 0 
    direction = Direction.EAST
    n = findEnergisedTiles(y,x, direction)
    if n > mostEnegrised: 
        mostEnegrised = n

    x = len(grid[0])-1
    direction = Direction.WEST
    n = findEnergisedTiles(y,x, direction)
    if n > mostEnegrised: 
        mostEnegrised = n

for x in range(len(grid[0])):
    y = 0
    direction = Direction.SOUTH
    n = findEnergisedTiles(y,x, direction)
    if n > mostEnegrised: 
        mostEnegrised = n
    
    y = len(grid)-1
    direction = Direction.NORTH
    n = findEnergisedTiles(y, x, direction)
    if n > mostEnegrised: 
        mostEnegrised = n

print(mostEnegrised)
