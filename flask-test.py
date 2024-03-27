# This is a very simple program to test that the Flask and JSON packages are correctly installed

import flask
import json
import random

app = flask.Flask(__name__)

#New game
@app.route('/newgame/<player>')
def newGame(player):
    the_dictionary = {'ID': '2387'} # ID: num
    return flask.jsonify(the_dictionary)


#Next Move
@app.route('/nextmove/<gameID>/<oppCol>/<state>')
def nextMove(gameID, oppCol, state):
    
    #Read in state
    gameID = int(gameID)
    oppCol = int(oppCol)
    player = state.split('#')[0]
    board = state.split('#')[1]
    
    #Decide next move (currently random column)
    randNum = random.randint(0,6)
    success = False
    currentPos = randNum
    numIterations = 0
    while not success and numIterations < 7:
        if currentPos > 41:
            numIterations += 1
            randNum += 1
            currentPos = randNum
            if currentPos > 6:
                currentPos = 0

        if board[currentPos] != "-":
            currentPos += 7
        else:
            success = True
            board = board[:currentPos] + player + board[currentPos + 1:]

    if success == False:
        print("No legal moves available")

    #Return new board state
    return flask.jsonify({'ID': gameID, 'Col': randNum, 'State': board})



if __name__ == '__main__':
    host = 'localhost'
    port = 5127
    app.run(host=host, port=port, debug=True)
