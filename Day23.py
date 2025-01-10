import re

f = open("Day23.txt","r")
s = f.readlines()

hlf = re.compile(r"^hlf ([ab])$")
tpl = re.compile(r"^tpl ([ab])$")
inc = re.compile(r"^inc ([ab])$")
jmp = re.compile(r"^jmp ([+-]\d+)$")
jie = re.compile(r"^jie ([ab]), ([+-]\d+)$")
jio = re.compile(r"^jio ([ab]), ([+-]\d+)$")


def run_program(ip, a, b):
    while ip >= 0 and ip < len(s):
        ins = s[ip]
        m = hlf.match(ins)
        if (m != None):
            if (m.group(1) == "a"):
                a //= 2
            elif (m.group(1) == "b"):
                b //= 2
            ip += 1
            continue
        m = tpl.match(ins)
        if (m != None):
            if (m.group(1) == "a"):
                a *= 3
            elif (m.group(1) == "b"):
                b *= 3
            ip += 1
            continue
        m = inc.match(ins)
        if (m != None):
            if (m.group(1) == "a"):
                a += 1
            elif (m.group(1) == "b"):
                b += 1
            ip += 1
            continue
        m = jmp.match(ins)
        if (m != None):
            ip += int(m.group(1))
            continue
        m = jie.match(ins)
        if (m != None):
            v = a
            if (m.group(1) == "b"):
                v = b
            if (v % 2) == 0:
                ip += int(m.group(2))
            else:
                ip += 1
            continue
        m = jio.match(ins)
        if (m != None):
            v = a
            if (m.group(1) == "b"):
                v = b
            if (v == 1):
                ip += int(m.group(2))
            else:
                ip += 1
            continue
    return b


print("Part 1: " + str(run_program(0,0,0)))
print("Part 2: " + str(run_program(0,1,0)))
