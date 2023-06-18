from puzzle import star

# import  graphviz, os
# dot = graphviz.Graph()

# dot.node("A", "test")

# print(dot.source)


# output = os.getcwd() + "/graph/test"
# dot.view(output)


# star.solve_mix("120345")

p = star.Puzzle("123456780", n=40)

star.solve(p)
star.solve_by_hill_climbing(p)
star.solve_by_beam(p)
