import re
#with open("sampleData.txt", "r" ) as data:
with open("input.txt", "r" ) as data:
    res = data.readlines()

times = re.findall("[\d]+", res[0])
distances = re.findall("[\d]+", res[1])

def getTimes(minDistance, time): 
    times = 0   
    speed = 0
    distanceTraveled = 0
    speed = 0
    while time > 0:
        speed += 1
        time -= 1
        distanceTraveled = speed * time
        if distanceTraveled > minDistance:
            times+=1

    return times

answer = 1      
for time, distance in zip(times, distances):
    answer *= getTimes(int(distance), int(time))

print(answer)

# part 2

time = "".join(times) 
distance = "".join(distances)

print(getTimes(int(distance), int(time)))