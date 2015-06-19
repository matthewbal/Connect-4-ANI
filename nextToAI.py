"""
This file is the brains for the NextToAI for connect four.
When given its number and the current board,
it will output its desired move

Its move checks the positions left to right to see if any position placed will be next to an already placed piece.
If it cant find a place to put it, it will select randomly.
Only valid moves will be selected.

This AI is ~4.6 times better at winning than a random selection AI

Author: Matthew Balshaw
"""

from __future__ import division
from random import randint

def NextToAI(board, playerNum):

    for pos in range(0,7):
        if ValidMove(pos, board):
            for row in range(5,-1,-1): #go up from the base to the top
                if board[row][pos] == 0: #find first value going from bottom of board up that is zero (no piece there)
                    col = pos #we would put a piece in the position selected
                    for yCheck in range(-1,2): #Generate y values
                        for xCheck in range(-1,2): #generate x values
                            if (xCheck != 0 or yCheck != 0): #Discount checking same position
                                rowCheck = row + yCheck
                                colCheck = col + xCheck
                                if rowCheck > -1 and rowCheck < 6 and colCheck > -1 and colCheck < 7: #Stop if at bounds
                                    if board[rowCheck][colCheck] == playerNum: #Two adjacent same piece!
                                        #therefore this position is the first viable one found!
                                        return pos+1
    while True:
        pos = randint(1,7)
        if ValidMove(pos, board):
            return pos


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


