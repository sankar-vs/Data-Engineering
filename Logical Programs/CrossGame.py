'''
@Author: Sankar
@Date: 2021-04-01 15:35:20
@Last Modified by: Sankar
@Last Modified time: 2021-04-01 19:16:38
@Title : CrossGame
'''
import random
import sys

def test_index_position(x):
    while True:
        try:
            if (int(x) >= 0 and int(x) <3):
                return int(x)
            else:
                print("Enter Proper Position")
                break    
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            break

def check_status(board, element):
    '''
    Description:
        This method checks the conditions for winning the game 
        [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)] Diagonal Winning Condition
        [(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)] Horizontal Winning Condition
        [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)] Vertical Winning Condition
        If the conditions are true it returns the respected element 'X or 'O' else 3
    Parameter:
        board (list[][]): Character elements
        element (str): 'X' or 'O'
    Return:
        element (str): 'X' or 'O' if winning conditions are true
        3 (int): returns integer value 3 if  winning conditions are false
    '''
    for i in range(3):
        if ((board[i][0] == element and board[i][1] == element and board[i][2] == element) or 
                (board[0][i] == element and board[1][i] == element and board[2][i] == element)):
            return element
    if ((board[0][0] == element and board[1][1] == element and board[2][2] == element) or
            (board[0][2] == element and board[1][1] == element and board[2][0] == element)):
        return element
    return 3

def display_board(board, count):
    '''
    Description:
        This method prints the cross game board
        prints the total number of counts of plays
        |   |   |   |
        -------------   
        |   |   |   |
        ------------- 
        |   |   |   | 
    Parameter:
        board (list[][]): Character elements
        count (int): number of plays in the cross game
    Return:
        None
    '''
    print()
    for i in range(3):
        if ( i != 0):
            print("-------------")
        print("| ", end = "")
        for j in range(3):
            print(board[i][j], end = " | ")
        print()
    print(count)        

def player_play(element, board):
    '''
    Description:
        This method gets the row and column form the user for which position
        the user would like to play the move.
        |(0,0)|(0,1)|(0,2)|
        -------------------  
        |(1,0)|(1,1)|(1,2)|
        ------------------- 
        |(2,0)|(2,1)|(2,2)| 
    Parameter:
        board (list[][]): Character elements
        element (str): 'X' or 'O'
    Return:
        board (list[][]): After the player has played his move
    '''
    while True:
        try:
            print("Enter player2 position to play: ")
            row = test_index_position(input("Enter row(0-2): "))
            column = test_index_position(input("Enter column(0-2): "))
            if (board[row][column] == ' '):
                board[row][column] = element
                break
            else:
                print("The field is not empty Please five a new position")
        except TypeError:
            print("Please check the inputs to row and column")
    return board

def computer_play(element, board):
    '''
    Description:
        This method generates the row and column from using random function.
        It checks for if not empty and calls itself recursively
        |(0,0)|(0,1)|(0,2)|
        -------------------  
        |(1,0)|(1,1)|(1,2)|
        ------------------- 
        |(2,0)|(2,1)|(2,2)| 
    Parameter:
        board (list[][]): Character elements
        element (str): 'X' or 'O'
    Return:
        board (list[][]): After the computer has played its move
    '''
    row = random.randint(0,2)
    column = random.randint(0,2)
    if (board[row][column] != " "):
        computer_play(element, board)
    if (board[row][column] == " "):
        board[row][column] = element
    return board

def print_winOrDraw(board, element, count):
    '''
    Description:
        This method checks for the winning conditions or the draw 
        and prints the status before exiting the program
    Parameter:
        board (list[][]): Character elements
        element (str): 'X' or 'O'
        count (int): number of plays in the cross game
    Return:
        None
        Exits if the Condition is met
    '''
    result = check_status(board, element)
    if (result == element):
        display_board(board, count)
        print("{} Won".format(element))
        sys.exit()
    if (result == 3 and count == 9):
        display_board(board, count)
        sys.exit("The game is a Tie")

def play_game():
    '''
    Description:
        The game is played in this method. 
        Initialisation of the boards and then starts of by user playing
        his move first then the computer plays his move.
        The game is played till anyone wins or end up in a draw
    Parameter:
        None
    Return:
        None
    '''
    count = 0
    board = [[' ' for i in range(3)] for j in range(3)]
    display_board(board, count)
    while(count < 9):
        count += 1
        board = player_play('X',board)
        display_board(board, count)
        print_winOrDraw(board, 'X', count)
        count += 1
        board = computer_play('O',board)
        display_board(board, count)
        print_winOrDraw(board, 'O', count)

play_game()