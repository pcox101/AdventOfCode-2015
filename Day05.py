f = open("Day05.txt","r")
s = f.readlines()

p1 = 0

for l in s:
    vowels = 0
    double = False
    disallowed = False

    prev = " "
    for c in l:
        if c in "aeiou":
            vowels += 1
        if (c == prev):
            double = True
        dis = prev + c
        if dis in "ab,cd,pq,xy":
            disallowed = True
            break
        prev = c

    if not disallowed and vowels > 2 and double:
        p1 += 1
    
print("Part 1: " + str(p1))

p2 = 0
for l in s:

    pairs = set()
    prev = " "
    prevprev = " "

    pairofpairs = False
    repeat2apart = False

    for c in l:

        if (c == prevprev):
            repeat2apart = True
        d = prev + c
        if (d in pairs) and not (c == prev and c == prevprev):
            pairofpairs = True
        pairs.add(d)
        
        prevprev = prev
        prev = c

    if repeat2apart and pairofpairs:
        p2 += 1

print("Part 2: " + str(p2))
