from connectfour.board import Board
from connectfour.players.player import Player
from copy import deepcopy

# uses the megamax algorithm to decide its next move
class NegamaxAlphaBetaPruningPlayer(Player):

    def __init__(self, difficulty=4, verbose=False):
        """
        Optional argument "difficulty" should be an integer of 1 or more
        """
        self.difficulty = difficulty
        self.verbose = verbose

    def getName(self):
        return "NegamaxABP(%d)" % (self.difficulty)

    def isHuman(self):
        return False

    def getMove(self, board, player):
        """
        Returns the index of the column (0-indexed) of which this player wants to place his token
        """
        moves, bestscore = self.negamax(board, player, self.difficulty, -1000, 1000)
        return moves[0]

    def negamax(self, board, player, depth, alpha, beta):

        moves = []

        # go only to the specified depth, or to the end of the game
        if depth <= 0 or board.isFull() or board.winningState() != 0:
            return moves, board.getScore(player)

        # after this move, recurse for the other player's next move
        otherPlayer = 2 if (player == 1) else 1

        # find the best of all the possible moves
        bestmove = 0
        bestscore = -1000
        for x in xrange(0, 7):
            if not board.isColumnFull(x):
                # place a token in this column
                b = deepcopy(board)
                b.placeToken(player, x)
                # get the score for the other player's next move based on this new board state
                moves, score = self.negamax(b, otherPlayer, depth-1, (0-beta), (0-alpha))
                # always invert the score we get back from the recursion
                score = 0-score
                # debug
                if self.verbose and depth == self.difficulty:
                    print "- column %d score: %d %s" % (x, score, [x] + moves)
                if score > bestscore:
                    bestscore = score
                    bestmove = x
                # alpha beta pruning
                alpha = max(alpha, score);
                if alpha >= beta:
                    break

        moves.insert(0, bestmove)

        #print ("  " * (depth-1)) + "negamax best move for player %d at depth %d: %d (score: %d)" % (player, depth, bestmove, bestscore)
        return moves, bestscore
