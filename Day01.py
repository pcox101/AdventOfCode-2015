f = open("Day01.txt","r")
s = f.readline()

c = 0
p = 1
p2done = False

for n in s:
    if n == "(":
        c = c + 1
    else:
        c = c - 1
    if c == -1 and p2done == False:
        print("Part 2: " + str(p))
        p2done = True
    p = p + 1

print("Part 1: " + str(c))