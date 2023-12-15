import math
import re
import time
#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

answer = 0

for line in res:    
    line = re.findall("[-\d]+",line.strip())
    lines = [line]    

    def getNextRow(): 
        nextLine=[]       
        for i in range(0,len(line)-1):
            nextLine.append(int(line[i+1])-int(line[i]))
        return nextLine
    
    while True:
        nextLine = getNextRow()
        lines.append(nextLine)
        line = nextLine

        allZeros = True        
        for val in line:
            if val:
                allZeros = False
                break
        if allZeros:
            break        

    lines[-1].append(0)
    for l in range(len(lines)-1, 0 ,-1):
        lines[l-1].append(int(lines[l-1][-1]) + lines[l][-1])
    answer += lines[0][-1]

print(answer)


# part 2
answer = 0

for line in res:    
    line = re.findall("[-\d]+",line.strip())
    lines = [line]    

    def getNextRow():     
        nextLine=[]   
        for i in range(0,len(line)-1):
            nextLine.append(int(line[i+1])-int(line[i]))
        return nextLine    
    
    while True:
        nextLine = getNextRow()
        lines.append(nextLine)
        line = nextLine

        allZeros = True        
        for val in line:
            if val:
                allZeros = False
                break
        if allZeros:
            break
        

    lines[-1].insert(0,0)
    for l in range(len(lines)-1, 0 ,-1):
        lines[l-1].insert(0, int(lines[l-1][0]) +-lines[l][0])
    answer += lines[0][0]

print(answer)