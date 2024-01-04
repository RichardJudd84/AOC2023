from enum import Enum
import queue
#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

####################################### part 1 #######################################

point = (0,0)
outlineOfPit = []

for line in res:    
    splitLine = line.strip().split()
    direction = splitLine[0]
    distance = int(splitLine[1])
    colour = splitLine[2]

    for rep in range(distance):
        outlineOfPit.append(point)
        y,x = point
        if direction == 'U':
            point = (y-1, x)
        if direction == 'D':
            point = (y+1, x)
        if direction == 'L':
            point = (y, x-1)
        if direction == 'R':
            point = (y, x+1)


def shoelace(points: list()):
    area = 0
    xpoints = [point[0] for point in points] + [points[0][0]]
    ypoints = [point[1] for point in points] + [points[0][1]]

    for i in range(len(points)):
        area += (xpoints[i]*ypoints[i+1])
        area -= (ypoints[i]*xpoints[i+1])
    return abs(area / 2)

shoelaceArea = shoelace(outlineOfPit+[(0,0)])
area = shoelaceArea+((len(outlineOfPit)/2)+1)
print(area)

####################################### part 2 #######################################

point = (0,0)
outlineOfPit = []

for line in res:    
    splitLine = line.strip().split()
    colour = splitLine[2]
    direction = colour[7]
    distance = int(colour[2:7],16)

    for rep in range(distance):
        outlineOfPit.append(point)
        y,x = point
        if direction == '3':
            point = (y-1, x)
        if direction == '1':
            point = (y+1, x)
        if direction == '2':
            point = (y, x-1)
        if direction == '0':
            point = (y, x+1)

shoelaceArea = shoelace(outlineOfPit+[(0,0)])
area = shoelaceArea+((len(outlineOfPit)/2)+1)
print(area)