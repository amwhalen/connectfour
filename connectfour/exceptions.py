# raised when a token is placed by the wrong player
class OutOfTurnError(Exception):
    pass

# raised if the given player is invalid
class InvalidPlayerError(Exception):
    pass

# raised if the given column is out of bounds
class InvalidColumnError(Exception):
    pass

# raised when a column is full
class FullColumnError(Exception):
    pass

# raised when the board is in an invalid state
class InvalidBoardError(Exception):
    pass