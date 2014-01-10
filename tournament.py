import connectfour as cf
import connectfour.players as players
import connectfour.games.standard as standard

def playGame(p1, p2):
    print "==============================="
    print p1.getName()+" vs. "+p2.getName()
    verbose = (p1.isHuman() or p2.isHuman())
    game = standard.StandardGame(p1, p2, verbose=verbose)
    game.play()
    winner = p1 if (game.getWinner() == 1) else p2
    print p1.getName()+" vs. "+p2.getName()+" winner in "+str(game.getTurns())+" turns: "+winner.getName()

players = [
    players.cover.CoverPlayer(),
    #players.human.HumanPlayer(),
    players.random.RandomPlayer()
]

#playGame(players[0], players[1])
#playGame(players[1], players[2])
#playGame(players[2], players[0])

playGame(players[0], players[1])
playGame(players[1], players[0])