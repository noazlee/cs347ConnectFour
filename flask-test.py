# This is a very simple program to test that the Flask and JSON packages are correctly installed

import flask
import json
import random

app = flask.Flask(__name__)
num = 0

#new game
@app.route('/newgame/<player>')
def newGame(num):
    num += 1
    the_dictionary = {'ID': num} # ID: num 
    return json.dumps(the_dictionary)

# Read in current game state
# Decide what move to make - random number and then dont do illegal move
# Return game state

#existing game
@app.route('/nextmove/<gameID>/<oppCol>/<state>')
def nextMove(gameID, oppCol, state):
    
    s = state
    randNum = random.randint(0,6)
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



if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5127
    app.run(host=host, port=port, debug=True)
