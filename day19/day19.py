from enum import Enum
import re
with open("sampleData.txt", "r" ) as data:
#with open("input.txt", "r" ) as data:
    res = data.readlines()

####################################### part 1 #######################################
    
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
            value = xmasDict[self.xmas]
            if self.operator == '<':
                if value < self.value:
                    return self.action
            elif self.operator == '>':
                if value > self.value:
                    return self.action
        else:
            return self.action
        
        return False
            
workflows = True
workFlowDict = {}
answer = 0

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

    else:
        xmasdict = {}
        acceptedVal = 0
        for e in line[1:-1].split(','):
            e = e.split('=')
            key = e[0]
            value = int(e[1])
            xmasdict[key] = value
            acceptedVal += value

        currentWFKey = 'in'
        while currentWFKey:
            rules:[Rule] = workFlowDict[currentWFKey]
            for rule in rules:
                action = rule.rule(xmasdict)
                if not action:
                    continue
                elif action == 'A':
                    answer += acceptedVal
                    currentWFKey = False
                    break
                elif action == 'R':
                    currentWFKey = False
                    break
                else:
                    currentWFKey = action
                    break
             

print(answer)


xmasDict = {'x': 1, 'm': 1, 'a': 1, 's': 1 } 

currentWFKey = 'in'
