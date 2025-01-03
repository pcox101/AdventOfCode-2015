import re
import numpy as np

on = re.compile(r"^turn on (\d*),(\d*) through (\d*),(\d*)$")
off = re.compile(r"^turn off (\d*),(\d*) through (\d*),(\d*)$")
toggle = re.compile(r"^toggle (\d*),(\d*) through (\d*),(\d*)$")

lightBoard1 = np.empty(shape=(1000, 1000), dtype=np.bool)
lightBoard2 = np.empty(shape=(1000, 1000), dtype=np.int32)
for x in range(0,1000):
    for y in range(0,1000):
        lightBoard1[x,y] = False
        lightBoard2[x,y] = 0

f = open("Day06.txt","r")
s = f.readlines()

for l in s:
    turnOn = on.match(l)
    turnOff = off.match(l)
    toggled = toggle.match(l)
    if (turnOn != None):
        for x in range(int(turnOn.group(1)),int(turnOn.group(3)) + 1):
            for y in range(int(turnOn.group(2)),int(turnOn.group(4)) + 1):
                lightBoard1[x,y] = True
                lightBoard2[x,y] += 1
    elif (turnOff != None):
        for x in range(int(turnOff.group(1)),int(turnOff.group(3)) + 1):
            for y in range(int(turnOff.group(2)),int(turnOff.group(4)) + 1):
                lightBoard1[x,y] = False
                lightBoard2[x,y] -= 1
                if (lightBoard2[x,y] < 0):
                    lightBoard2[x,y] = 0
    elif (toggled != None):
        for x in range(int(toggled.group(1)),int(toggled.group(3)) + 1):
            for y in range(int(toggled.group(2)),int(toggled.group(4)) + 1):
                lightBoard1[x,y] = not lightBoard1[x,y]
                lightBoard2[x,y] += 2

p1 = 0
p2 = 0
for x in range(0,1000):
    for y in range(0,1000):
        if lightBoard1[x,y]:
            p1 += 1
        p2 += lightBoard2[x,y]

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
