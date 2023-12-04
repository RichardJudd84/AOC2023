#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

answer = 0
for line in res:
    score = 0
    matches = False
    line= line.strip()
    line = line.split(':')[1]
    line = line. split('|')
    wNums = line[0].split()
    lNums = line[1].split()

    for num in wNums:
        if num in lNums:
            if not matches:
                matches = True
                score = 1
                
            else:
                score *= 2

    answer += score 

print(answer)


# part 2

answer = 0 
cards = []

for line in res:
    line= line.strip()
    line = line.split(':')[1]
    line = line. split('|')
    wNums = line[0].split()
    lNums = line[1].split()
    cards.append((wNums,lNums))

for i in range(len(cards)):

    def playCards(cardnum):
        wNums, lNums = cards[cardnum]
        matches = 1
        newCards = 0
        for num in wNums:
            if num in lNums:    
                newCards+=1         
                matches += playCards(cardnum + newCards)
        return matches    
    
    answer += playCards(i)

print(answer)