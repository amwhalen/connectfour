
import connectfour
import random


def playLotsOfGames(numGames):
    playerOneWins = 0
    playerTwoWins = 0
    draws = 0
    averageTurns = 0
    totalTurns = 0
    board = connectfour.Board()
    # play the specified number of games
    for x in xrange(0, numGames):
        board.reset()
        player = 1
        tokenWasPlaced = True
        turns = 0
        while(not board.isBoardFull() and board.winningState() == 0):
            column = random.randint(0, 6)
            while(board.isColumnFull(column)):
                column = random.randint(0, 6)
            tokenWasPlaced = board.placeToken(player, column)
            player = player % 2 + 1
            turns += 1

        # who won?
        winningPlayer = board.winningState()
        if winningPlayer == 1:
            playerOneWins += 1
        elif winningPlayer == 2:
            playerTwoWins += 1
        else:
            draws += 1

        # compute average turns
        totalTurns += turns
        averageTurns = totalTurns / (x + 1)

    print "Games Played:  " + str(numGames)
    print "Draws:         " + str(draws)
    print "Player 1 Wins: " + str(playerOneWins)
    print "Player 2 Wins: " + str(playerTwoWins)
    print "Average Turns: " + str(averageTurns)

playLotsOfGames(1000)
