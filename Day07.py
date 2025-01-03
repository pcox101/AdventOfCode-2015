import re
import numpy as np

f = open("Day07.txt","r")
s = f.readlines()

two_input_gate = re.compile(r"^(\w*) (RSHIFT|OR|AND|LSHIFT) (\w*) -> (\w*)$")
one_input_gate = re.compile(r"^(NOT)? ?(\w*) -> (\w*)$")

class Gate:
    def __init__(self, name):
        self.name = name

class TwoInputGate(Gate):
    def __init__(self, name, input1, input2, type):
        self.name = name
        self.input1 = input1
        self.input2 = input2
        self.type = type

class OneInputGate(Gate):
    def __init__(self, name, input1, type):
        self.name = name
        self.input1 = input1
        self.type = type

gates = dict()
memo = dict()

for l in s:
    two = two_input_gate.match(l)
    one = one_input_gate.match(l)

    if two != None:
        g = TwoInputGate(two.group(4), two.group(1), two.group(3), two.group(2))
        gates[g.name] = g
    elif one != None:
        g = OneInputGate(one.group(3), one.group(2), one.group(1))
        gates[g.name] = g
    else:
        raise Exception("Invalid input")

def get_result(input):
    # if we have been passed a value, then just return this value
    if input.isnumeric():
        return input
    
    if input in memo:
        return memo[input]
    
    # find the gate with this name
    g = gates[input]
    
    # if this is a one input gate
    if isinstance(g, OneInputGate):
        # get the input value
        inp = get_result(g.input1)
        if (g.type == "NOT"):
            ret = np.invert(np.uint16(inp))
            memo[input] = ret
            return ret
        else:
            memo[input] = inp
            return inp
    elif isinstance(g, TwoInputGate):
        inp1 = get_result(g.input1)
        inp2 = get_result(g.input2)

        if g.type == "RSHIFT":
            ret = np.right_shift(np.uint32(inp1), np.uint32(inp2))
            memo[input] = ret
            return ret
        elif g.type == "LSHIFT":
            ret = np.left_shift(np.uint32(inp1), np.uint32(inp2))
            memo[input] = ret
            return ret
        elif g.type == "OR":
            ret = np.bitwise_or(np.uint32(inp1), np.uint32(inp2))
            memo[input] = ret
            return ret
        elif g.type == "AND":
            ret = np.bitwise_and(np.uint32(inp1), np.uint32(inp2))
            memo[input] = ret
            return ret
        else:
            raise Exception("Invalid type " + g.type)
    else:
        raise Exception("No gate found " + input)

p1 = get_result("a")
# Reset with b = result of a and then go again
memo.clear()
gates["b"].input1 = str(p1)
p2 = get_result("a")

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))