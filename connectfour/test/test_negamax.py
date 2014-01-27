import unittest
import connectfour.board
import connectfour.board_factory
from connectfour.players.negamax import NegamaxPlayer
from copy import deepcopy

class TestBoard(unittest.TestCase):

    def setUp(self):
        pass

    def test_negamax(self):
    	n = NegamaxPlayer(4)
    	self.assertEquals(n.getName(), "Negamax(4)")
    	self.assertFalse(n.isHuman())

		# 0 1 2 3 4 5 6
		# . . . . . . . 
		# . . . . . . . 
		# . . . . . . . 
		# 1 . . . . . . 
		# 1 . . . . . . 
		# 1 . 2 2 . . .
		#
		# should result in player 2 (negamax) moving to column zero to block
		#
    	bf = connectfour.board_factory.BoardFactory()
    	b = bf.generatePlayerOneNextMoveWinsColZero()
    	self.assertEquals(n.getMove(b, 2), 0)

    	# 0 1 2 3 4 5 6
		# . . . . . . . 
		# . . . . . . . 
		# . . . . . . . 
		# . . . . . . 1 
		# . . . . . . 1 
		# . . 2 2 . . 1
		#
		# should result in player 2 (negamax) moving to column six to block
		#
    	bf = connectfour.board_factory.BoardFactory()
    	b = bf.generatePlayerOneNextMoveWinsCol6()
    	self.assertEquals(n.getMove(b, 2), 6)

        # 0 1 2 3 4 5 6
        # . . . . . . . 
        # . . . . . . . 
        # . . . . . . . 
        # . . . . . . . 
        # 1 . . . . . . 
        # 1 . 2 2 . . .
        #
        # should result in player 2 (negamax) moving to column zero
        #
        bf = connectfour.board_factory.BoardFactory()
        b = bf.generatePlayerOneHasTwoInColZero()
        self.assertEquals(n.getMove(b, 2), 0)

        # 0 1 2 3 4 5 6
        # . . . . . . . 
        # . . . . . . . 
        # . . . . . . . 
        # . . . . . . . 
        # . . . . . . 1 
        # . . 2 2 . . 1
        #
        # should result in player 2 (negamax) moving to column six
        #
        bf = connectfour.board_factory.BoardFactory()
        b = bf.generatePlayerOneHasTwoInCol6()
        self.assertEquals(n.getMove(b, 2), 6)

if __name__ == '__main__':
    unittest.main()