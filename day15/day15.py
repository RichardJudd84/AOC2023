from enum import Enum
import re
import csv
#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = list(csv.reader(data))[0]

####################################### part 1 #######################################
    
def getValue(currentVal: int, currentChar: str):
    currentVal += ord(currentChar)
    currentVal *= 17
    currentVal %= 256
    return currentVal

def gethash(code):
    currentVal = 0
    for ch in code:
        currentVal = getValue(currentVal, ch)
    return currentVal

answer = 0
for code in res:    
    answer += gethash(code)
    
print(answer)


####################################### part 2 #######################################

boxes = {key:[] for key in range(256)}
lensValues = {}

for val in res:
    seq = re.findall('[a-z]+|[=-]|\d', val)
    lensCode = seq[0]
    operator = seq[1]
    boxNumber = gethash(lensCode)
    box = boxes[boxNumber]
    if operator == '=':
        lens = int(seq[2])
        focusingPower = lens    
        lensValues[lensCode] = focusingPower
        if lensCode not in box:
            box.append(lensCode)
    elif operator == '-':
        lensValues[lensCode] = None
        if lensCode in box: box.remove(lensCode)         

answer = 0

for boxKey in boxes:
    contents = boxes[boxKey]
    boxNr = boxKey+1
    for i in range(len(contents)):
        slotNr = i+1
        lensKey = contents[i]
        focalLength = lensValues[lensKey]
        focusingPower = boxNr * slotNr * focalLength
        answer += focusingPower

print(answer)