import re

f = open("Day08.txt","r")
s = f.readlines()

total_characters = 0
total_memory = 0
for l in s:
    l = l.strip()
    total_memory += len(l)
    # Remove the quotes
    l = l[1:len(l) - 1]
    new_l = ""
    c = 0
    while c < len(l):
        if l[c] == "\\":
            if l[c + 1] == "\\" or l[c + 1] == "\"":
                new_l += l[c + 1]
                c += 1
            elif l[c + 1] == "x":
                c += 3
                new_l += "@"
            else:
                raise Exception("Invalid markup")
        else:
            new_l += l[c]
        c += 1
    
    total_characters += len(new_l)

print("Part 1: " + str(total_memory - total_characters))

total_original = 0
total_encoded = 0
for l in s:
    l = l.strip()
    total_original += len(l)
    c = 0
    new_l = "\""
    while c < len(l):
        if l[c] == "\\":
            new_l += "\\\\"
        elif l[c] == "\"":
            new_l += "\\\""
        else:
            new_l += l[c]
        c += 1
    new_l += "\""
    #print(l + " : " + new_l)
    
    total_encoded += len(new_l)

print("Part 2: " + str(total_encoded - total_original))
