import re
import numpy as np
import itertools

def calculate_net_happiness(combo, thismatrix):
    total = 0
    for i in range(0,len(combo)):
        i1 = i - 1
        if (i1 < 0):
            i1 = len(combo) - 1
        i2 = i + 1
        if i2 == len(combo):
            i2 = 0

        p = people.index(combo[i])
        p1 = people.index(combo[i1])
        p2 = people.index(combo[i2])

        total += thismatrix[p][p1] + thismatrix[p][p2]

    return total 

line_match = re.compile(r"^(\w*) would (gain|lose) (\d*) happiness units by sitting next to (\w*).$")

f = open("Day13.txt","r")
s = f.readlines()

# Work out how many people there are and their names
people = set()
for i in s:
    matches = line_match.match(i)
    people.add(matches.group(1))

matrix = np.zeros(shape=(len(people),len(people)), dtype=int)

people = list(people)

# Now populate our ordered matrix
for i in s:
    matches = line_match.match(i)
    v = int(matches.group(3))
    if (matches.group(2) == "lose"):
        v *= -1
    matrix[people.index(matches.group(1))][people.index(matches.group(4))] = v

# Now attempt every permutation
combos = itertools.permutations(people)

total = 0
for combo in combos:
    total = max(total, calculate_net_happiness(combo, matrix))

print("Part 1: " + str(total))

# Add me to the end of the list, rebuild the matrix and go again
people.append("Me")

newmatrix = np.zeros(shape=(len(people),len(people)), dtype=int)
for i in range(0,len(people) - 1):
    for j in range(0,len(people) - 1):
        newmatrix[i][j] = matrix[i][j]
    
combos = itertools.permutations(people)
total = 0
for combo in combos:
    total = max(total, calculate_net_happiness(combo, newmatrix))

print("Part 2: " + str(total))
