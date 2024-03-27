# This is a very simple program to test that the Flask and JSON packages are correctly installed

import json
import random


def replacer(s, index, newstring):
    return s[:index] + newstring + s[index+1:]


def nextMove(player, state):
    board = state

    columns = [board[i::7] for i in range(7)]  # 2D ARRAY

    success = False
    numTries = 0
    while not success or numTries > 30:
        randCol = random.randint(0, 6)  # Select a random column
        column = columns[randCol]
        # Find the first empty slot from the bottom of the column
        emptySlot = column.find('-')
        if emptySlot != -1:
            # Calculate the index in the string
            index = emptySlot * 7 + randCol
            board = replacer(board, index, player)
            success = True
        else:
            # If the selected column is full, try another one
            numTries += 1
            continue

    return board


def randomBoard():
    egBoard = "-" * 42  # Initialize an empty board
    numMoves = random.randint(0, 41)
    players = ["X", "O"]
    for i in range(numMoves):
        player = players[i % 2]
        egBoard = nextMove(player, egBoard)

    return egBoard


# new game
newBoard = randomBoard()

print(newBoard)


def layOutCorrectly(board):
    newBoard = [[] for i in range(6)]
    counter = 0
    numRows = 6
    for i in range(len(board)):
        # Fill rows from bottom to top
        newBoard[numRows - 1 - (i // 7)].append(board[i])
        counter += 1
        if counter == 7:
            counter = 0  # Reset counter after every 7 elements

    return newBoard


print(layOutCorrectly(newBoard))
