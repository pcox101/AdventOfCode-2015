import re

f = open("Day05.txt","r")
s = f.readlines()

p1 = 0
p2 = 0

v = re.compile(r"a|e|i|o|u")
dub = re.compile(r"(.)\1{1}")
dis = re.compile(r"ab|cd|pq|xy")

one_apart = re.compile(r"(.).\1{1}")
pairofpairs = re.compile(r"(..).*\1{1}")
    
for l in s:
    if len(v.findall(l)) > 2 and len(dub.findall(l)) > 0 and len(dis.findall(l)) == 0:
        p1 += 1
    
    if len(one_apart.findall(l)) > 0 and len(pairofpairs.findall(l)) > 0:
        p2 += 1   

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
