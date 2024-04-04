'''Connect 4 API implementation: Alex Wcislo, Carlos Flores, Valentina Guerrero'''
# ai2

import flask
import random
import json
import time

app = flask.Flask(__name__)

# Dictionary of all current games(gameIDs are keys) and boards(list of board string and the next player is the value)
# Our boards are build left to right, upwards. Meaning the bottom left of a connect 4 board is represented by the first character in the board string, and the top right is the last character.
allBoards = {}

# Update the board in allBoards with the last move from the opponent. Return false if not possible (index out of range)


# def addLastMove(opponentMove, gameID, board):
#     currPlayer = allBoards[gameID][1]
#     boardList = list(board)
#     targetIndex = opponentMove - 1
#     while targetIndex < 42:
#         if boardList[targetIndex] == "-":
#             boardList[targetIndex] = currPlayer
#             # Convert the list back to a string before returning
#             return ''.join(boardList)
#         else:
#             targetIndex += 7
#     return False

# AI moves their piece to the next available spot, iterating through the board from left to right
def replacer(s, index, newstring):
    return s[:index] + newstring + s[index+1:]


def makeNextMove(player, board):
    # Create a list of strings for each column
    columns = [board[i::7] for i in range(7)]
    validMoveMade = False
    nextMove = None

    for col in range(7):
        for row in reversed(range(6)):
            if columns[col][row] == "-":
                index = row * 7 + col
                board = board[:index] + player + \
                    board[index + 1:]
                validMoveMade = True
                nextMove = col
                break
        if validMoveMade:
            break

    if not validMoveMade:
        return None, board

    return nextMove, board

# Initiates a new connect 4 game with the player being X or O


@app.route('/newgame/<player>')
def newgame(player):
    gameId = int(time.time())
    # state = [player, "------------------------------------------"]
    # allBoards[gameId] = state
    response = {'ID': gameId}
    return json.dumps(response)


@app.route('/nextmove/<gameID>/<oppCol>/<state>')
def nextmove(gameID, oppCol, state):
    gameID = int(gameID)
    oppCol = int(oppCol)

    player, board = state.split('#')

    # if gameID not in allBoards:
    #     response = {"Error": "gameID not Found"}
    #     return json.dumps(response)

    # updatedBoard = addLastMove(oppCol, gameID, board)

    # if updatedBoard == False:
    #     response = {"Error": "Board is not valid"}
    #     return json.dumps(response)

    nextMove, currBoard = makeNextMove(player, board)
    # nextPlayer = allBoards[gameID][0]

    # Update global variable allBoards
    # allBoards[gameID][1] = ''.join(currBoard)

    if player == 'X':
        nextPlayer = 'O'
    else:
        nextPlayer = 'X'

    # allBoards[gameID][0] = nextPlayer
    state = nextPlayer + '#' + currBoard
    response = {'ID': gameID, 'col': nextMove, 'state': state}

    return json.dumps(response)


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port, debug=True)
