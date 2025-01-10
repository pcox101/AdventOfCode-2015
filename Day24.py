import itertools
import math

f = open("Day24.txt","r")
s = f.readlines()

weights = list(map(lambda x: int(x), s))
weights.sort()

def get_part_one():

    group_total = sum(weights) // 3
    print(group_total)

    for i in range(1,len(weights) - 1):
        print("Testing length : " + str(i))
        possible_options = list()
        for firstList in (list(tup) for tup in itertools.combinations(weights, i)):
            if sum(firstList) != group_total:
                continue

            qe = math.prod(firstList)

            # No need to check it if it's not already better
            if len(possible_options) > 0 and qe >= min(possible_options):
                continue
            
            foundOptionForThisGroup = False
            remainingList = list(filter(lambda x: not x in firstList, weights))

            for j in range(1, len(remainingList) - 1):
                for secondList in (list(tup) for tup in itertools.combinations(remainingList, j)):
                    if sum(secondList) != group_total:
                        continue

                    print("Found option - qe = " + str(qe))
                    possible_options.append(qe)
                    foundOptionForThisGroup = True
                    break
                
                if foundOptionForThisGroup:
                    break
            if foundOptionForThisGroup:
                break
        if (len(possible_options) > 0):
            break

    # Get the lowest quantum entanglement
    return min(possible_options)

def get_part_two():
    
    group_total = sum(weights) // 4
    print(group_total)
    
    for i in range(1,len(weights) - 1):
        print("Testing length : " + str(i))
        possible_options = list()
        for firstList in (list(tup) for tup in itertools.combinations(weights, i)):
            if sum(firstList) != group_total:
                continue
            
            qe = math.prod(firstList)

            # No need to check it if it's not already better
            if len(possible_options) > 0 and qe >= min(possible_options):
                continue
            
            remainingListAfterFirst = list(filter(lambda x: not x in firstList, weights))

            foundOptionForThisGroup = False
            for j in range(1, len(remainingListAfterFirst) - 1):
                for secondList in (list(tup) for tup in itertools.combinations(remainingListAfterFirst, j)):
                    if (sum(secondList) != group_total):
                        continue
                    
                    remainingListAfterSecond = list(filter(lambda x: not x in secondList, remainingListAfterFirst))

                    for k in range(1, len(remainingListAfterSecond) - 1):
                        for thirdList in (list(tup) for tup in itertools.combinations(remainingListAfterSecond, k)):
                            fourthList = list(filter(lambda x: not x in thirdList, remainingListAfterSecond))

                            if sum(thirdList) != group_total:
                                continue
                    
                            print("Found option - qe = " + str(qe))
                            possible_options.append(qe)
                            foundOptionForThisGroup = True
                            break

                        if foundOptionForThisGroup:
                            break
                    if foundOptionForThisGroup:
                        break
                if foundOptionForThisGroup:
                        break
        
        if len(possible_options) > 0:
            break

    # Get the lowest quantum entanglement
    return min(possible_options)

print("Part 1: " + str(get_part_one()))
print("Part 2: " + str(get_part_two()))