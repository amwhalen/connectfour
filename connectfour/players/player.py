from connectfour.board import Board

# base class for players to extend
class Player():

    def getName(self):
        return ""

    def isHuman(self):
        return False

    def getMove(self, board, player):
        """
        Returns the index of the column (0-indexed) of which this player wants to place his token
        """
        return 0