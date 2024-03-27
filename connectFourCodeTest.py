# This is a very simple program to test that the Flask and JSON packages are correctly installed

import json
import random


def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring


def nextMove(player, state):

    randNum = random.randint(0, 6)
    success = False
    currentPos = randNum

    numIterations = 0

    player = player
    board = state

    while not success or numIterations < 7:
        if board[currentPos] != "-":
            currentPos += 7
            if currentPos > 42:
                numIterations += 1
                randNum += 1
                currentPos = randNum
                if currentPos > 6:
                    currentPos = 0
        else:
            success = True
            replacer(board, currentPos, player)

    return board


def randomBoard():
    egBoard = ""
    for i in range(42):
        egBoard += "-"
    numMoves = random.randint(0, 41)
    players = ["X", "O"]
    for c in range(numMoves):
        player = players[c % 2]
        egBoard = nextMove(player, egBoard)

    return egBoard

    # new game


print(randomBoard())
