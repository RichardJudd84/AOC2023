import re

#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()


cols = len(res[0].strip())
rows = len(res)

lastLine = '.'*cols
res.append(lastLine)
matrix = ['.' + line.strip() + '.'  for line in res]

answer = 0

for i in range(rows):
    previousRow = matrix[i-1]
    currentRow = matrix[i]
    nextRow = matrix[i+1]

    numbers = re.findall( '\d+',currentRow)    
    if not len(numbers):
        continue

    for number in numbers:
        # get positon of number
        nStart = currentRow.find(number)-1 
        # problem: find always finds first instance
        # solution first instance replace with ... 
        nEnd = nStart + len(number)+2

        # check for validity
        sample = previousRow[nStart:nEnd] + currentRow[nStart:nEnd] + nextRow[nStart:nEnd]
        result = re.search( '[^.\d]',sample)
    
        if result:            
            answer += int(number)

        currentRow = currentRow.replace(number, '.'*len(number),1)

print(answer)
     
# part 2
answer = 0

# 1 find all gears 
def getNum(pos, row):
    left = pos
    right = pos
    leftEnd = False
    rightEnd = False
    while not leftEnd:
        if row[left-1].isnumeric():
            left -= 1
        else:
            leftEnd = True
    while not rightEnd:
        if row[right+1].isnumeric():
            right += 1
        else:
            rightEnd = True
    num = int(row[left:right+1])
    return num,left,right

for i in range(rows):
    previousRow = matrix[i-1]
    currentRow = matrix[i]
    nextRow = matrix[i+1]

    gears = re.findall('\*',currentRow)

    if (gears):
        print(gears)

        for gear in gears:
            gearpos = currentRow.find(gear)
            numbers = []
            for row in [previousRow,currentRow,nextRow]:
                pos = gearpos-1
                while pos < gearpos+2:
                    if row[pos].isnumeric():
                        num, left, right = getNum(pos,row)
                        numbers.append(num)
                        pos = right
                    pos += 1
            if len(numbers) == 2:
                answer += numbers[0] * numbers[1]

            currentRow = currentRow.replace(gear, '.', 1)

print(answer)