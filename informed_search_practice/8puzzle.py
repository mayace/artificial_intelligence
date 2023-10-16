# Luis Espino 2017
import random


# tiles out heuristic
def h_tiles_out(current, end):
    return [x != y for (x, y) in zip(current, end)].count(True)


# def h_misplaced(current, end):
#     node, _, _ = current
#     total = 0
#     for index, item in enumerate(end):
#         if item != node[index]:
#             total += 1

#     return total


def h_manhattan(current, end):
    total = 0
    for index, item in enumerate(end):
        current_index = current.index(item)
        x = abs(index % 3 - current_index % 3)
        y = abs(index // 3 - current_index // 3)
        total += x + y

    return total


def h_euclidean(current, end):
    total = 0
    for index, item in enumerate(end):
        current_index = current.index(item)
        x = abs(index % 3 - current_index % 3)
        y = abs(index // 3 - current_index // 3)
        total += (x**2 + y**2) ** 0.5

    return total


def succesors(node, s, h):
    n, _, level = node
    i = n.index("0")
    if i == 0:
        return [
            [
                n[1] + n[0] + n[2] + n[3] + n[4] + n[5] + n[6] + n[7] + n[8],
                h(n[1] + n[0] + n[2] + n[3] + n[4] + n[5] + n[6] + n[7] + n[8], s),
                level + 1,
            ],
            [
                n[3] + n[1] + n[2] + n[0] + n[4] + n[5] + n[6] + n[7] + n[8],
                h(n[3] + n[1] + n[2] + n[0] + n[4] + n[5] + n[6] + n[7] + n[8], s),
                level + 1,
            ],
        ]
    elif i == 1:
        return [
            [
                n[1] + n[0] + n[2] + n[3] + n[4] + n[5] + n[6] + n[7] + n[8],
                h(n[1] + n[0] + n[2] + n[3] + n[4] + n[5] + n[6] + n[7] + n[8], s),
                level + 1,
            ],
            [
                n[0] + n[2] + n[1] + n[3] + n[4] + n[5] + n[6] + n[7] + n[8],
                h(n[0] + n[2] + n[1] + n[3] + n[4] + n[5] + n[6] + n[7] + n[8], s),
                level + 1,
            ],
            [
                n[0] + n[4] + n[2] + n[3] + n[1] + n[5] + n[6] + n[7] + n[8],
                h(n[0] + n[4] + n[2] + n[3] + n[1] + n[5] + n[6] + n[7] + n[8], s),
                level + 1,
            ],
        ]
    elif i == 2:
        return [
            [
                n[0] + n[2] + n[1] + n[3] + n[4] + n[5] + n[6] + n[7] + n[8],
                h(n[0] + n[2] + n[1] + n[3] + n[4] + n[5] + n[6] + n[7] + n[8], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[5] + n[3] + n[4] + n[2] + n[6] + n[7] + n[8],
                h(n[0] + n[1] + n[5] + n[3] + n[4] + n[2] + n[6] + n[7] + n[8], s),
                level + 1,
            ],
        ]
    elif i == 3:
        return [
            [
                n[3] + n[1] + n[2] + n[0] + n[4] + n[5] + n[6] + n[7] + n[8],
                h(n[3] + n[1] + n[2] + n[0] + n[4] + n[5] + n[6] + n[7] + n[8], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[2] + n[4] + n[3] + n[5] + n[6] + n[7] + n[8],
                h(n[0] + n[1] + n[2] + n[4] + n[3] + n[5] + n[6] + n[7] + n[8], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[2] + n[6] + n[4] + n[5] + n[3] + n[7] + n[8],
                h(n[0] + n[1] + n[2] + n[6] + n[4] + n[5] + n[3] + n[7] + n[8], s),
                level + 1,
            ],
        ]
    elif i == 4:
        return [
            [
                n[0] + n[4] + n[2] + n[3] + n[1] + n[5] + n[6] + n[7] + n[8],
                h(n[0] + n[4] + n[2] + n[3] + n[1] + n[5] + n[6] + n[7] + n[8], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[2] + n[4] + n[3] + n[5] + n[6] + n[7] + n[8],
                h(n[0] + n[1] + n[2] + n[4] + n[3] + n[5] + n[6] + n[7] + n[8], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[2] + n[3] + n[5] + n[4] + n[6] + n[7] + n[8],
                h(n[0] + n[1] + n[2] + n[3] + n[5] + n[4] + n[6] + n[7] + n[8], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[2] + n[3] + n[7] + n[5] + n[6] + n[4] + n[8],
                h(n[0] + n[1] + n[2] + n[3] + n[7] + n[5] + n[6] + n[4] + n[8], s),
                level + 1,
            ],
        ]
    elif i == 5:
        return [
            [
                n[0] + n[1] + n[5] + n[3] + n[4] + n[2] + n[6] + n[7] + n[8],
                h(n[0] + n[1] + n[5] + n[3] + n[4] + n[2] + n[6] + n[7] + n[8], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[2] + n[3] + n[5] + n[4] + n[6] + n[7] + n[8],
                h(n[0] + n[1] + n[2] + n[3] + n[5] + n[4] + n[6] + n[7] + n[8], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[2] + n[3] + n[4] + n[8] + n[6] + n[7] + n[5],
                h(n[0] + n[1] + n[2] + n[3] + n[4] + n[8] + n[6] + n[7] + n[5], s),
                level + 1,
            ],
        ]
    elif i == 6:
        return [
            [
                n[0] + n[1] + n[2] + n[6] + n[4] + n[5] + n[3] + n[7] + n[8],
                h(n[0] + n[1] + n[2] + n[6] + n[4] + n[5] + n[3] + n[7] + n[8], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[2] + n[3] + n[4] + n[5] + n[7] + n[6] + n[8],
                h(n[0] + n[1] + n[2] + n[3] + n[4] + n[5] + n[7] + n[6] + n[8], s),
                level + 1,
            ],
        ]
    elif i == 7:
        return [
            [
                n[0] + n[1] + n[2] + n[3] + n[4] + n[5] + n[7] + n[6] + n[8],
                h(n[0] + n[1] + n[2] + n[3] + n[4] + n[5] + n[7] + n[6] + n[8], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[2] + n[3] + n[7] + n[5] + n[6] + n[4] + n[8],
                h(n[0] + n[1] + n[2] + n[3] + n[7] + n[5] + n[6] + n[4] + n[8], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[2] + n[3] + n[4] + n[5] + n[6] + n[8] + n[7],
                h(n[0] + n[1] + n[2] + n[3] + n[4] + n[5] + n[6] + n[8] + n[7], s),
                level + 1,
            ],
        ]
    elif i == 8:
        return [
            [
                n[0] + n[1] + n[2] + n[3] + n[4] + n[5] + n[6] + n[8] + n[7],
                h(n[0] + n[1] + n[2] + n[3] + n[4] + n[5] + n[6] + n[8] + n[7], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[2] + n[3] + n[4] + n[8] + n[6] + n[7] + n[5],
                h(n[0] + n[1] + n[2] + n[3] + n[4] + n[8] + n[6] + n[7] + n[5], s),
                level + 1,
            ],
        ]


def mix(current, end):
    return random.choice(succesors(current, end, h_tiles_out))[0]


def bestfirst(start, end, h=None, star=None):
    # start the search
    print("BEST FIRST")
    unvisited = [[start, h(start, end), 0]]
    visited = []
    while unvisited:
        current = unvisited.pop(0)
        print("CURRENT", current)
        visited.extend([current])
        if current[0] == end:
            return print("SOLUTION IN " + str(len(visited)) + " ITERATIONS")
        temp = succesors(current, end, h)
        print("SUCCESORS", temp)
        # without repeating visited nodes
        unvisited.extend([x for x in temp if x[0] not in visited])
        if star:
            unvisited.sort(key=lambda x: x[1] + x[2])
        else:
            unvisited.sort(key=lambda x: x[1])

        print(
            "UNVISITED",
            len(unvisited),
            unvisited if len(unvisited) < 10 else str(unvisited[:10]) + "...",
        )

        if len(unvisited) > 500:
            break
    print("NO-SOLUTION")


# mix the end node
end = "123456780"
start = end
for x in range(0, 20):
    start = mix((start, 0, 0), end)

# start = "254713086"
print("\n\nCASILLAS", "START", start, "END", end)
bestfirst(start, end, h=h_tiles_out, star=False)
print("\n\nMANHATTAN", "START", start, "END", end)
bestfirst(start, end, h=h_manhattan, star=False)
print("\n\nEUCLIDEAN", "START", start, "END", end)
bestfirst(start, end, h=h_euclidean, star=False)
# bestfirst("062143758", end, h=h_tiles_out, star=True)
