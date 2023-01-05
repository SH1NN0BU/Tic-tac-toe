# Console game Tic Tac Toe

# Card Initialization
maps [1,2,3,
      4,5,6,
      7,8,9]
# Initialization of winning lines

victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

# Displaying the map on the screen
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])

# Make a move to the cell
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol