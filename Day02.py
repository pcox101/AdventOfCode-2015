f = open("Day02.txt","r")
s = f.readlines()

t = 0
r = 0

for l in s:
    lwh = l.split("x")
    l = int(lwh[0])
    w = int(lwh[1])
    h = int(lwh[2])
    a1 = l * w
    a2 = w * h
    a3 = h * l
    t = t + (2 * (a1 + a2 + a3)) + min(a1, a2, a3)
    r = r + (2 * ((l + w + h) - max(l, w, h))) + (l * w * h)

print("Part 1: " + str(t))
print("Part 2: " + str(r))