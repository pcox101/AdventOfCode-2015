import numpy as np
import itertools

f = open("Day09.txt","r")
s = f.readlines()

locs = list()

arraysize = 0
total = 0
while True:
    arraysize += 1
    total += arraysize
    if (total == len(s)):
        break
arraysize += 1
matrix = np.zeros(shape=(arraysize,arraysize), dtype=int)

for i in s:
    spl = i.split(" to ")
    l1 = spl[0]
    spl = spl[1].split(" = ")
    l2 = spl[0]
    d = int(spl[1])

    i1 = 0
    if l1 in locs:
        i1 = locs.index(l1)
    else:
        locs.append(l1)
        i1 = len(locs) - 1

    i2 = 0
    if l2 in locs:
        i2 = locs.index(l2)
    else:
        locs.append(l2)
        i2 = len(locs) - 1

    matrix[i1][i2] = d
    matrix[i2][i1] = d

print(matrix)

def calculate_cost(route):
    total = 0
    n = len(route)
    for i in range(n - 1):
        total += matrix[route[i]][route[(i+1) % n]]
    return total

routes = itertools.permutations(range(0,arraysize))
mincost = 9**10
maxcost = 0
for r in routes:
    c = calculate_cost(r)
    mincost = min(mincost, c)
    maxcost = max(maxcost, c)
    
print("Part 1: " + str(mincost))
print("Part 2: " + str(maxcost))
