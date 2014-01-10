import connectfour as cf
import connectfour.players as players
import connectfour.games.standard

game = connectfour.games.standard.StandardGame(p1=players.human.HumanPlayer(), p2=players.random.RandomPlayer(), verbose=True)
game.play()
