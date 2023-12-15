import queue
#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

matrix = []
for line in res:
    line = list(line.strip())
    matrix.append(line)

def printMatrix():
    for line in matrix:
        print(line)
#printMatrix()

def transposeMatrix(matrix):
    newMatrix = []
    for y in range(len(matrix[0])):
        col = []
        for x in range(len(matrix)):
            col.append(matrix[x][y])
        newMatrix.append(col)
    return newMatrix

def addRowsIfBlank(matrix):
    newMatrix = [] 
    for line in matrix:
        newMatrix.append(line)
        if '#' in line:
            continue
        else:
            newMatrix.append(line)
    return newMatrix

matrix = addRowsIfBlank(matrix)
matrix = transposeMatrix(matrix)
matrix = addRowsIfBlank(matrix)
matrix = transposeMatrix(matrix)
#printMatrix()

def getPoints(matrix):
    points = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == '#':
                points.append((x,y))
    return points

points= getPoints(matrix)

answer = 0
for iA in range(len(points)-1):
    pointA = points[iA]
    for iB in range(iA+1,len(points)):
        pointB = points[iB]
        distance = abs(pointB[0] - pointA[0]) + abs(pointB[1] - pointA[1])
        answer += distance

print(answer)


# part 2

matrix = []
expanseFactor = 1000000
for line in res:
    line = list(line.strip())
    matrix.append(line)

def getRowNumberIfBlank(matrix):
    rowNumbers = [] 
    for i in range(len(matrix)):
        if '#' in matrix[i]:
            continue
        else:
            rowNumbers.append(i)
    return rowNumbers

expandingRows = getRowNumberIfBlank(matrix)
matrix = transposeMatrix(matrix)
expandingCols = getRowNumberIfBlank(matrix)
matrix = transposeMatrix(matrix)

points = getPoints(matrix)

def addExpansetoPoint(point, increase):
    def increasepoint(p, expander):
        for i in range(len(expander)):
            if p < expander[i]:
                return p + (i*increase) - i
        return p + ((i+1)*increase) - (i+1) 
    point = (increasepoint(point[0], expandingRows), increasepoint(point[1], expandingCols))
    return point

points = [addExpansetoPoint(point, expanseFactor) for point in points]

answer = 0

for iA in range(len(points)-1):
    pointA = points[iA]
    for iB in range(iA+1,len(points)):
        pointB = points[iB]
        distance = abs(pointB[0] - pointA[0]) + abs(pointB[1] - pointA[1])
        answer += distance

print(answer)