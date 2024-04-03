#! /usr/bin/python
# A simple API endpoint to be used for a game of connect4
# Noah, Warren, Mary

import flask, random

app = flask.Flask(__name__)

# Store a list of existing games
existing_games = {}

# New game
@app.route('/newgame/<player>')
def newGame(player):
    waiting = True
    while waiting:
        newID = random.randint(1000, 2000)
        if newID not in existing_games:
            existing_games[newID] = player
            return flask.jsonify({
                'ID': newID
            })

# Existing game
@app.route('/nextmove/<gameID>/<oppCol>/<state>')
def nextMove(gameID, oppCol, state):

    randNum = random.randint(0,6)
    currentPos = randNum
    tries = 1

    player = state.split('#')[0]
    board = state.split('#')[1]

    success = False
    while not success:
        if currentPos + 7 > 41:
            board = board[:currentPos] + player + board[currentPos + 1:]
            success = True
            break
        elif board[currentPos + 7] == '-':
            currentPos += 7
        elif board[currentPos] != '-':
            randNum = (randNum + 1) % 7
            currentPos = randNum
            tries += 1
        else:
            board = board[:currentPos] + player + board[currentPos + 1:]
            success = True

        if tries > 7:
            return flask.jsonify({
                "error": "no_valid_move"
            })

    if player == 'X':
        player = 'O'
    else:
        player = 'X'


    return flask.jsonify({'ID': gameID, 'Col': randNum, 'State': player + "#" + board})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)
