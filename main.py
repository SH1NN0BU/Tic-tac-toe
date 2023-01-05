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

# Get the current result of the game
def get_result():
    win = ""
 
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"   
             
    return win

# The main program
game_over = False
player1 = True
 
while game_over == False:
 
    # Showing the map
    print_maps()
 
    # Let's ask the player where to make a move
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок 2, ваш ход: "))

# We make a move to the specified cell
    step_maps(step,symbol)

# Let's determine the winner
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False
 
    player1 = not(player1)        
 
#The game is over. Let's show the map. We will announce the winner.
print_maps()
print("Победил", win)