# with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

cubeBag = {'red': 12, 'green': 13, 'blue': 14}
answer = 0 
gameNr = 0

for game in res:
    gameNr +=1
    gamePossible = True

    game = game.strip()
    game = game.split(':')
    sets = game[1].split(';')    

    for set in sets:
        colours = set.split(',')
        for colour in colours:
            colour = colour.strip()
            colour = colour.split()
            key = colour[1]
            val = int(colour[0])

            if val > cubeBag[key]: 
                gamePossible = False
    if gamePossible:
        answer += gameNr

print(answer)


# part 2

#with open("sampleData2.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

answer = 0 
gameNr = 0

for game in res:
    gameNr +=1
    cubeBag = {'red': 0, 'green': 0, 'blue': 0}
    
    game = game.strip()
    game = game.split(':')
    sets = game[1].split(';')

    for set in sets:
        colours = set.split(',')
        for colour in colours:
            colour = colour.strip()
            colour = colour.split()
            key = colour[1]
            val = int(colour[0])

            if val > cubeBag[key]: 
                cubeBag[key] = val

    power = 1
    for val in cubeBag.values(): 
        power *= val        
    answer += power

print(answer)
