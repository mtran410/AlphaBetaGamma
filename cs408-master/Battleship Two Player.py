from random import randint

#Initialize variables
board_one = []
board_two = []

ship_row_one = []
ship_col_one = []

ship_row_two = []
ship_col_two = []

turn = 0
counter = 0

p1_battleship = 3
p2_battleship = 3

#Set the boards
for x in range(5):
    board_one.append(["O"] * 5)
    board_two.append(["O"] * 5)

#Print the boards   
def print_board(board):
    for row in board:
        print(" ".join(row))

#Display the boards nicely
def display():
    print()
    print("Player 1 board")
    print_board(board_one)
    print()
    print()
    print("Player 2 board")
    print_board(board_two)
    print()

#Check if battleship has been sunk
def is_battleship_sunk(row, col, g_row, g_col):    
    for index in range(len(row)):
        if g_row == row[index] and g_col == col[index]:
            row.remove(row[index])
            col.remove(col[index])
            return True
    return False

#Player 1 coordinates for battleships
for x in range(3):
    print("Player1 enter coordinates for your battleship ", x+1)
    ship_row_one.append(int(input("Row:")))
    ship_col_one.append(int(input("Col:")))

#Player 2 coordinates for battleships
for x in range(3):
    print("Player2 enter coordinates for your battleship", x+1)
    ship_row_two.append(int(input("Row:")))
    ship_col_two.append(int(input("Col:")))

print("Let's play Battleship!")
display()

#Start the game    
while(True):
    
    flag = False
    while(flag == False):
        
        #Player 1 Guess row & col
        print("Player 1 Guess:")
        guess_row_one = int(input("Guess Row:"))
        guess_col_one = int(input("Guess Col:"))
        print()

        #Check if its a hit
        if is_battleship_sunk(ship_row_two, ship_col_two, guess_row_one, guess_col_one):
            print("Congratulations! You sunk my battleship!")
            board_two[guess_row_one][guess_col_one] = "!"
            display()
            p2_battleship = p2_battleship - 1
            flag = True
            
        #Check if its a valid move    
        else:
            if (guess_row_one < 0 or guess_row_one > 4) or (guess_col_one < 0 or guess_col_one > 4):
                print("Oops, that's not even in the ocean.")
                print()
                
            elif(board_two[guess_row_one][guess_col_one] == "X" or
                 board_two[guess_row_one][guess_col_one] == "!"):
                print("You guessed that one already.")
                print()
                
            else:
                print("You missed Player 2's battleship!")
                board_two[guess_row_one][guess_col_one] = "X"
                display()
                flag = True

    #reset flag
    flag = False
            
    while(flag == False):

        #Player 2 Guess row & col
        print("Player 2 Guess:")
        guess_row_two = int(input("Guess Row:"))
        guess_col_two = int(input("Guess Col:"))
        print()

        #Check if its a hit
        if is_battleship_sunk(ship_row_one, ship_col_one, guess_row_two, guess_col_two):
            print("Congratulations! You sunk my battleship!")
            board_one[guess_row_two][guess_col_two] = "!"
            display()
            p1_battleship = p1_battleship - 1
            flag = True

        #Check if its a valid move    
        else:
            if (guess_row_two < 0 or guess_row_two > 4) or (guess_col_two < 0 or guess_col_two > 4):
                print("Oops, that's not even in the ocean.")
                print()
                
            elif(board_one[guess_row_two][guess_col_two] == "X" or
                 board_one[guess_row_two][guess_col_two] == "!"):
                print("You guessed that one already.")
                print()
                
            else:
                print("You missed Player 1's battleship!")
                board_one[guess_row_two][guess_col_two] = "X"
                display()
                flag = True
                
    #Check if battleships from player 1 or player 2 have been depleted    
    if p1_battleship == 0 or p2_battleship == 0:
        break;
        
print("Game Over")

if p1_battleship == 0:
    print("Player 2 Wins!")
else:
    print("Player 1 Wins!")










