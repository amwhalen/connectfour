from __future__ import absolute_import
import connectfour
import random

class RandomPlayer:

    def getName(self):
        return "Random"

    def isHuman(self):
        return False

    def getMove(self, board, player):
        """
        Returns the index of the column (0-indexed) of which this player wants to place his token
        """

        # try random columns
        while True:
            column = random.randint(0, 6)
            try:
                if board.placeToken(player, column):
                    return column
            except connectfour.exceptions.FullColumnError:
                pass
            except Exception as e:
                raise e