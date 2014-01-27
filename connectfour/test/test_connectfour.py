import unittest
import connectfour.board
import connectfour.board_factory
from copy import deepcopy

class TestBoard(unittest.TestCase):

    def setUp(self):
        pass

    def test_turn(self):
        b = connectfour.board.Board()
        
        # p2 can't place token first
        with self.assertRaises(connectfour.exceptions.OutOfTurnError):
            b.placeToken(2, 0)

        # p1 can go though
        self.assertTrue(b.placeToken(1, 0))

        # now p2 can go
        self.assertTrue(b.placeToken(2, 0))

        # but p2 can't go again
        with self.assertRaises(connectfour.exceptions.OutOfTurnError):
            b.placeToken(2, 0)

        self.assertTrue(b.isValid())

    def test_player(self):
        b = connectfour.board.Board()

        # 3 is not a valid player
        with self.assertRaises(connectfour.exceptions.InvalidPlayerError):
            b.placeToken(3, 0)

    def test_columns(self):
        b = connectfour.board.Board()

        # bad column
        with self.assertRaises(connectfour.exceptions.InvalidColumnError):
            b.placeToken(1, -1)

        # bad column
        with self.assertRaises(connectfour.exceptions.InvalidColumnError):
            b.placeToken(1, 7)

    def test_full_col(self):
        b = connectfour.board.Board()
        self.assertFalse(b.isColumnFull(0))
        self.assertTrue(b.placeToken(1, 0))
        self.assertTrue(b.placeToken(2, 0))
        self.assertTrue(b.placeToken(1, 0))
        self.assertTrue(b.placeToken(2, 0))
        self.assertTrue(b.placeToken(1, 0))
        self.assertTrue(b.placeToken(2, 0))
        # full
        with self.assertRaises(connectfour.exceptions.FullColumnError):
            b.placeToken(1, 0)
        self.assertTrue(b.isColumnFull(0))
        self.assertTrue(b.isValid())

    def test_full(self):
        b = connectfour.board.Board()
        self.assertFalse(b.isFull())
        # fill it up
        for col in xrange(0, 7):
            for y in xrange(0, 3):
                for p in [1, 2]:
                    b.placeToken(p, col)
        self.assertTrue(b.isFull())
        self.assertTrue(b.isValid())

    def test_reset(self):
        b = connectfour.board.Board()
        # fill it up
        for col in xrange(0, 7):
            for y in xrange(0, 3):
                for p in [1, 2]:
                    b.placeToken(p, col)
        b.reset()
        self.assertFalse(b.isFull())
        self.assertTrue(b.isValid())

    def test_valid(self):
        b = connectfour.board.Board()
        self.assertTrue(b.isValid())
        # fill it up
        for col in xrange(0, 7):
            for y in xrange(0, 3):
                for p in [1, 2]:
                    b.placeToken(p, col)
        self.assertTrue(b.isValid())

    def test_wins(self):

        bf = connectfour.board_factory.BoardFactory()

        b = connectfour.board.Board()
        self.assertEquals(b.winningState(), 0)
        b.placeToken(1, 0)
        self.assertEquals(b.winningState(), 0)
        b.placeToken(2, 0)
        self.assertEquals(b.winningState(), 0)
        b.reset()

        b = bf.generatePlayerTwoHorizontalWinBoard()
        self.assertEquals(b.winningState(), 2)

        b = bf.generatePlayerTwoVerticalWinBoard()
        self.assertEquals(b.winningState(), 2)

        b = bf.generatePlayerTwoDiagonalWinBoard()
        self.assertEquals(b.winningState(), 2)

        b = bf.generatePlayerOneHorizontalWinBoard()
        self.assertEquals(b.winningState(), 1)

        b = bf.generatePlayerOneVerticalWinBoard()
        self.assertEquals(b.winningState(), 1)

        b = bf.generatePlayerOneDiagonalWinBoard()
        self.assertEquals(b.winningState(), 1)

    def test_peek(self):
        b = connectfour.board.Board()

        self.assertEquals(b.peek(0), 0)
        self.assertEquals(b.peek(1), 0)
        self.assertEquals(b.peek(2), 0)
        self.assertEquals(b.peek(3), 0)
        self.assertEquals(b.peek(4), 0)
        self.assertEquals(b.peek(5), 0)
        self.assertEquals(b.peek(6), 0)

        b.placeToken(1, 0)
        self.assertEquals(b.peek(0), 1)

        b.placeToken(2, 0)
        self.assertEquals(b.peek(0), 2)

    def test_undo(self):
        b = connectfour.board.Board()
        # nothing to undo yet
        self.assertFalse(b.undo())
        # add some tokens
        self.assertEquals(b.getPlayerTurn(), 1)
        b.placeToken(1, 0)
        self.assertEquals(b.getPlayerTurn(), 2)
        b.placeToken(2, 0)
        self.assertEquals(b.getPlayerTurn(), 1)
        b.placeToken(1, 0)
        self.assertEquals(b.getPlayerTurn(), 2)
        self.assertEquals(b.peek(0), 1)
        self.assertEquals(b.getNumberOfMoves(), 3)
        self.assertEquals(b.getMoves(), [0, 0, 0])
        # now undo one move
        self.assertTrue(b.undo())
        self.assertEquals(b.getPlayerTurn(), 1)
        self.assertEquals(b.peek(0), 2)
        self.assertEquals(b.getNumberOfMoves(), 2)
        self.assertEquals(b.getMoves(), [0, 0])
        # and another
        self.assertTrue(b.undo())
        self.assertEquals(b.getPlayerTurn(), 2)
        self.assertEquals(b.peek(0), 1)
        self.assertEquals(b.getNumberOfMoves(), 1)
        self.assertEquals(b.getMoves(), [0])
        # another
        self.assertTrue(b.undo())
        self.assertEquals(b.getPlayerTurn(), 1)
        self.assertEquals(b.peek(0), 0)
        self.assertEquals(b.getNumberOfMoves(), 0)
        self.assertEquals(b.getMoves(), [])
        # back at the start, nothing to undo 
        self.assertFalse(b.undo())

    def test_score_segment(self):
        bf = connectfour.board_factory.BoardFactory()
        b = bf.generateBoard()

        self.assertFalse(b.scoreSegment(6, 0, 1, 1))
        self.assertEquals(b.scoreSegment(0, 0, 1, 1), [4, 0, 0])

        # p1 horizontal
        b = bf.generatePlayerOneHorizontalWinBoard()
        self.assertEquals(b.scoreSegment(3, 0, 1, 0), [0, 4, 0])
        self.assertEquals(b.scoreSegment(0, 0, 1, 0), [0, 1, 3])

        # p2 horizontal
        b = bf.generatePlayerTwoHorizontalWinBoard()
        self.assertEquals(b.scoreSegment(3, 0, 1, 0), [0, 0, 4])
        self.assertEquals(b.scoreSegment(0, 0, 1, 0), [0, 3, 1])

        # tricky scores
        self.assertEquals(b.scoreSegmentsAt(0, 0), {1: [0, 2, 0, 1, 0], 2: [2, 1, 0, 0, 0]})
        self.assertEquals(b.getCounts(), {1: [60, 7, 1, 1, 0], 2: [56, 10, 1, 1, 1]})
        self.assertEquals(b.getRawScores(), [0, 5, 1000])
        self.assertEquals(b.getScore(1), -1000)
        self.assertEquals(b.getScore(2), 1000)

        # which is the best move?
        expectedScores = [-7, -3, -6, 1000, -7, -9, -9]
        for x in xrange(0, 7):
            b = bf.generatePlayerOneDiagonalWinBoard()
            b._board[3][3] = 0
            b.placeToken(1, x)
            #print "column %d: %d" % (x, b.getScore(1))
            #print b
            self.assertEquals(b.getScore(1), expectedScores[x])

    def test_score(self):
        # 0 1 2 3 4 5 6
        # . . . . . . . 
        # . . . . . . . 
        # . . . . . . . 
        # 1 . . . . . . 
        # 1 . . . . . . 
        # 1 . 2 2 . . .
        #
        # should result in a score of 2 for player 1
        #
        bf = connectfour.board_factory.BoardFactory()
        b = bf.generatePlayerOneNextMoveWins()
        self.assertEquals(b.getRawScores(), [0, 5, 3])
        self.assertEquals(b.getScore(1), 2)
        self.assertEquals(b.getScore(2), -2)
        # player 2 doesn't go for the obvious block
        b.placeToken(2, 4)
        self.assertEquals(b.getRawScores(), [0, 5, 10])
        self.assertEquals(b.getScore(1), -5)
        self.assertEquals(b.getScore(2), 5)
        # now player 1 should win, and player 2 loses
        b.placeToken(1, 0)
        self.assertEquals(b.getRawScores(), [0, 1000, 10])
        self.assertEquals(b.getScore(1), 1000)
        self.assertEquals(b.getScore(2), -1000)

        # make sure this board is not considered full
        # 0 1 2 3 4 5 6
        # . 1 2 1 1 2 . 
        # . 2 2 1 1 1 . 
        # . 1 1 1 2 2 . 
        # 1 2 2 2 1 2 . 
        # 2 1 2 1 2 1 1 
        # 2 1 2 1 1 2 2


if __name__ == '__main__':
    unittest.main()