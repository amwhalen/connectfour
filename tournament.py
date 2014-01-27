import connectfour as cf
import connectfour.players as players
import connectfour.games.standard as standard

def playGame(p1, p2):
    verbose = (p1.isHuman() or p2.isHuman())
    game = standard.StandardGame(p1, p2, verbose=verbose)
    game.play()
    return game

players = [
    players.negamax.NegamaxPlayer(6),
    players.negamax.NegamaxPlayer(5),
    players.negamax.NegamaxPlayer(4),
    players.negamax.NegamaxPlayer(3),
    players.negamax.NegamaxPlayer(2),
    players.negamax.NegamaxPlayer(1),
    players.negamaxabp.NegamaxAlphaBetaPruningPlayer(6),
    players.negamaxabp.NegamaxAlphaBetaPruningPlayer(5),
    players.negamaxabp.NegamaxAlphaBetaPruningPlayer(4),
    players.negamaxabp.NegamaxAlphaBetaPruningPlayer(3),
    players.negamaxabp.NegamaxAlphaBetaPruningPlayer(2),
    players.negamaxabp.NegamaxAlphaBetaPruningPlayer(1),
    players.random.RandomPlayer(),
    players.cover.CoverPlayer()
]

stats = {}
for x in range(0, len(players)):
    stats[x] = {'wins':0,'losses':0}

for p1index, p1 in enumerate(players):
    for p2index, p2 in enumerate(players):
        # don't play the same player against itself
        if p1 == p2:
            continue
        # play the game
        print "==============================="
        print "%s vs. %s" % (p1.getName(), p2.getName())
        game = playGame(p1, p2)
        winner = game.getWinner()
        # update the scoreboard
        if winner == 1:
            stats[p1index]['wins'] += 1
            stats[p2index]['losses'] += 1
        else:
            stats[p1index]['losses'] += 1
            stats[p2index]['wins'] += 1
        # announce the winner
        p_winner = p1 if (winner == 1) else p2
        print "%s winner in %d turns." % (p_winner.getName(), game.getTurns())
        board = game.getBoard()
        print board.getMoves()
        print board

print "Name Wins Losses"
for index,p in enumerate(players):
    print "%s %d %d" % (p.getName(), stats[index]['wins'], stats[index]['losses'])
