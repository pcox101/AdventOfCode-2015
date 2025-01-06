inputString = "vzbxkghb"
input = list(inputString)

alphabet = "abcdefghijklmnopqrstuvwxyz"
valid3Strings = list()
valid2Strings = list()
for i in range(0,len(alphabet)):
    if i < len(alphabet) - 2:
        valid3Strings.append(alphabet[i:i + 3])
    valid2Strings.append(alphabet[i] + alphabet[i])

def getnext(input):
    increment = "abcdefghjkmnpqrstuvwxyz"
    currentIndex = len(input) - 1
    while True:
        char = input[currentIndex]
        val = increment.index(char)
        val += 1
        if val < len(increment):
            input[currentIndex] = increment[val]
            return input
        else:
            input[currentIndex] = "a"
            currentIndex -= 1
            continue

def isvalid(input):
    s = "".join(input)
    contains3 = False
    for ss in valid3Strings:
        if ss in s:
            contains3 = True
            break
    if not contains3:
        return False
    contains2 = 0
    for ss in valid2Strings:
        if ss in s:
            contains2 += 1
            if contains2 > 1:
                break
    if contains2 > 1:
        return True
    return False

while not isvalid(input):
    input = getnext(input)

print("Part 1: " + "".join(input))

input = getnext(input)
while not isvalid(input):
    input = getnext(input)

print("Part 2: " + "".join(input))
