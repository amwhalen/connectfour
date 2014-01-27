import connectfour.board

class BoardFactory:

    def generateBoard(self):
        return connectfour.board.Board()

    def generatePlayerOneNextMoveWinsColZero(self):
        """
        0 1 2 3 4 5 6
        . . . . . . . 
        . . . . . . . 
        . . . . . . . 
        1 . . . . . . 
        1 . . . . . . 
        1 . 2 2 . . .
        """
        b = connectfour.board.Board()
        b.placeToken(1, 0)
        b.placeToken(2, 3)
        b.placeToken(1, 0)
        b.placeToken(2, 2)
        b.placeToken(1, 0)
        return b

    def generatePlayerOneHasTwoInColZero(self):
        """
        0 1 2 3 4 5 6
        . . . . . . . 
        . . . . . . . 
        . . . . . . . 
        . . . . . . . 
        1 . . . . . . 
        1 . . 2 . . .
        """
        b = connectfour.board.Board()
        b.placeToken(1, 0)
        b.placeToken(2, 3)
        b.placeToken(1, 0)
        return b

    def generatePlayerOneNextMoveWinsCol6(self):
        """
        0 1 2 3 4 5 6
        . . . . . . . 
        . . . . . . . 
        . . . . . . . 
        . . . . . . 1
        . . . . . . 1 
        . . 2 2 . . 1
        """
        b = connectfour.board.Board()
        b.placeToken(1, 6)
        b.placeToken(2, 3)
        b.placeToken(1, 6)
        b.placeToken(2, 2)
        b.placeToken(1, 6)
        return b

    def generatePlayerOneHasTwoInCol6(self):
        """
        0 1 2 3 4 5 6
        . . . . . . . 
        . . . . . . . 
        . . . . . . . 
        . . . . . . .
        . . . . . . 1 
        . . . 2 . . 1
        """
        b = connectfour.board.Board()
        b.placeToken(1, 6)
        b.placeToken(2, 3)
        b.placeToken(1, 6)
        return b

    def generatePlayerTwoHorizontalWinBoard(self):
        b = connectfour.board.Board()
        b._board[0][0] = 1
        b._board[1][0] = 1
        b._board[2][0] = 1
        b._board[3][0] = 2
        b._board[4][0] = 2
        b._board[5][0] = 2
        b._board[6][0] = 2
        return b

    def generatePlayerTwoVerticalWinBoard(self):
        b = connectfour.board.Board()
        b._board[0][0] = 2
        b._board[0][1] = 2
        b._board[0][2] = 2
        b._board[0][3] = 2
        b._board[3][0] = 1
        b._board[4][0] = 1
        b._board[5][0] = 1
        return b

    def generatePlayerTwoDiagonalWinBoard(self):
        b = connectfour.board.Board()
        b._board[0][0] = 2
        b._board[1][1] = 2
        b._board[2][2] = 2
        b._board[3][3] = 2
        b._board[1][0] = 2
        b._board[2][0] = 1
        b._board[2][1] = 1
        b._board[3][0] = 1
        b._board[3][1] = 1
        b._board[3][2] = 1
        return b

    def generatePlayerOneHorizontalWinBoard(self):
        b = connectfour.board.Board()
        b._board[0][0] = 2
        b._board[1][0] = 2
        b._board[2][0] = 2
        b._board[3][0] = 1
        b._board[4][0] = 1
        b._board[5][0] = 1
        b._board[6][0] = 1
        return b

    def generatePlayerOneVerticalWinBoard(self):
        b = connectfour.board.Board()
        b._board[0][0] = 1
        b._board[0][1] = 1
        b._board[0][2] = 1
        b._board[0][3] = 1
        b._board[3][0] = 2
        b._board[4][0] = 2
        b._board[5][0] = 2
        return b

    def generatePlayerOneDiagonalWinBoard(self):
        b = connectfour.board.Board()
        b._board[0][0] = 1
        b._board[1][1] = 1
        b._board[2][2] = 1
        b._board[3][3] = 1
        b._board[1][0] = 1
        b._board[2][0] = 2
        b._board[2][1] = 2
        b._board[3][0] = 2
        b._board[3][1] = 2
        b._board[3][2] = 2
        return b
