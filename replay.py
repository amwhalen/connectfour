import connectfour

# replay
moves = [0, 2, 3, 4, 1, 5, 1, 3, 1, 1, 1, 3, 3, 4, 3, 5, 0, 0, 0, 2]
print "replay: %s" % (moves)
board = connectfour.board.Board()
for m in moves:
    board.placeToken(board.getPlayerTurn(), m)
    print "=============="
    print (" " * m * 2) + "v"
    print board