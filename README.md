Connect Four
============

A Connect Four game board implemented in python.

The connectfour/board.py file defines the Board class.
This class takes care of dropping tokens into the board while enforcing (most) game rules.
The board tries to keep itself from entering an invalid state, like too many tokens in one column.
A method is defined to calculate if the board contains a winning state for either player.

Here's an example string representation of the 7x6 board:
```
0 1 2 3 4 5 6
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
1 . . . . . . 
1 . . 2 . . .
```

Using the Board
---------------
```python
>>> import connectfour
>>> b = connectfour.board.Board()
>>> print(b)
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
>>> b.placeToken(b.getPlayerTurn(), 3)
True
>>> b.placeToken(b.getPlayerTurn(), 2)
True
>>> print(b)
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . 2 1 . . . 
>>> b.undo()
True
>>> print(b)
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . 1 . . . 
>>> b.reset()
>>> print(b)
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
```

Querying the State of the Game
------------------------------
```python
>>> print(b)
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . . . . . . 
. . 2 1 . . . 
>>> b.isFull()
False
>>> b.isColumnFull(3)
False
>>> b.peek(3)
1
>>> b.getPlayerTurn()
1
>>> b.getNumberOfMoves()
2
>>> b.getMoves()
[3, 2]
>>> b.getScore(1)
0
>>> b.winningState()
0
```

Playing a Game
--------------
There is a StandardGame class that uses the Board to run a standard game.
This code will play a standard game with a Human player as player 1, and an AI player using the Negamax algorithm to depth 4 as player 2.
The game can be played on the command line and will accept input from the human player.
```python
import connectfour as cf
import connectfour.players as players
import connectfour.games.standard

game = connectfour.games.standard.StandardGame(p1=players.human.HumanPlayer(), p2=players.negamax.NegamaxPlayer(4))
game.play()
```

AI Players
----------
Included are some Player classes that will choose moves based on algorithms or from user input:

**CoverPlayer**
A player that tries to cover up the other player's last move with a token. Extremely easy.

**RandomPlayer**
A player whose moves are completely random. Easy.

**NegamaxAlphaBetaPruningPlayer**
A quick but smart player that sometimes chooses speed over an optimal move. Medium to incredibly difficult.

**NegamaxPlayer**
A slow but very smart player. Medium to incredibly difficult.

**HumanPlayer**
A player with a command line interface in order to interact with a real live person.

License
-------

The MIT License (MIT)

Copyright (c) 2014 Andrew M. Whalen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.