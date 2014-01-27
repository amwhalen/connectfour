import connectfour as cf
import connectfour.players as players
import connectfour.games.standard

# play a single game

#game = connectfour.games.standard.StandardGame(p1=players.human.HumanPlayer(), p2=players.negamaxabp.NegamaxAlphaBetaPruningPlayer(4, verbose=True), verbose=True)
game = connectfour.games.standard.StandardGame(p1=players.human.HumanPlayer(), p2=players.negamax.NegamaxPlayer(4, verbose=True), verbose=True)
#game = connectfour.games.standard.StandardGame(p1=players.negamax.NegamaxPlayer(4), p2=players.negamax.NegamaxPlayer(4), verbose=True)
#game = connectfour.games.standard.StandardGame(p1=players.negamaxabp.NegamaxAlphaBetaPruningPlayer(4), p2=players.negamaxabp.NegamaxAlphaBetaPruningPlayer(4), verbose=True)
#game = connectfour.games.standard.StandardGame(p1=players.random.RandomPlayer(), p2=players.negamax.NegamaxPlayer(4), verbose=True)
#game = connectfour.games.standard.StandardGame(p1=players.human.HumanPlayer(), p2=players.negamaxalphabeta.NegamaxAlphaBetaPlayer(4, verbose=True), verbose=True)
game.play()
