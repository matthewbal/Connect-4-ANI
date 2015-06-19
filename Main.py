"""
A simple AI program to learn the minmax approach to AI for simple games.
Allows for AI vs AI where you can spectate matches.
Also allows for human vs AI for debugging.

Author: Matthew Balshaw
Begin Date: 20/6/2015
Last Update: ^^
"""
from __future__ import division
from random import randint
from nextToAI import NextToAI
from firstRatingAI import FirstRatingAI

playermove = 1
steps = 0
Wins1 = 0
Wins2 = 0
draws = 0


def CreateBoard():

    # 0 indicates no piece there
    # 1 indicates player 1 piece
    # 2 indicates player 2 piece
    board = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]
    return board

def DisplayBoard(board):

    
    for row in board:
        for col in row:
            if col == 0:
                print "X",
            if col == 1:
                print "1",
            if col == 2:
                print "2",
        print " "

    for x in range(0, 7):
        print "-",
    print""
        
    for x in range(0, 7):
        print x+1,
    print ""


def MakeMoveWithHumanPlayer(board):
    global playermove
    global steps
    global Wins1
    global Wins2
    global draws
    
    steps += 1
    DisplayBoard(board)
    if playermove == 1:
        pos = int(raw_input("Position to play? (1-7)\n"))
    elif playermove == 2:
        #pos = RandomAI(board)
        pos = FirstRatingAI(board, playermove)
        #pos = int(raw_input("Position to play? (1-7)\n"))

    board = DeterminePosToPlace(pos, board)

    if playermove == 1:
        playermove = 2
    else:
        playermove = 1
        
    isWinner = CheckForWinner(board)

    if isWinner == 0:
        MakeMoveWithHumanPlayer(board)
    elif isWinner == 1:
        print "Player one wins!\n"
        print "Moves:", steps, "\n"
        Wins1 += 1        
        print "\n\n"
    elif isWinner == 2:
        print "Player two wins!\n"
        print "Moves:", steps, "\n"
        Wins2 += 1
        print "\n\n"
    else:
        draws += 1

def MakeMoveAIOnly(board):
    global playermove
    global steps
    global Wins1
    global Wins2
    global draws
    
    steps += 1
    if playermove == 1:
        pos = RandomAI(board)
    elif playermove == 2:
        pos = FirstRatingAI(board, playermove)

    board = DeterminePosToPlace(pos, board)

    if playermove == 1:
        playermove = 2
    else:
        playermove = 1
        
    isWinner = CheckForWinner(board)

    if isWinner == 0:
        MakeMoveAIOnly(board)
    elif isWinner == 1:
        Wins1 += 1        
    elif isWinner == 2:
        Wins2 += 1
    else:
        draws += 1


def DeterminePosToPlace(pos, board):
    global playermove

    if not ValidMove(pos, board):
        print "Invalid Move Attempt by player", playermove
        return board
    
    for row in range(5,-1,-1):
        if board[row][pos-1] == 0:
            if playermove == 1:
                board[row][pos-1] = 1
            else:
                board[row][pos-1] = 2
            return board

def ValidMove(pos, board):
    #eliminate impossible numbers
    if pos-1 > 6:
        return False
    elif pos-1 < 0:
        return False
    
    #check if there is a place on the top row for the position

    if board[0][pos-1] == 0:
        return True
    else:
        return False
        
def CheckForWinner(board):
    global playermove

    checking = 0
    for row in range(0,6):
        for col in range(0,7):
            if board[row][col] == 1:
                checking = 1
            elif board[row][col] == 2:
                checking = 2

            if checking == 1 or checking == 2:
                #Here we are about to see if there are 4 same pieces in a row
                if board[row][col] == checking:
                    for yCheck in range(-1,2): #Generate y values
                        for xCheck in range(-1,2): #generate x values
                            if (xCheck != 0 or yCheck != 0): #Discount checking same position
                                rowCheck = row + yCheck
                                colCheck = col + xCheck
                                if rowCheck > -1 and rowCheck < 6 and colCheck > -1 and colCheck < 7: #Stop if at bounds
                                    if board[rowCheck][colCheck] == checking: #Two adjacent same piece!
                                        rowCheck += yCheck
                                        colCheck += xCheck
                                        if rowCheck > -1 and rowCheck < 6 and colCheck > -1 and colCheck < 7:#Stop if at bounds
                                            if board[rowCheck][colCheck] == checking: #Three adjacent same piece in a line!
                                                    rowCheck += yCheck
                                                    colCheck += xCheck
                                                    if rowCheck > -1 and rowCheck < 6 and colCheck > -1 and colCheck < 7:#Stop if at bounds
                                                        if board[rowCheck][colCheck] == checking: #four adjacent same pieces! Winner!
                                                            #print "detected a", board[rowCheck][colCheck], "at pos Y:", rowCheck, "X:", colCheck
                                                            #print  "Began at Y:", row, "X:", col
                                                            return checking
    #need to check for a draw!
    draw = True
    for row in range(0,6):
        for col in range(0,7):
            if board[row][col] == 0:
                draw = False
    if draw:
        return 3
    
    return 0 #no win or draw
    
def RandomAI(board):
    while True:
        pos = randint(1,7)
        if ValidMove(pos, board):
            return pos

def RunCompetition(points, rounds):
    global Wins1
    global Wins2
    winRatio = [0]
    roundCount = rounds


    while roundCount > 0:
        while Wins1 < points and Wins2 < points:
            MakeMoveAIOnly(CreateBoard())

        winRatio.append(Wins2/Wins1)
        roundCount -= 1
        Wins1 = 0
        Wins2 = 0
        
    print "The second AI won", sum(winRatio) / len(winRatio), "times more than the first"
    print "This was the first to", points, "wins and was run", rounds, "times"
    
            
if __name__ == "__main__":

    RunCompetition(100,10)

    #MakeMoveWithHumanPlayer(CreateBoard())
























