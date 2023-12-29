import queue
import re
#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

answer = 0    

for line in res:
    line = line.strip().split()
    sequence = line[1]
    line = list(line[0])
    unknowns = []
    for i in range(len(line)):
        if line[i]=='?':
            unknowns.append(i)

    nrUnknowns = len(unknowns)
    nrCombos = 2**nrUnknowns
    ncombos = 0 
    for combo in range(nrCombos):
        tempLine = line.copy()
        combo = [int(e) for e in bin(combo)[2:].zfill(nrUnknowns)]
        for e , i in zip(combo, unknowns):
            if e:
                tempLine[i] = '#'
            else:
                tempLine[i]= '.'
        tempLine = "".join(tempLine)
        groups = re.findall('#+', tempLine)
        resSequence = ""
        for group in groups:
            resSequence += str(len(group)) + ',' 
               
        if resSequence[:-1] == sequence:
            answer += 1
            ncombos+= 1
    print(ncombos)

print(answer)
