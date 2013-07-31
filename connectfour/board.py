
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


class Board:

    _board = []

    def __init__(self):
        """
        Constructor
        """
        self.reset

    def placeToken(self, player, column):
        """
        Places a player's token in the specified column
        """
        if player != 1 and player != 2:
            return False
        if column < 0 or column > 6:
            return False
        # attempt to drop the token in
        for y in xrange(0, 6):
            if self._board[column][y] == 0:
                self._board[column][y] = player
                return True
        # the column is full!
        return False

    def isColumnFull(self, col):
        """
        Returns True if the given column is full
        """
        for y in xrange(0, 6):
            if self._board[col][y] == 0:
                return False
        return True

    def isBoardFull(self):
        """
        Returns True if the board is full
        """
        for x in xrange(0, 6):
            if not self.isColumnFull(x):
                return False
        return True

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
            boardStr += rowString + "\n"
        return boardStr

    def reset(self):
        """
        Sets up the empty game board
        """
        self._board = []
        for x in xrange(0, 7):
            col = []
            for y in xrange(0, 6):
                col.append(0)
            self._board.append(col)

    def isValid(self):
        """
        Returns True if the board is in a valid state
        Does not check (yet) for the right number of each token color
        """
        # if there are tokens in a column, they must obey "gravity"
        # look at each column from left to right
        for x in xrange(0, 7):
            columnHasTokens = False
            # look at this column from top to bottom
            for y in xrange(5, -1, -1):
                cell = self._board[x][y]
                if columnHasTokens:
                    if cell == 0:
                        # no gaps once a token has been found!
                        return False
                else:
                    if cell != 0:
                        # found first token in this column
                        columnHasTokens = True
        return True

    def winningState(self):
        """
        Returns 0 if the board is not in a winning state
        Returns 1 if Red is in a winning state
        Returns 2 if Black is in a winning state
        """
        if not self.isValid():
            return 0
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

    def generatePlayerTwoHorizontalWinBoard(self):
        self.reset()
        self._board[0][0] = 1
        self._board[1][0] = 1
        self._board[2][0] = 1
        self._board[3][0] = 2
        self._board[4][0] = 2
        self._board[5][0] = 2
        self._board[6][0] = 2

    def generatePlayerTwoVerticalWinBoard(self):
        self.reset()
        self._board[0][0] = 2
        self._board[0][1] = 2
        self._board[0][2] = 2
        self._board[0][3] = 2
        self._board[3][0] = 1
        self._board[4][0] = 1
        self._board[5][0] = 1

    def generatePlayerTwoDiagonalWinBoard(self):
        self.reset()
        self._board[0][0] = 2
        self._board[1][1] = 2
        self._board[2][2] = 2
        self._board[3][3] = 2
        self._board[1][0] = 2
        self._board[2][0] = 1
        self._board[2][1] = 1
        self._board[3][0] = 1
        self._board[3][1] = 1
        self._board[3][2] = 1

    def generatePlayerOneHorizontalWinBoard(self):
        self.reset()
        self._board[0][0] = 2
        self._board[1][0] = 2
        self._board[2][0] = 2
        self._board[3][0] = 1
        self._board[4][0] = 1
        self._board[5][0] = 1
        self._board[6][0] = 1

    def generatePlayerOneVerticalWinBoard(self):
        self.reset()
        self._board[0][0] = 1
        self._board[0][1] = 1
        self._board[0][2] = 1
        self._board[0][3] = 1
        self._board[3][0] = 2
        self._board[4][0] = 2
        self._board[5][0] = 2

    def generatePlayerOneDiagonalWinBoard(self):
        self.reset()
        self._board[0][0] = 1
        self._board[1][1] = 1
        self._board[2][2] = 1
        self._board[3][3] = 1
        self._board[1][0] = 1
        self._board[2][0] = 1
        self._board[2][1] = 2
        self._board[3][0] = 2
        self._board[3][1] = 2
        self._board[3][2] = 2
