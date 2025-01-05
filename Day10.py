def look_and_say(s):
    inNumber = ""
    counter = 1
    output = ""
    for i in s:
        if inNumber == "":
            inNumber = i
            counter = 1
        elif i == inNumber:
            counter += 1
        else:
            output += str(counter) + inNumber
            inNumber = i
            counter = 1
    output += str(counter) + inNumber
    return output

input = "1113222113"

for i in range(0,40):
    input = look_and_say(input)

print("Part 1: " + str(len(input)))

for i in range(40,50):
    input = look_and_say(input)

print("Part 2: " + str(len(input)))
