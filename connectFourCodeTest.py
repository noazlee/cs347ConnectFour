# This is a very simple program to test that the Flask and JSON packages are correctly installed

import json
import random

num = 0

egBoard = ""
for counter in range(42):
    egBoard += "-"

print(egBoard)
print(len(egBoard))


def randomBoard() -> str:
    return ""
    # new game


def newGame(num):
    num += 1
    the_dictionary = {'ID': num}  # ID: num
    return json.dumps(the_dictionary)


def nextMove(gameID, oppCol, state):

    s = state
    randNum = random.randint(0, 6)
    success = False
    currentPos = randNum

    numIterations = 0

    player = s.split('#')[0]
    board = s.split('#')[1]

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
            board[currentPos] = player

    if success == False:
        print("No legal moves available")

    return json.dumps({'ID': gameID, 'Col': randNum, 'State': board})
