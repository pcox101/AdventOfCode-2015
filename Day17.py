f = open("Day17.txt","r")
s = f.readlines()

s = list(map(lambda x: int(x), s))

visited = dict()
ways = dict()

def how_many_ways(remaining_size, used_items: list[int], remaining_items: list[int]):

    # base case, remaining size = 0. There is one way to do this
    if remaining_size == 0:
        used_key = str(used_items)
        if not used_key in ways:
            ways[used_key] = 1
        return

    for i in remaining_items:
        val = s[i]
        if remaining_size - val >= 0:
            new_remaining_list = list(remaining_items)
            new_remaining_list.remove(i)
            new_used_list = list(used_items)
            new_used_list.append(i)
            new_used_list.sort()
            
            key = str(remaining_size - val) + ":" + str(new_remaining_list)
            if not key in visited:
                visited[key] = 1
                how_many_ways(remaining_size - val, new_used_list, new_remaining_list)
    
    return

how_many_ways(150, list(), list(range(0,len(s))))

#print(visited)
#print(ways)

print("Part 1: " + str(len(ways)))

# For part 2 we need to get the minimum number of containers and then identify how many ways there are with that number of containers
m = 10**10
c = 0
for l in ways.keys():
    s = l[1:len(l) - 1]
    print(s)
    ln = s.split(", ")
    if len(ln) < m:
        m = len(ln)
        c = 1
    elif len(ln) == m:
        c += 1

print(m)
print("Part 2: " + str(c))