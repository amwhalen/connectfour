import exceptions as errors

#
# Connect Four
#
# 7x6 Game Board
#
# 5 . . . . . . .
# 4 . . . . . . .
# 3 . . . . . . .
# 2 . . . . . . .
# 1 . . . . . . .
# 0 . . . . . . .
#   0 1 2 3 4 5 6
#

# http://en.wikipedia.org/wiki/Connect_Four
# https://en.wikipedia.org/wiki/Solved_game
# The game was solved mathematically by James D. Allen (October 1, 1988), and independently by Victor Allis (October 16, 1988).
# With perfect play, the first player can force a win by starting in the middle column.
# By starting in the two adjacent columns, the first player allows the second player to reach a draw;
# by starting with the four outer columns, the first player allows the second player to force a win.

# winning segments (39 total):
#
# horizontal segments (15):
# 0-3, 1-5, 2-6
#
# vertical segments (12):
# 0-3, 1-5
#
# diagonal segments (12):
# 0,2->3,5
# 0,1->3,4
# 1,2->4,5
# 0,0->3,3
# 1,1->4,4
# 2,2->5,5
# 1,0->4,3
# 2,1->5,4
# 3,2->6,5
# 2,0->5,3
# 3,1->6,4
# 3,0->6,3

class Board:

    def __init__(self):
        """
        Constructor
        """
        self.reset()

    def placeToken(self, player, column):
        """
        Places a player's token in the specified column
        """
        if player != 1 and player != 2:
            raise errors.InvalidPlayerError('Invalid player.')
        if player != self.playerTurn:
            raise errors.OutOfTurnError('Not your turn.')
        if column < 0 or column > 6:
            raise errors.InvalidColumnError('Invalid column.')
        # attempt to drop the token in
        for y in xrange(0, 6):
            if self._board[column][y] == 0:
                self._board[column][y] = player
                self.moves.append(column)
                self.playerTurn = 2 if (self.playerTurn == 1) else 1
                return True
        # the column is full!
        raise errors.FullColumnError('Column is full.')

    def undo(self):
        """
        Undo operation for the last move
        """
        if len(self.moves) == 0:
            return False
        lastMove = self.moves[-1]
        # look at this column from top to bottom
        for y in xrange(5, -1, -1):
            if self._board[lastMove][y] == 0:
                # ignore
                continue
            else:
                # remove the token
                self._board[lastMove][y] = 0
                break
        self.moves.pop()
        self.playerTurn = 2 if (self.playerTurn == 1) else 1
        return True

    def isColumnFull(self, col):
        """
        Returns True if the given column is full
        """
        for y in xrange(0, 6):
            if self._board[col][y] == 0:
                return False
        return True

    def isFull(self):
        """
        Returns True if the board is full
        """
        for x in xrange(0, 7):
            if not self.isColumnFull(x):
                return False
        return True

    def peek(self, col):
        """
        Returns the token value at the top of the given column
        """
        if col < 0 or col > 6:
            raise errors.InvalidColumnError('Invalid column.')
        # look at this column from top to bottom
        for y in xrange(5, -1, -1):
            cell = self._board[col][y]
            if cell != 0:
                return cell
        return 0

    def getMoves(self):
        """
        Returns a list of the moves taken in this game.
        """
        return self.moves

    def getNumberOfMoves(self):
        """
        Returns the total number of moves taken in this game so far
        """
        return len(self.moves)

    def getPlayerTurn(self):
        """
        Returns the number (1,2) of the player whose turn it is
        """
        return self.playerTurn

    def __str__(self):
        """
        Return the board as a string
        """
        boardStr = ''
        for y in xrange(5, -1, -1):
            rowString = ''
            for x in xrange(0, 7):
                cell = self._board[x][y]
                if cell != 0:
                    cStr = str(cell)
                else:
                    cStr = '.'
                rowString += cStr + " "
            boardStr += rowString
            if y > 0:
                boardStr += "\n"
        return boardStr

    def reset(self):
        """
        Sets up the empty game board
        """
        self._board = []
        self.playerTurn = 1
        self.moves = []
        for x in xrange(0, 7):
            col = []
            for y in xrange(0, 6):
                col.append(0)
            self._board.append(col)

    def isValid(self):
        """
        Returns True if the board is in a valid state
        """
        # if there are tokens in a column, they must obey "gravity"
        # look at each column from left to right
        tokens = {1: 0, 2: 0}
        for x in xrange(0, 7):
            columnHasTokens = False
            # look at this column from top to bottom
            for y in xrange(5, -1, -1):
                cell = self._board[x][y]
                if cell != 0:
                    tokens[cell] += 1
                if columnHasTokens:
                    if cell == 0:
                        # no gaps once a token has been found!
                        return False
                else:
                    if cell != 0:
                        # found first token in this column
                        columnHasTokens = True
        # at this point we know the columns obey gravity
        # now check that token counts are valid
        if self.isFull():
            # if full, p1 and p2 should have equal numbers of tokens
            return tokens[1] == tokens[2]
        else:
            # if not full, p1 and p2 should have equal or +/-1 tokens
            return (tokens[1] - tokens[2]) in [0, 1, -1]

    def winningState(self):
        """
        Returns 0 if the board is not in a winning state
        Returns 1 if Player 1 is in a winning state
        Returns 2 if Player 2 is in a winning state
        """
        if not self.isValid():
            raise errors.InvalidBoardError('Board is not valid.')
        for x in xrange(0, 7):
            for y in xrange(0, 6):
                if self.__isLineStartingAt(x, y):
                    return self._board[x][y]
        return 0

    def __isLineStartingAt(self, x, y):
        """
        Private
        Returns True if the given board coordinates lead to 4 contiguous tokens from the same player
        http://stackoverflow.com/questions/4636575/win-conditions-for-a-connect-4-like-game
        """
        # horizontal || vertical || diagonal down || diagonal up
        return self.__isLinearMatch(x, y, 1,  0) or self.__isLinearMatch(x, y, 0,  1) or self.__isLinearMatch(x, y, 1,  1) or self.__isLinearMatch(x, y, 1, -1)

    def __isLinearMatch(self, x, y, stepX, stepY):
        """
        Private
        Returns True if the given board coordinates lead to 4 contiguous tokens from the same player in the direction specified by stepX and stepY
        """
        # get value at start position
        cell = self._board[x][y]

        # can't have a win if the starting cell is empty!
        if cell == 0:
            return False

        # look for 4 identical values in a row
        for i in xrange(0, 4):
            cX = x + i * stepX
            cY = y + i * stepY
            if len(self._board) > cX and len(self._board[cX]) > cY:
                if self._board[cX][cY] != cell:
                    return False
            else:
                return False
        # if we get here, then they all match
        return True

    def getScore(self, player):
        """
        Returns the current score relative to the given player
        """
        scores = self.getRawScores()

        # make sure a win or a loss has a bigger impact than other scores
        if scores[1] == 1000 or scores[2] == 1000:
            if scores[player] == 1000:
                return 1000
            else:
                return -1000

        # score depends on the player
        if player == 1:
            return scores[1] - scores[2]
        else:
            return scores[2] - scores[1]

    def getRawScores(self):
        """
        Determines the score for each player based on these weights:
        Tokens  Weight
        1       0
        2       1
        3       4
        4       Infinite
        """
        c = self.getCounts()

        # if there's a segment with 4, it's a win for this player
        if c[1][4] >= 1:
            p1Score = 1000
        else:
            p1Score = c[1][2] * 1 + c[1][3] * 4

        # if there's a segment with 4, it's a win for this player
        if c[2][4] >= 1:
            p2Score = 1000
        else:
            p2Score = c[2][2] * 1 + c[2][3] * 4

        return [0, p1Score, p2Score]

    def getCounts(self):
        """
        Returns a dictionary of segment counts as such:
        Tokens  P1  P2
        0       60  56 
        1        7  10
        2        1   1
        3        1   1
        4        0   1
        """
        counts = {1: [0, 0, 0, 0, 0], 2: [0, 0, 0, 0, 0]}
        if not self.isValid():
            raise errors.InvalidBoardError('Board is not valid.')
        for x in xrange(0, 7):
            for y in xrange(0, 6):
                segmentCounts = self.scoreSegmentsAt(x, y)
                for i in xrange(0, 5):
                    counts[1][i] += segmentCounts[1][i]
                    counts[2][i] += segmentCounts[2][i]
        return counts

    def scoreSegmentsAt(self, x, y):
        """
        Returns a dictionary of segment counts for each player at the given coordinates
        """
        # horizontal + vertical + diagonal up + diagonal down
        hor = self.scoreSegment(x, y, 1, 0)
        ver = self.scoreSegment(x, y, 0, 1)
        dup = self.scoreSegment(x, y, 1, 1)
        ddn = self.scoreSegment(x, y, 1, -1)

        counts = {1: [0, 0, 0, 0, 0], 2: [0, 0, 0, 0, 0]}
        if hor != False:
            counts[1][hor[1]] += 1
            counts[2][hor[2]] += 1
        if ver != False:
            counts[1][ver[1]] += 1
            counts[2][ver[2]] += 1
        if dup != False:
            counts[1][dup[1]] += 1
            counts[2][dup[2]] += 1
        if ddn != False:
            counts[1][ddn[1]] += 1
            counts[2][ddn[2]] += 1

        return counts

    def scoreSegment(self, x, y, stepX, stepY):
        """
        Returns a list containing the counts of each player's tokens in this segment, or False if it's not a 4-segment
        """
        counts = [0, 0, 0]
        # iterate over 3 more cells
        for i in xrange(0, 4):
            cX = x + i * stepX
            cY = y + i * stepY
            # are these coordinates OK?
            if len(self._board) > cX and 0 <= cX and len(self._board[cX]) > cY and 0 <= cY:
                # give a point to the player with this cell
                counts[self._board[cX][cY]] += 1
            else:
                return False
        #print "segment: %d,%d -> %d,%d" % (x, y, cX, cY)
        return counts
