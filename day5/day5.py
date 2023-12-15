import re
#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

seeds = re.findall("[\d]+",res[0])
results = []

for seed in seeds:
    found = False 
    seed = int(seed)
    for i in range(len(res)):                       

        line = res[i]
        line = line.strip()
        if ':' in line:
            continue

        if line == "": 
            found = False        
            continue      

        line = tuple(re.findall("[\d]+",line))
        mappedVal = int(line[0])
        seedVal = int(line[1])
        reps = int(line[2])

        if seed >= seedVal and seed < seedVal+reps and not found:
            found = True
            offset = mappedVal-seedVal
            seed += offset
   
    results.append(seed)

print(min(results))


# part 2

seedRanges = []
for i in range(0,len(seeds),2):
    seedRanges.append([(int(seeds[i]), int(seeds[i])+int(seeds[i+1])-1)])

answer = 100000000

for seedRange in seedRanges:  
    foundRanges = set()
    unfoundRanges = set()

    for i in range(len(res)):        
        line = res[i]
        line = line.strip()

        if ':' in line:
            continue

        if line == "": 
            seedRange += list(foundRanges)
            foundRanges = set()
            unfoundRanges = set()
            continue   
        
        line = tuple(re.findall("[\d]+",line))
        mappedVal = int(line[0])
        rangeMin = int(line[1])
        reps = int(line[2])
        offset = mappedVal-rangeMin
        rangeMax = rangeMin + reps

        for seedMin,seedMax in seedRange:
            # no match  
            if seedMin >= rangeMax or seedMax < rangeMin:
                unfoundRanges.add((seedMin, seedMax))
            # complete match
            elif seedMin >= rangeMin and seedMax < rangeMax:
                foundRanges.add((seedMin + offset, seedMax + offset))
            # min match, max no match
            elif seedMin >= rangeMin and seedMin < rangeMax and seedMax >= rangeMax:
                foundRanges.add((seedMin + offset , rangeMax-1 + offset))
                unfoundRanges.add((rangeMax , seedMax))
            # min no match, max match
            elif seedMin < rangeMin and seedMax >= seedMin and seedMax < rangeMax:
                unfoundRanges.add((seedMin, rangeMin-1))
                foundRanges.add((rangeMin + offset, seedMax + offset))
            # min no match, middle match, max no match 
            elif seedMin < rangeMin and seedMax >= rangeMax:
                unfoundRanges.add((seedMin, rangeMin-1))
                foundRanges.add((rangeMin + offset, rangeMax-1 + offset))
                unfoundRanges.add((rangeMax , seedMax))
            # errors
            else:
                print("Missed combination")

        seedRange = list(unfoundRanges)
        unfoundRanges = set()

    seedRange += list(foundRanges)
    for lMin , lMax in seedRange:
        if lMin < answer:
            answer = lMin

print(answer)

