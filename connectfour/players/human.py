import connectfour

# gets input from a human
class HumanPlayer():

    def getName(self):
        return "Human"

    def isHuman(self):
        return True

    def getMove(self, board, player):
        """
        Returns the index of the column (0-indexed) of which this player wants to place his token
        """

        while True:
            try:
                humanMove = self.getMoveInput(player)
                board.placeToken(player, humanMove)
                break
            except Exception as e:
                print e
        return humanMove

    def getMoveInput(self, player):
        while True:
            try:
                yourMove = int(raw_input("Player "+str(player)+", enter your move (0-6): "))
                return yourMove
            except ValueError:
                print "That's not a number. Try again."