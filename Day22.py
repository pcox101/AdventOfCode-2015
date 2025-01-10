import heapq

##########
# CHANGE THIS VALUE FOR Part1 vs Part2
HARD_MODE = True

boss_hit_points = 71
boss_damage = 10

my_hit_points = 50
my_mana = 500

# Test case 1
#boss_hit_points = 13
#boss_damage = 8

#my_hit_points = 10
#my_mana = 250

# Test case 2
#boss_hit_points = 14
#boss_damage = 8

#my_hit_points = 10
#my_mana = 250

class spell:
    name = ""
    cost = 0
    damage = 0
    heal = 0
    armour = 0
    new_mana = 0
    mana_increase = 0
    timer = 0
    def __init__(self, name, cost, damage, heal, armour, mana_increase, timer):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.heal = heal
        self.armour = armour
        self.mana_increase = mana_increase
        self.timer = timer

spells = [spell("Magic Missile", 53,  4, 0, 0,   0, -1),
          spell("Drain", 73,  2, 2, 0,   0, -1),
          spell("Shield", 113, 0, 0, 7,   0, 6),
          spell("Poison", 173, 3, 0, 0,   0, 6),
          spell("Recharge", 229, 0, 0, 0, 101, 5)]

class spell_state:
    current_timer = 0
    spell_index = 0

class game_state:
    mana_spent = 0
    current_mana = my_mana
    current_hit_points = my_hit_points
    current_armour = 0
    current_boss_hit_points = boss_hit_points
    current_spells = []
    def __str__(self):
        return f"- Player has {self.current_hit_points} hit points, {self.current_armour} armor, {self.current_mana} mana\n- Boss has {self.current_boss_hit_points} hit points"
    def __lt__(self, other):
        return self.mana_spent < other.mana_spent
    def clone(self):
        c = game_state()
        c.mana_spent = self.mana_spent
        c.current_mana = self.current_mana
        c.current_hit_points = self.current_hit_points
        c.current_armour = self.current_armour
        c.current_boss_hit_points = self.current_boss_hit_points
        c.current_spells = list(self.current_spells)
        return c

def process_spells(process_state: game_state):
    new_state = process_state.clone()
    new_spells = list()
    for this_spell in new_state.current_spells:
        #print(spells[this_spell[1]].name + " is being cast or is still active; its timer is " + str(this_spell[0] - 1))
        # Armour effect - only affects state if ending
        if (spells[this_spell[1]].armour > 0) and this_spell[0] == 1:
            #print("Armour spell wore off")
            new_state.current_armour = 0
        # Otherwise deal the damage or increase our mana
        #print("Did " + str(spells[this_spell[1]].damage) + " damage.")
        new_state.current_boss_hit_points -= spells[this_spell[1]].damage
        #print("Increased mana by " + str(spells[this_spell[1]].mana_increase) + ".")
        new_state.current_mana += spells[this_spell[1]].mana_increase
        if (this_spell[0] > 1):
            new_spells.append((this_spell[0] - 1, this_spell[1]))
        #else:
            #print("Spell wore off")

    new_state.current_spells = new_spells
    
    return new_state


# This appears to be Dijkstra based on the least number of mana spent where the final state is a win
# So we sort on amount of mana spent

starting_state = game_state()
q = []

heapq.heappush(q, starting_state)

round = 1
while len(q) > 0:
    entry: game_state = heapq.heappop(q)

    # Player turn
    #print("\n-- Player Turn --")
    #print(entry)

    done = False

    # Play this turn

    current_state = entry.clone()
    if (HARD_MODE):
        current_state.current_hit_points -= 1
        if (current_state.current_hit_points <= 0):
            continue
    
    # Are there any spells active?
    current_state = process_spells(current_state)

    if (current_state.current_boss_hit_points <= 0):
        print("Part 1 or 2: " + str(current_state.mana_spent))
        done = True
        break
    
    # The player will always cast something if
    # we want to continue down this path
    for i in range(0,len(spells)):
#        if (round == 1):
#            if (spells[i].name != "Recharge"):
#                continue
#        elif (round == 2):
#            if (spells[i].name != "Shield"):
#                continue
#        elif (round == 3):
#            if (spells[i].name != "Drain"):
#                continue
#        elif (round == 4):
#            if (spells[i].name != "Poison"):
#                continue
#        elif (round == 5):
#            if (spells[i].name != "Magic Missile"):
#                continue
        
        already_being_played = False
        for sp in current_state.current_spells:
            if sp[1] == i:
                already_being_played = True
        if current_state.current_mana >= spells[i].cost and not already_being_played:
            new_state = current_state.clone()
            new_state.mana_spent += spells[i].cost
            new_state.current_mana -= spells[i].cost
            #print("Player casts " + spells[i].name)
            # Does the spell become effective immediately?
            if (spells[i].timer == -1):
                new_state.current_boss_hit_points -= spells[i].damage
                new_state.current_hit_points += spells[i].heal
                if (new_state.current_boss_hit_points <= 0):
                    print("Part 1 or 2: " + str(new_state.mana_spent))
                    done = True
                    break
            else:
                # Otherwise add it to the list of current spells
                new_state.current_spells.append((spells[i].timer, i))
                # And apply the armour
                new_state.current_armour += spells[i].armour

            # Now it's the boss's turn
            #print("\n-- Boss turn --")
            #print(new_state)

            new_state = process_spells(new_state)

            if (new_state.current_boss_hit_points <= 0):
                print("Part 1 or 2: " + str(new_state.mana_spent))
                done = True
                break

            #print("Boss attacks for " + str(boss_damage) + " (Armour is " + str(new_state.current_armour) + ")")
            new_state.current_hit_points -= (boss_damage - new_state.current_armour) 
            
            if (new_state.current_hit_points > 0):
                heapq.heappush(q, new_state)

        if done:
            break
        

    if done:
        break
    
    round += 1