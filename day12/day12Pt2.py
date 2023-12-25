import queue
import re
with open("sampleData.txt", "r" ) as data:
#with open("input.txt", "r" ) as data:
    res = data.readlines()

answer = 0    
repp = 0
for row in res:
    repp+=1
    row = row.strip().split()
    sequence = [int(e) for e in row[1].split(',')]
    line = row[0]
    tsequence = sequence.copy()
    for rep in range(2):
        line += '?' + row[0]
        sequence += tsequence

    print(line, sequence)
    # remove leading and trailing '.' from line

    line = line.strip('.')
    print(line)

    # get list all parts
    parts = re.findall('[^.]+', line)
    print('List of all parts: ', parts)

    print(parts)
    print(sequence)

    
    

    # find possible sequence numbers per part from left to right
    numsLToR = []
    seqI = 0
    for part in parts:
        partNums = []
        sumSeqNR = sequence[seqI]
        size = len(part)
        while sumSeqNR <= size:
            #print('ltr' , seqI)
            partNums.append(seqI)            
            if seqI+1 >= len(sequence):
                break
            seqI += 1
            sumSeqNR += 1 + sequence[seqI]
        numsLToR.append(partNums)        
    

    #find possible sequence numbers per part from right to left
    parts.reverse() 
    numsRToL = []
    for part in parts:
        partNums = []
        sumSeqNR = sequence[seqI]
        
        size = len(part)
        while sumSeqNR <= size:
            #print('rtl', seqI)
            partNums.append(seqI)
            if seqI <= 0:
                break
            seqI -= 1
            sumSeqNR += 1 + sequence[seqI]
        partNums.reverse()    
        numsRToL.append(partNums)
    numsRToL.reverse()
    parts.reverse()


    for l, r , p in zip(numsLToR, numsRToL, parts):
        print(l,r, p)


    input()

    
      
