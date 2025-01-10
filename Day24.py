import itertools
import math

f = open("Day24.txt","r")
s = f.readlines()

# I'm tempted to say that this logic won't work for all examples, given that we need to find the group with the lowest
# product. It gives the right answer, and that is probably because we are working with a sorted list where, for example,
# 4x11 (44) is found before 5x10 (55) and 6x9 (54) but I can't be sure that that is always the case
def get_groups(group_to_split, number_of_groups):
    
    group_total = sum(group_to_split) // number_of_groups

    if number_of_groups == 1:
        return group_to_split
    
    for i in range(1,len(group_to_split) - 1):
        
        for firstList in (list(tup) for tup in itertools.combinations(group_to_split, i)):
            if sum(firstList) != group_total:
                continue

            remainingList = list(filter(lambda x: not x in firstList, group_to_split))

            # The remaining list needs to be split into (number_of_groups - 1) groups
            # Where each group adds up to the group_total
            possible_option = get_groups(remainingList, number_of_groups - 1)
            
            if len(possible_option) > 0:
                return firstList    
    
    return list()


weights = list(map(lambda x: int(x), s))

print("Part 1: " + str(math.prod(get_groups(weights, 3))))
print("Part 2: " + str(math.prod(get_groups(weights, 4))))