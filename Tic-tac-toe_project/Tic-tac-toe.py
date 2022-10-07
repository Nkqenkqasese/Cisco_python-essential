#REQUIREMENTS

#Implement the following features:

#the board should be stored as a three-element list, while each element is another three-element list (the inner lists represent rows) so that all of the squares may be accessed using the following syntax:

#each of the inner list's elements can contain 'O', 'X', or a digit representing the square's number (such a square is considered free)
#the board's appearance should be exactly the same as the one presented in the example.
#implement the functions defined for you in the editor.

import math
from random import randrange

board=[[1,2,3],[4,'X',6],[7,8,9]]
empty_fields=[1,2,3,4,6,7,8,9]

def display_board(matrix):
    for i in range(13):
            if i % 4 == 0:
                print("+-------+-------+-------+")
            elif i % 2 ==1:
                print("|       |       |       |")
            else:
                print("|  ",matrix[math.floor(i/4-1/2)][0]," ","|  ",matrix[math.floor(i/4-1/2)][1]," ","|  ",matrix[math.floor(i/4-1/2)][2],"  |")

def update_empty_fields(move):
    for i in range(len(empty_fields)):
      if empty_fields[i] == move:
        j=i  
        break 
    del empty_fields[j]

def victory_for(matrix,sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    for i in range(3):
        if matrix[i]==[sign,sign,sign]: 
            return True
    
    if matrix[0][0] == matrix[1][0] and matrix[0][0] == matrix[2][0]:
        return True
    
    elif matrix[0][1] == matrix[1][1] and matrix[0][1] == matrix[2][1]:
        return True
    
    elif matrix[0][2] == matrix[1][2] and matrix[0][2] == matrix[2][2]:
        return True
        
    elif matrix[0][0] == matrix[2][2] or matrix[0][2] == matrix[2][0]:
        return True

    elif len(empty_fields) == 0:
        return True
    else:
        print('Game is not over !')
        return False

def enter_move(move):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    print(move)

    if move==1:
        board[0][0]='O'
        update_empty_fields(move)
        
    if move==2:
        board[0][1]='O'
        update_empty_fields(move)
        
    if move==3:
        board[0][2]='O'
        update_empty_fields(move)
        
    if move==4:
        board[1][0]='O'
        update_empty_fields(move)
        
    if move==6:
        board[1][2]='O'
        update_empty_fields(move)
        
    if move==7:
        board[2][0]='O'
        update_empty_fields(move)
        
    if move==8:
        board[2][1]='O'
        update_empty_fields(move)
        
    if move==9:
        board[2][2]='O'
        update_empty_fields(move)
    

    print(display_board(board))
    
def computer_move():
    # The function enter and draws computer's random move
    move=randrange(0,10,1)
    print('The computer plays ', move)
    if move not in empty_fields:
        move=randrange(1,10,1)
        computer_move()

    if move==1:
        board[0][0]='X'
        update_empty_fields(move)
        
    if move==2:
        board[0][1]='X'
        update_empty_fields(move)
        
    if move==3:
        board[0][2]='X'
        update_empty_fields(move)
        
    if move==4:
        board[1][0]='X'
        update_empty_fields(move)
        
    if move==6:
        board[1][2]='X'
        update_empty_fields(move)
        
    if move==7:
        board[2][0]='X'
        update_empty_fields(move)
        
    if move==8:
        board[2][1]='X'
        update_empty_fields(move)
        
    if move==9:
        board[2][2]='X'
        update_empty_fields(move)

    print(display_board(board))



###############MAIN########################

print(display_board(board)) #initial board display

while empty_fields != []:

    move=int(input('Please Enter a valid move'))

    if move not in empty_fields:
        print('Impossible move ')
        continue

    enter_move(move)
    if victory_for(board,'O') == True:
        print('!!!!! Congratulations you win !!!!!')
        break


    computer_move()
    if victory_for(board,'X') == True:
        print('!!!!! The computer wins, good try!!!!!')
        break

    if empty_fields == []:
         print('Good game, this is a tie')
         break




