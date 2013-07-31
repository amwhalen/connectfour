Connect Four
============

A Connect Four game board implemented in python.

The connectfour/board.py file defines the Board class.
This class takes care of dropping tokens into the board while enforcing (most) game rules.
The board tries to keep itself from entering an invalid state, like too many tokens in one column.
A method is defined to calculate if the board contains a winning state for either player.

The play.py file runs many simulated games and prints the results.