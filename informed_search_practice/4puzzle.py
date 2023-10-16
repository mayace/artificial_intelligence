# "hola"

import random


def h_casillas(start, end):
    return [x != y for (x, y) in zip(start, end)].count(True)


def h_manhattan(start, end):
    total = 0
    for index, item in enumerate(end):
        total += abs(start.index(item) - index)

    return total


# def h_euclidean(start, end):
#     return sum(
#         ((x - y) ** 2) ** 0.5 for (x, y) in zip(start, end)
#     )  # **0.5 is the square root


def succesors(current, end, h):
    (node, _, level) = current
    return [
        [
            node[1] + node[0] + node[2] + node[3],
            h(node[1] + node[0] + node[2] + node[3], end),
            level + 1,
        ],
        [
            node[0] + node[2] + node[1] + node[3],
            h(node[0] + node[2] + node[1] + node[3], end),
            level + 1,
        ],
        [
            node[0] + node[1] + node[3] + node[2],
            h(node[0] + node[1] + node[3] + node[2], end),
            level + 1,
        ],
    ]


def bestfirst(start, end, h=None, beam=None, star=None):
    print("BEST-FIRST")
    lista = [[start, h(start, end), 0]]
    visitados = []
    while lista:
        current = lista.pop(0)
        visitados.extend(current)
        print(current)
        if current[0] == end:
            print("SOLUCION", "VISITADOS", len(visitados))
            print("SOLUCION", "NO VISITADOS", len(lista))
            print("HAY OTRA SOLUCION", [item for item in lista if item[1] == 0])
            return
        temp = succesors(current, end, h)
        print("succesors", temp)
        if temp:
            if beam and beam > 0:
                temp.sort(key=lambda x: x[1])
                lista.extend(item for item in temp[:beam] if item not in visitados)
            else:
                lista.extend(item for item in temp if item not in visitados)

            if star:
                lista.sort(key=lambda x: x[1] + x[2])
            else:
                lista.sort(key=lambda x: x[1])

            print("all", len(lista), lista)
            if len(lista) > 1000:
                print("NO-SOLUCION")
                return
    print("NO-SOLUCION")


# end = "hola"
# start = end
# for item in range(20):
#     start = random.choice(succesors((start, 0, 0), end, h_casillas))[0]


start = "3214"
end = "1234"

start = "DCBA"
end = "ABCD"


print("\nSTART", start)
print("END", end)

# print("\nCASILLAS")
# bestfirst(start, end, h=h_casillas)
# print("\nMANHATTAN")


bestfirst(start, end, h=h_casillas, beam=2)
# bestfirst(start, end, h=h_manhattan)
