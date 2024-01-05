from enum import Enum
import re
import queue
#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

####################################### part 2 #######################################
    
class Rule:
    xmas = None
    operator = None
    value = None
    action = None

    def __init__(self, ruleString: str):
        splitString = re.findall('[\w]+|[<>]|[\d]+', ruleString)
        if len(splitString) == 1:
            self.action = splitString[0]
        else:
            self.xmas = splitString[0]
            self.operator = splitString[1]
            self.value = int(splitString[2])
            self.action = splitString[3]

    def rule(self, xmasDict:dict()):
        if self.xmas:
            xmin, xmax = xmasDict[self.xmas]
            xmasDictFail = xmasDict.copy()
            xmasDictPass = xmasDict.copy()
            if self.operator == '<':
                if xmax < self.value:
                    xmasDictPass[self.xmas] = (xmin,xmax)
                    xmasDictFail = None
                elif xmin < self.value and xmax >= self.value:
                    xmasDictPass[self.xmas] = (xmin,self.value-1)
                    xmasDictFail[self.xmas] = (self.value,xmax)
                elif xmin >= self.value:
                    xmasDictPass= None 
                    xmasDictFail[self.xmas] = (xmin,xmax)
                else:
                    print('Missed something')
            elif self.operator == '>':
                if xmin > self.value:
                    xmasDictPass[self.xmas] = (xmin,xmax)
                    xmasDictFail = None
                elif xmax > self.value and xmin <= self.value:
                    xmasDictPass[self.xmas] = (self.value+1,xmax)
                    xmasDictFail[self.xmas] = (xmin,self.value)
                elif xmax <= self.value:
                    xmasDictPass = None 
                    xmasDictFail[self.xmas] = (xmin,xmax)
                else:
                    print('Missed something')
            return self.action, xmasDictPass, xmasDictFail 
        else:
            return self.action, xmasDict, None
        
            
workflows = True
workFlowDict = {}
accepted = []

for line in res:
    line = line.strip()
    if line == "":
        workflows = False
        continue

    if workflows:
        splitLine = line.split('{')
        workflowKey = splitLine[0]
        workFlowDict[workflowKey] = []

        workflowItems = splitLine[1].split(',')
        for item in workflowItems:
            workFlowDict[workflowKey].append(Rule(item))



xmasDict = {'x': (1,4000), 'm': (1,4000), 'a': (1,4000), 's': (1,4000)}
currentWFKey = 'in'
passQue = queue.Queue()

def addToQue(xmasDict:dict(), currentWFKey: str):
    passQue.put((xmasDict, currentWFKey))

addToQue(xmasDict, currentWFKey)

while not passQue.empty():
    xmasDict, currentWFKey = passQue.get()
    rules:[Rule] = workFlowDict[currentWFKey]
    for rule in rules:
        action, passDict, failDict = rule.rule(xmasDict)
        if not passDict:
            xmasDict = failDict
            continue
        elif action == 'A' and passDict:
            accepted.append((passDict, currentWFKey))
            xmasDict = failDict
        elif action == 'R' and passDict:
            xmasDict = failDict
        else:
            addToQue(passDict, action)
            xmasDict = failDict
 
             
answer = 0 

for xmasDict in accepted:
    nrAcceptedValsList = [(mx+1)-mn for mn,mx, in xmasDict[0].values()]
    nrCombos = 1
    for nrAcceptedVals in nrAcceptedValsList:
        nrCombos *= nrAcceptedVals
    answer += nrCombos

print(answer)
