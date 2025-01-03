import re

f = open("Day08.txt","r")
s = f.readlines()

total_characters = 0
total_memory = 0
for l in s:
    l = l.strip()
    total_memory += len(l)
    position = 1
    counter = 0
    while position < len(l) - 1:
        if l[position] == "\\":
            if l[position + 1] == "x":
                position += 3
            else:
                position += 1
        total_characters += 1
        position += 1

print("Part 1: " + str(total_memory - total_characters))

total_original = 0
total_encoded = 0
for l in s:
    l = l.strip()
    total_original += len(l)
    position = 0
    total_encoded += 2 # The quotes
    while position < len(l):
        if l[position] == "\\":
            total_encoded += 1
        elif l[position] == "\"":
            total_encoded += 1
        total_encoded += 1
        position += 1

print("Part 2: " + str(total_encoded - total_original))
