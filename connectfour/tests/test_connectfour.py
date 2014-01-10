import unittest
import connectfour.board

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
        b = connectfour.board.Board()

        self.assertEquals(b.winningState(), 0)
        b.placeToken(1, 0)
        self.assertEquals(b.winningState(), 0)
        b.placeToken(2, 0)
        self.assertEquals(b.winningState(), 0)
        b.reset()

        b.generatePlayerTwoHorizontalWinBoard()
        self.assertEquals(b.winningState(), 2)
        b.reset()

        b.generatePlayerTwoVerticalWinBoard()
        self.assertEquals(b.winningState(), 2)
        b.reset()

        b.generatePlayerTwoDiagonalWinBoard()
        self.assertEquals(b.winningState(), 2)
        b.reset()

        b.generatePlayerOneHorizontalWinBoard()
        self.assertEquals(b.winningState(), 1)
        b.reset()

        b.generatePlayerOneVerticalWinBoard()
        self.assertEquals(b.winningState(), 1)
        b.reset()

        b.generatePlayerOneDiagonalWinBoard()
        self.assertEquals(b.winningState(), 1)
        b.reset()

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



if __name__ == '__main__':
    unittest.main()