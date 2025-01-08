# Can't be bothered parsing the input file...
boss_hit = 103
boss_damage = 9
boss_armour = 2

my_hit = 100

# The rules are we can buy 1 weapon, 0-1 armour, 0-2 rings
# So include the "null" option
weapons = [(8,4,0), (10,5,0), (25,6,0), (40,7,0), (74,8,0)]
armour = [(0,0,0), (13,0,1), (31,0,2), (53,0,3), (75,0,4), (102,0,5)]
rings = [(0,0,0), (25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3)]


# Build our list of possible options
options = []
for w in weapons:
    for a in armour:
        for r1 in rings:
            for r2 in rings:
                if (r1 == r2) and r1[0] != 0:
                    continue
                options.append((sum((w[0],a[0],r1[0],r2[0])),sum((w[1],a[1],r1[1],r2[1])),sum((w[2],a[2],r1[2],r2[2]))))
                
# sort the options by the first value to give us an ordered by lowest spend
options.sort()

# Now play each option in order
for option in options:
    my_damage = option[1]
    my_armour = option[2]

    boss_relative = max(1, my_damage - boss_armour)
    my_relative = max(1, boss_damage - my_armour)

    boss_current_hit = boss_hit
    my_current_hit = my_hit

    while True:
        boss_current_hit -= boss_relative
        if boss_current_hit <= 0:
            print("Part 1: " + str(option[0]))
            break
        my_current_hit -= my_relative
        if my_current_hit <= 0:
            break

    if boss_current_hit <= 0:
        break

# Reverse the sort
options.sort(reverse=True)

for option in options:
    my_damage = option[1]
    my_armour = option[2]

    boss_relative = max(1, my_damage - boss_armour)
    my_relative = max(1, boss_damage - my_armour)

    boss_current_hit = boss_hit
    my_current_hit = my_hit

    while True:
        boss_current_hit -= boss_relative
        if boss_current_hit <= 0:
            break
        my_current_hit -= my_relative
        if my_current_hit <= 0:
            print("Part 2: " + str(option[0]))
            break

    if my_current_hit <= 0:
        break