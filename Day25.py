required_col = 3075
required_row = 2981

row = 1
col = 1
value = 20151125

while True:
    if row == required_row and col == required_col:
        print ("Part 1: " + str(value))
        break

    row = row - 1
    col = col + 1
    if (row == 0):
        row = col
        col = 1
    
    value = (value * 252533) % 33554393
