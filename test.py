
import connectfour
import random

cf = connectfour.Board()
cf.generatePlayerTwoHorizontalWinBoard()

print cf
print "Valid:   " + str(cf.isValid())
print "Winning: " + str(cf.winningState())
print

cf.reset()
player = 1
tokenWasPlaced = True
turns = 0
while(not cf.isFull() and cf.winningState() == 0):
    column = random.randint(0, 6)
    while(cf.isColumnFull(column)):
        column = random.randint(0, 6)
    print "player " + str(player) + " col " + str(column)
    tokenWasPlaced = cf.placeToken(player, column)
    player = player % 2 + 1
    turns += 1

print cf
print "Valid:   " + str(cf.isValid())
if not cf.winningState() == 0:
    print "Player " + str(cf.winningState()) + " wins in " + str(turns) + " turns."
else:
    print "No win in " + str(turns) + " turns."
print