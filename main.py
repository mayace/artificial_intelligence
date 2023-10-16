from puzzle import star

# import  graphviz, os
# dot = graphviz.Graph()

# dot.node("A", "test")

# print(dot.source)


# output = os.getcwd() + "/graph/test"
# dot.view(output)


# star.solve_mix("120345")


# 8 puzzle
# p = star.Puzzle("123456780", n=20)

# star.solve(p)
# star.solve_by_hill_climbing(p)
# star.solve_by_beam(p)

# 15 puzzle

p = star.Puzzle15([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0], n=20)
star.solve_by_hill_climbing(p)
