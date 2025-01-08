from sympy import divisors

input = 33100000

# The total number of presents delivered is 10 * (sum of divisors)
# i.e. for 8, the divisors are 1,2,4 & 8 meaning there are 150 presents delivered to house number 8

# So we need to find the first number for which all the divisors sum to more than the input

# For part 2, the sum calculation becomes more difficult. Each elf now delivers only 50 times
# bu 11 presents each time
house_number = 1
part1_done = False
part2_done = False
while not (part1_done and part2_done):
    house_number += 1
    divs = divisors(house_number)
    if (not part1_done):
        part1_val = sum(divs) * 10
        if (part1_val >= input):
            print("Part 1: " + str(house_number))
            part1_done = True
    # Remove from our list of divisors where the divisor is greater than the counter divided by 50
    # as they will have delivered 50 times and therefore shouldn't be included
    if not (part2_done):
        limit = (house_number - 1) // 50
        divs = list(filter(lambda divisor: divisor > limit, divs))
        #print(str(counter) + ": " + str(divs))
        part2_val = sum(divs) * 11
        if (part2_val >= input):
            print("Part 2: " + str(house_number))
            part2_done = True
