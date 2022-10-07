#REQUIREMENTS

#Implement the following features:

#the board should be stored as a three-element list, while each element is another three-element list (the inner lists represent rows) so that all of the squares may be accessed using the following syntax:

#each of the inner list's elements can contain 'O', 'X', or a digit representing the square's number (such a square is considered free)
#the board's appearance should be exactly the same as the one presented in the example.
#implement the functions defined for you in the editor.

from random import randrange

row_1=[1,2,3]
row_2=[4,'X',6]
row_3=[7,8,9]
empty_fields=[1,2,3,4,6,7,8,9]

def display_board(line_1,line_2,line_3):
    for i in range(4):
        if i % 4 == 0:
            print("+-------+-------+-------+")
        elif i % 2 ==1:
            print("|       |       |       |")
        else:
            print("|  ",line_1[i-2]," ","|  ",line_1[i-1]," ","|  ",line_1[i],"  |")

    for i in range(4):
        if i % 4 == 0:
            print("+-------+-------+-------+")
        elif i % 2 ==1:
            print("|       |       |       |")
        else:
            print("|  ",line_2[i-2]," ","|  ",line_2[i-1]," ","|  ",line_2[i],"  |")

    for i in range(5):
        if i % 4 == 0:
            print("+-------+-------+-------+")
        elif i % 2 ==1:
            print("|       |       |       |")
        else:
            print("|  ",line_3[i-2]," ","|  ",line_3[i-1]," ","|  ",line_3[i],"  |")

def update_empty_fields(move):
    for i in range(len(empty_fields)):
      if empty_fields[i] == move:
        j=i  
        break 
    del empty_fields[j]

def enter_move(move):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    print(move)

    if move < 4:
        row_1[move-1]='0'
        update_empty_fields(move)
        
    elif move > 3 and move < 7:
        row_2[move-4]='0'
        update_empty_fields(move)

    elif move > 6:
        row_3[move-7]='O'
        update_empty_fields(move)

    print(display_board(row_1,row_2,row_3))
    
def computer_move():
    # The function enter and draws computer's random move
    move=randrange(1,10,1)
    print('The computer plays ', move)
    if move not in empty_fields:
        move=randrange(1,9,1)
        computer_move()

    elif move < 4:
        row_1[move-1]='X'
        update_empty_fields(move)
        
    elif move > 3 and move < 7:
        row_2[move-4]='X'
        update_empty_fields(move)

    elif move > 6:
        row_3[move-7]='X'
        update_empty_fields(move)

    print(display_board(row_1,row_2,row_3))


#def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    


###############MAIN########################


print(display_board(row_1,row_2,row_3)) #initial board display

while empty_fields != []:

  move=int(input('Please Enter a valid move'))

  if move not in empty_fields:
    print('Impossible move ')
    continue

  enter_move(move)

  computer_move()

