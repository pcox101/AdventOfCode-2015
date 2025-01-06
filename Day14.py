import re
import numpy as np

def calculate_distance(seconds, travelling_time, rest_time, speed):
    loops = int(seconds / (travelling_time + rest_time))
    remainder = seconds % (travelling_time + rest_time)
    distance = loops * speed * travelling_time
    if remainder > travelling_time:
        distance += speed * travelling_time
    else:
        distance += speed * remainder
    return distance

linepattern = re.compile(r"^(\w*) can fly (\d*) km\/s for (\d*) seconds, but then must rest for (\d*) seconds\.$")

f = open("Day14.txt","r")
s = f.readlines()

part1 = 0

reindeer = list()

for l in s:
    match = linepattern.match(l)

    speed = int(match.group(2))
    travelling_time = int(match.group(3))
    rest_time = int(match.group(4))
    reindeer.append([travelling_time, rest_time, speed])
    
    part1 = max(part1, calculate_distance(2503, travelling_time, rest_time, speed))

print("Part 1: " + str(part1))

# Part 2 is different, we need to play through until we reach the end
scores = np.zeros(shape=(len(reindeer)), dtype=np.int32)

for i in range(1,2504):
    l = np.zeros(shape=(len(reindeer)), dtype=np.int32)
    for r in range(0,len(reindeer)):
        l[r] = calculate_distance(i, reindeer[r][0], reindeer[r][1], reindeer[r][2])
    scores[l.argmax()] += 1

print("Part 2: " + str(max(scores)))
