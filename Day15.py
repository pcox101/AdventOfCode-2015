import re
import itertools
import numpy as np

linepattern = re.compile(r"^(\w*): capacity ([-\d]*), durability ([-\d]*), flavor ([-\d]*), texture ([-\d]*), calories ([-\d]*)$")

f = open("Day15.txt","r")
s = f.readlines()

items = list()

for l in s:
    match = linepattern.match(l)
    items.append([int(match.group(2)), int(match.group(3)), int(match.group(4)), int(match.group(5)), int(match.group(6))])

# We have to have 100 items in the knapsack
combs = itertools.product(range(0,100),repeat=len(items))

p1 = 0
p2 = 0
for c in combs:
    if sum(c) != 100:
        continue

    scores = np.empty(shape=(4, len(items)),dtype=int)
    
    for i in range(0,len(items)):
        scores[0][i] = items[i][0] * c[i]
        scores[1][i] = items[i][1] * c[i]
        scores[2][i] = items[i][2] * c[i]
        scores[3][i] = items[i][3] * c[i]

    # sum the rows and then multiply
    thisTotal = max(0,sum(scores[0])) * max(0,sum(scores[1])) * max(0,sum(scores[2])) * max(0,sum(scores[3]))
    p1 = max(thisTotal, p1)
    
    # Only consider this total for p2 if the total calories is 500
    totalCals = 0
    for i in range(0,len(items)):
        totalCals += c[i] * items[i][4]
    if (totalCals == 500):
        p2 = max(thisTotal, p2)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))