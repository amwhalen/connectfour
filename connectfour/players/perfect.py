from connectfour.board import Board
from copy import deepcopy

class PerfectPlayer:

    def getName():
        return "Perfect"

    def __init__(self, player):
        self.open_lists = []
        self.open_lists[1] = []
        self.open_lists[2] = []
        self.closed_lists = []
        self.closed_lists[1] = []
        self.closed_lists[2] = []

        self.originalPlayer = player

    def getMove(self, board, player):
        """
        Returns the index of the column (0-indexed) of which this player wants to place his token
        """
    
    def solveBoard(self, board, player):

        # using depth first search, let's find the best move

        self.open_lists[player].append(deepcopy(board))
    
        while len(self.open_lists[player]) > 0:
    
            currentBoard = self.open_lists[player].pop()
            print "---"
            print currentBoard
        
            # if this results in a win for us, let's use this one!
            if currentBoard.winningState() == self.originalPlayer:
                break
        
            # no win for us yet, keep digging...
            self.assimilate_children(currentBoard, player)

            # this one didn't work out
            self.closed_lists[player].append(deepcopy(currentBoard))
    
        if currentBoard.winningState() == self.originalPlayer:
            # currentBoard now contains a solved game board
            # But... I just want to return the next move here, not an entire solved board!
            return currentBoard
        else:
            # couldn't find a win for this player :(
            # return something random
            return False

    def assimilate_children(self, board, player):

        temp = []

        # find each open column and generate children for it
        for col in xrange(0, 7):
            
            # check if this column is not full
            if not board.isColumnFull(col):

                # copy the board and place a token in this column
                b = deepcopy(board)
                b.placeToken(player, col)

                # add this child to the open list
                temp.append(b)

                # add the children from the temp list to the open list
                # this assures we get a correct ordering.
                # ex: if we had pushed 1 onto the open list directly, then
                # pushed 2, we'd be pulling 2 off before 1, and we wouldn't
                # be going in the correct order.
                while len(temp) > 0:
                    self.open_lists[player].append(temp.pop())

                # we were only looking for one cell, so return
                return

    def otherPlayer(self, player):
        if player == 1:
            return 2
        else:
            return 1