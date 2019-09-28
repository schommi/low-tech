import z3

feed = z3.Int("feed")
clean = z3.Int("clean")
play = z3.Int("play")

solver = z3.Solver()

z3.solve(
  (feed * 10) - (play * 2) == 72,
  (feed * 2) + (play * 4) - (clean * 1) == 30,
  (clean * 6) - (feed * 1) - (play * 1) == 0)

# clean = 2, play = 4, feed = 8   
