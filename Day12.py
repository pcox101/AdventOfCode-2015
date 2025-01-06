import json

f = open("Day12.txt","r")
p = json.load(f)

def getSum(l,ignoreRed = False):
    tot = 0
    for i in l:
        if isinstance(i, list):
           tot = tot + getSum(i, ignoreRed)
        elif isinstance(i, dict):
           if ignoreRed:
              # See if we have an element with value "red"
              thisList = i.values()
              if not ("red" in thisList):
                 tot = tot + getSum(thisList, ignoreRed)
           else:   
              tot = tot + getSum(i.values(), ignoreRed)
        elif isinstance(i, int):
           tot = tot + i
    return tot

i = getSum(p.values())
print("Part 1: " + str(i))

i = getSum(p.values(), True)
print("Part 2: " + str(i))
