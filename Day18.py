import numpy as np

def get_new_value(row, column):
    neighbours = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    on_neighbours = 0
    for n in neighbours:
        nrow = row + n[0]
        ncolumn = column + n[1]
        if nrow >= 0 and nrow < len(gameboard) and ncolumn >= 0 and ncolumn < len(gameboard[nrow]):
            if gameboard[nrow][ncolumn]:
                on_neighbours += 1
        
    # A light which is on stays on when 2 or 3 neighbours are on and turns off otherwise
    if gameboard[row][column]:
        if on_neighbours == 2 or on_neighbours == 3:
            return True
        return False
    else:
        # A light which is off turns on if exactly 3 neighbours are on, and stays off otherwise
        if on_neighbours == 3:
            return True
        return False

def create_starting_gameboard(turn_on_corners = False):
    f = open("Day18.txt","r")
    s = f.readlines()
    
    gb = np.empty(shape=(len(s),len(s[0]) - 1), dtype=bool)

    for row in range(0,len(s)):
        for column in range(0,len(s[row]) - 1):
            gb[row][column] = s[row][column] == "#"

    if turn_on_corners:
        gb[0][0] = True
        gb[0][len(gb) - 1] = True
        gb[len(gb[0]) - 1][0] = True
        gb[len(gb[0]) - 1][len(gb) - 1] = True

    return gb

gameboard = create_starting_gameboard()

for counter in range(0,100):
    new_gameboard = np.empty(shape=(len(gameboard),len(gameboard[0])), dtype=bool)
    for row in range(0,len(gameboard)):
        for column in range(0,len(gameboard[row])):
            new_gameboard[row][column] = get_new_value(row, column)
    gameboard = new_gameboard

total = np.asarray(gameboard).sum()

print ("Part 1: " + str(total))

gameboard = create_starting_gameboard(True)

for counter in range(0,100):
    new_gameboard = np.empty(shape=(len(gameboard),len(gameboard[0])), dtype=bool)
    for row in range(0,len(gameboard)):
        for column in range(0,len(gameboard[row])):
            new_gameboard[row][column] = get_new_value(row, column)
            
    gameboard = new_gameboard
    gameboard[0][0] = True
    gameboard[0][len(gameboard) - 1] = True
    gameboard[len(gameboard[0]) - 1][0] = True
    gameboard[len(gameboard[0]) - 1][len(gameboard) - 1] = True

    #print(counter)
    #print(gameboard)

total = np.asarray(gameboard).sum()

print ("Part 2: " + str(total))
