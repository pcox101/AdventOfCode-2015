import re

f = open("Day16.txt","r")
s = f.readlines()

detected = {"children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1}

line_pattern = re.compile(r"^Sue (\d+): (.*)$")
item_pattern = re.compile(r"([a-z]+): (\d+)")

for i in s:
    lm = line_pattern.match(i)
    sue = int(lm.group(1))
    im = item_pattern.findall(lm.group(2))
    
    part1_happy = True
    part2_happy = True
    for e in im:
        if (detected[e[0]] != int(e[1])):
            part1_happy = False
        if (e[0] == "cats" or e[0] == "trees"):
            if (detected[e[0]] >= int(e[1])):
                part2_happy = False
        elif e[0] == "pomeranians" or e[0] == "goldfish":
            if (detected[e[0]] <= int(e[1])):
                part2_happy = False
        else:
            if (detected[e[0]] != int(e[1])):
                part2_happy = False

    if part1_happy:
        print("Part 1: " + str(sue))
    if part2_happy:
        print("Part 2: " + str(sue))
