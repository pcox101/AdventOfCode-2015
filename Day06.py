import re
import numpy as np

regex = re.compile(r"^([\w ]+) (\d*),(\d*) through (\d*),(\d*)$")

lightBoard1 = np.zeros(shape=(1000, 1000), dtype=np.int32)
lightBoard2 = np.zeros(shape=(1000, 1000), dtype=np.int32)

f = open("Day06.txt","r")
s = f.readlines()

for l in s:
    matches = regex.match(l)
    if matches.group(1) == "turn on":
        lightBoard1[int(matches.group(2)):int(matches.group(4)) + 1, int(matches.group(3)):int(matches.group(5)) + 1] = 1
        lightBoard2[int(matches.group(2)):int(matches.group(4)) + 1, int(matches.group(3)):int(matches.group(5)) + 1] += 1
    elif matches.group(1) == "turn off":
        lightBoard1[int(matches.group(2)):int(matches.group(4)) + 1, int(matches.group(3)):int(matches.group(5)) + 1] = 0
        lightBoard2[int(matches.group(2)):int(matches.group(4)) + 1, int(matches.group(3)):int(matches.group(5)) + 1] -= 1
        lightBoard2.clip(min = 0, out=lightBoard2)
    elif matches.group(1) == "toggle":
        lightBoard1[int(matches.group(2)):int(matches.group(4)) + 1, int(matches.group(3)):int(matches.group(5)) + 1] ^= 1
        lightBoard2[int(matches.group(2)):int(matches.group(4)) + 1, int(matches.group(3)):int(matches.group(5)) + 1] += 2

p1 = 0
p2 = 0

p1 = lightBoard1.sum()
p2 = lightBoard2.sum()

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
