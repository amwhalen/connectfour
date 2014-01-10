from connectfour.board import Board

# just tries to cover up the other player's tokens
class CoverPlayer():

    def getName(self):
        return "Cover"

    def isHuman(self):
        return False

    def getMove(self, board, player):
        """
        Returns the index of the column (0-indexed) of which this player wants to place his token
        """

        otherPlayer = 1 if (player == 2) else 2

        # try to cover the other player's tokens
        for col in xrange(0, 7):
            if board.peek(col) == otherPlayer and not board.isColumnFull(col):
                return col
        
        # didn't find anywhere to cover the other player...
        # this should only happen when we're going first and the board is empty
        # OR the other player last placed on top of a full column
        # so just find an open space:
        for col in xrange(0, 7):
            if not board.isColumnFull(col):
                return col