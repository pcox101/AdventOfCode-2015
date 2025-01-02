f = open("Day03.txt","r")
s = f.readline()

x = 0
y = 0
locs = set()
locs.add("0,0")

for m in s:
    match m:
        case ">":
            x = x + 1
        case "v":
            y = y - 1
        case "<":
            x = x - 1
        case "^":
            y = y + 1
    locs.add(str(x) + "," + str(y))

print("Part 1: " + str(len(locs)))

sx = 0
sy = 0
rx = 0
ry = 0

s_locs = set()
s_locs.add("0,0")
r_locs = set()
r_locs.add("0,0")

roboSanta = False
for m in s:
    match m:
        case ">":
            if roboSanta:
               rx = rx + 1
            else:
               sx = sx + 1
        case "v":
            if roboSanta:
               ry = ry - 1
            else:
               sy = sy - 1
        case "<":
            if roboSanta:
               rx = rx - 1
            else:
               sx = sx - 1
        case "^":
            if roboSanta:
               ry = ry + 1
            else:
               sy = sy + 1

    roboSanta = not roboSanta
    r_locs.add(str(rx) + "," + str(ry))
    s_locs.add(str(sx) + "," + str(sy))

locs = r_locs.union(s_locs)

print("Part 2: " + str(len(locs)))