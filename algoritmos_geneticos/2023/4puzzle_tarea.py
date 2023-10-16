import random


def fitness(item):
    """zero is better"""
    return abs(1234 - item)


def best_one(i1, i2):
    if fitness(i1) <= fitness(i2):
        return i1
    return i2


def get_sons(p1, p2):
    j1 = int((p1 + p2) / 2)
    j2 = abs(2 * p1 - p2)
    j3 = abs(p1 - p2)
    j4 = int(p1 * 1.2)
    return j1, j2, j3, j4


def get_next_generation(generation):
    i1, i2, i3, i4 = generation
    p1 = best_one(i1, i2)
    p2 = best_one(i3, i4)

    j1, j2, j3, j4 = get_sons(p1, p2)
    s1 = best_one(j1, j2)
    s2 = best_one(j3, j4)

    next_generation = [p1, p2, s1, s2]
    random.shuffle(next_generation)
    return next_generation


def get_avg(generation):
    fit = [fitness(item) for item in generation]
    return sum(fit) / len(fit)


def solve(generation, iterations):
    for item in range(iterations):
        generation = get_next_generation(generation)
        print(item, generation)


def solve_convergence(generation, convergence):
    i = 0
    prev = get_avg(generation)
    while True:
        generation = get_next_generation(generation)
        current = get_avg(generation)
        conv = current / prev
        # print(prev, current, conv)
        print(i, conv, generation)
        if conv >= convergence:
            break
        i += 1
        prev = current


# generating first generation

generation = []
for _ in range(4):
    generation.extend([random.randint(0, 9999)])


print(generation)
# solve(generation, 15)
solve_convergence(generation, 0.95)
