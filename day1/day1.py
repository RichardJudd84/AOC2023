#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

answer = 0

for line in res:
    line = [ch for ch in line if ch.isdigit()]
    line = int(line[0]+ line[-1])
    answer += line
    
print(answer)


# part two

#with open("sampleData2.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

days = {'one':'1', 'two': '2', 'three':'3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }
answer = 0
        
for line in res:
    line = line.lower()

    for key, val in zip(days.keys(), days.values()):
        line = line.replace(key, key[0]+val+key[-1])    
    
    line = [ch for ch in line if ch.isdigit()]
    line = int(line[0]+ line[-1])     

    answer += line

print(answer)   