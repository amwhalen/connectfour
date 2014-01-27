import connectfour
import connectfour.players as players
from copy import deepcopy

class StandardGame:

    def __init__(self, p1=players.human.HumanPlayer(), p2=players.random.RandomPlayer(), verbose=True):
        """
        Constructor
        """
        self.board = connectfour.board.Board()
        self.players = { 1: p1, 2: p2 }
        self.verbose = verbose

    def printGameBoard(self):
        print 0, 1, 2, 3, 4, 5, 6
        print self.board

    def isGameOver(self):
        if self.board.isFull() or not self.board.isValid() or self.board.winningState() != 0:
            return True
        else:
            return False

    def takeTurn(self, player):
        if self.verbose:
            self.printGameBoard()
            if not self.players[player].isHuman():
                print "%s is thinking..." % self.players[player].getName()

        # make a copy so it doesn't mess with the game
        board = deepcopy(self.board)
        move = self.players[player].getMove(board, player)
        self.board.placeToken(player, move)

        if self.verbose:
            print "Player "+str(player)+" ("+self.players[player].getName()+") places in column " + str(move) + ":"

    def getWinner(self):
        if not self.board.isValid():
            return None
        else:
            return self.board.winningState()

    def getTurns(self):
        return self.board.getNumberOfMoves()

    def getMoves(self):
        return self.board.getMoves()

    def getBoard(self):
        return self.board

    def getPlayer(self, player):
        return players[player]

    def play(self):
        self.board.reset()

        while not self.isGameOver():

            self.takeTurn(1)

            # is this the end?
            if (self.isGameOver()):
                break

            self.takeTurn(2)

        if self.verbose:
            self.printGameBoard()
            if not self.board.isValid():
                print "The game board somehow became invalid! No winner!"
            else:
                if not self.board.winningState() == 0:
                    print "Player " + str(self.board.winningState()) + " ("+self.players[self.board.winningState()].getName()+") wins in " + str(self.getTurns()) + " turns."
                else:
                    print "Draw in " + str(self.getTurns()) + " turns."
                print
