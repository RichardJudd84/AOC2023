import re
import queue
#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

pictureToValue = {'T': 10, 'J':11, 'Q': 12, 'K': 13, 'A':14}
rankedCards = queue.PriorityQueue()

for line in res:
    line = line.strip().split()
    hand = line[0] 
    bid = line[1]
    rank = None

    def parseCard(card):
        if card in pictureToValue:
            return pictureToValue[card]
        else:
            return int(card)

    handValues = [parseCard(card) for card in hand]
    sortedHandValues = sorted(handValues)

    # get rank based on hand 
    cardDict = {}
    
    for card in sortedHandValues:
        if card in cardDict:
            cardDict[card] += 1 
        else:
            cardDict[card] = 1 
    
    if len(cardDict) == 1: rank = (tuple([6] + handValues), bid, hand, "Five of a kind")
    elif len(cardDict) == 2:
        if 4 in cardDict.values(): rank = (tuple([5] + handValues), bid, hand, "Four of a kind" )
        elif 3 in cardDict.values(): rank = (tuple([4] + handValues), bid, hand, "Full house")
        else: print("Error, missed something (length 2)")
    elif len(cardDict) == 3:
        if 3 in cardDict.values(): rank = (tuple([3] + handValues), bid, hand, "Three of a kind")
        elif 2 in cardDict.values(): rank = (tuple([2] + handValues), bid, hand, "Two pair")
        else: print("Error, missed something (length 3)")
    elif len(cardDict) == 4: rank = (tuple([1] + handValues), bid, hand, "One pair")
    elif len(cardDict) == 5: rank = (tuple([0] + handValues), bid, hand, "High card")
    else: print("Error, missed something")

    rankedCards.put(rank)

answer = 0
rank = 0
while rankedCards.qsize():
    rank += 1
    card = rankedCards.get()
    answer += int(card[1]) * rank

print(answer)


# part 2

pictureToValue = { 'J':1,'T': 10, 'Q': 11, 'K': 12, 'A':13}
rankedCards = queue.PriorityQueue()

for line in res:
    line = line.strip().split()
    hand = line[0] 
    bid = line[1]
    rank = None

    def parseCard(card):
        if card in pictureToValue:
            return pictureToValue[card]
        else:
            return int(card)

    handValues = [parseCard(card) for card in hand]
    sortedHandValues = sorted(handValues)

    # get rank based on hand 

    cardDict = {}
    
    for card in sortedHandValues:
        if card in cardDict:
            cardDict[card] += 1 
        else:
            cardDict[card] = 1 
    
    if 1 in cardDict and len(cardDict) > 1:
        nrJokers = cardDict.pop(1)
        keyMax = max(cardDict, key = cardDict.get)
        cardDict[keyMax] += nrJokers

    if len(cardDict) == 1: rank = (tuple([6] + handValues), bid, hand, "Five of a kind")
    elif len(cardDict) == 2:
        if 4 in cardDict.values(): rank = (tuple([5] + handValues), bid, hand, "Four of a kind" )
        elif 3 in cardDict.values(): rank = (tuple([4] + handValues), bid, hand, "Full house")
        else: print("Error, missed something (length 2)")
    elif len(cardDict) == 3:
        if 3 in cardDict.values(): rank = (tuple([3] + handValues), bid, hand, "Three of a kind")
        elif 2 in cardDict.values(): rank = (tuple([2] + handValues), bid, hand, "Two pair")
        else: print("Error, missed something (length 3)")
    elif len(cardDict) == 4: rank = (tuple([1] + handValues), bid, hand, "One pair")
    elif len(cardDict) == 5: rank = (tuple([0] + handValues), bid, hand, "High card")
    else: print("Error, missed something")

    rankedCards.put(rank)

answer = 0
rank = 0
while rankedCards.qsize():
    rank += 1
    card = rankedCards.get()
    answer += int(card[1]) * rank

print(answer)
