import re
import heapq

pattern = re.compile(r"^(\w+) => (\w+)$")

f = open("Day19.txt","r")
s = f.readlines()

replacements = list()

molecule = ""

for i in s:
    match = pattern.match(i)
    if match == None:
        molecule = i
    else:
        replacements.append((match.group(1), match.group(2)))

#print(replacements)
#print(molecule)

def get_possible_replacements(input):
    possible_ways = set()

    for replacement in replacements:
        places = re.finditer(replacement[0], input)
        for place in places:
            way = input[0:place.span(0)[0]] + replacement[1] + input[place.span(0)[1]:len(input)]
            possible_ways.add(way)
    
    return possible_ways

possible_ways = get_possible_replacements(molecule)

print("Part 1: " + str(len(possible_ways)))

# Part 2 looks like a BFS but we will reverse it
# Actually, BFS is too slow, we will implement Djikstra to prioritise the shortest string

new_replacements = list()
for r in replacements:
    new_replacements.append((r[1],r[0]))
replacements = new_replacements

visited = set()

q = []
heapq.heappush(q, (len(molecule), molecule, 0))

result = 0
while len(q) > 0:
    entry = heapq.heappop(q)

    if entry[1] == "e":
        result = entry[2]
        break

    reps = get_possible_replacements(entry[1])
    
    for rep in reps:
        if not rep in visited:
            visited.add(rep)
            heapq.heappush(q, (len(rep), rep, entry[2] + 1))
    
print("Part 2: " + str(result))
