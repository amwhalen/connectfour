import connectfour

b = connectfour.Board()
p = connectfour.PerfectPlayer()

# let's place a move in the middle col
b.placeToken(1, 3)

# now see how the perfect player solves it:
solvedBoard = p.solveBoard(b, 2)

print "we win:"
print solvedBoard