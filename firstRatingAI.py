"""
This file is the brains for the FirstRatingAI for connect four.
When given its number and the current board, it will output its desired move

This AI will attempt to select the best move by determining which location has the highest value.
the formula for value:

(creates 4 in a row) = 999999
(creates 3 in a row) = 99
(creates 2 in a row) = 1

Summation of these is the value of any one position.

Only valid moves will be selected.


Author: Matthew Balshaw
"""

from __future__ import division
from random import randint
from copy import deepcopy

def FirstRatingAI(board, playerNum):

    #for each position.
    #place the move in that position
    #see if any pairs in a row
    #see if any three's in a row
    #see if any four's in a row
    #add value to that position and store in rating matrix
    #pick the highest rating and return that.
    #if tied, select the first one
    
    ratingMatrix = [0,0,0,0,0,0,0]
    twoNodeValue = 1
    threeNodeValue = 100
    fourNodeValue = 10000


    
    for pos in range(0,7):
        if ValidMove(pos, board):
            hypoBoard = deepcopy(board)
            foundPosition = False
            
            for row in range(5,-1,-1):
                if hypoBoard[row][pos] == 0 and not foundPosition:
                    foundPosition = True
                    if playerNum == 1:
                        hypoBoard[row][pos] = 1
                    else:
                        hypoBoard[row][pos] = 2

                    if hypoBoard[row][pos] == playerNum:

                        #test for causing an adjacent node
                        for yCheck in range(-1,2): #Generate y values
                            for xCheck in range(-1,2): #generate x values
                                if (xCheck != 0 or yCheck != 0): #Discount checking same position
                                    rowCheck = row + yCheck
                                    colCheck = pos + xCheck
                                    if rowCheck > -1 and rowCheck < 6 and colCheck > -1 and colCheck < 7: #Stop if at bounds
                                        if hypoBoard[rowCheck][colCheck] == playerNum: #Two adjacent same piece!
                                            ratingMatrix[pos] += twoNodeValue
                                            rowCheck += yCheck
                                            colCheck += xCheck
                                            if rowCheck > -1 and rowCheck < 6 and colCheck > -1 and colCheck < 7:#Stop if at bounds
                                                if hypoBoard[rowCheck][colCheck] == playerNum: #Three adjacent same piece in a line!
                                                    ratingMatrix[pos] += threeNodeValue
                                                    rowCheck += yCheck
                                                    colCheck += xCheck
                                                    if rowCheck > -1 and rowCheck < 6 and colCheck > -1 and colCheck < 7:#Stop if at bounds
                                                        if hypoBoard[rowCheck][colCheck] == playerNum: #four adjacent same pieces! Winner!
                                                            ratingMatrix[pos] += fourNodeValue
                                                            #print "found a way to win!"
        
    bestPos = 0
    bestPosValue = -10000
    for pos in range(0,7):
        if not ValidMove(pos, board):
            ratingMatrix[pos] -= 10000
            
        if ratingMatrix[pos] > bestPosValue:
            bestPos = pos
            bestPosValue = ratingMatrix[pos]
            
    #print "The rating of different positions", ratingMatrix

    if not ValidMove(bestPos+1, board): #Fallback if the AI really fucks something up. Should only happen once in a while!
        print "meh"
        while True:
            pos = randint(1,7)
            if ValidMove(pos, board):
                return pos
    
    return bestPos+1


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


