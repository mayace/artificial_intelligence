# Autor: Luis Espino 2016


def heuristic(nodo_actual, nodo_fin):
    return [x != y for (x, y) in zip(nodo_actual, nodo_fin)].count(True)


def h_manhattan(current, end):
    total = 0
    for index, item in enumerate(end):
        current_index = current.index(item)
        x = abs(index % 3 - current_index % 3)
        y = abs(index // 3 - current_index // 3)
        total += x + y

    return total


def sucesores(current, s, h):
    n, _, level = current
    i = n.index("0")
    if i == 0:
        return [
            [
                n[1] + n[0] + n[2] + n[3] + n[4] + n[5],
                h(n[1] + n[0] + n[2] + n[3] + n[4] + n[5], s),
                level + 1,
            ],
            [
                n[3] + n[1] + n[2] + n[0] + n[4] + n[5],
                h(n[3] + n[1] + n[2] + n[0] + n[4] + n[5], s),
                level + 1,
            ],
        ]

    if i == 1:
        return [
            [
                n[1] + n[0] + n[2] + n[3] + n[4] + n[5],
                h(n[1] + n[0] + n[2] + n[3] + n[4] + n[5], s),
                level + 1,
            ],
            [
                n[0] + n[2] + n[1] + n[3] + n[4] + n[5],
                h(n[0] + n[2] + n[1] + n[3] + n[4] + n[5], s),
                level + 1,
            ],
            [
                n[0] + n[4] + n[2] + n[3] + n[1] + n[5],
                h(n[0] + n[4] + n[2] + n[3] + n[1] + n[5], s),
                level + 1,
            ],
        ]
    if i == 2:
        return [
            [
                n[0] + n[2] + n[1] + n[3] + n[4] + n[5],
                h(n[0] + n[2] + n[1] + n[3] + n[4] + n[5], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[5] + n[3] + n[4] + n[2],
                h(n[0] + n[1] + n[5] + n[3] + n[4] + n[2], s),
                level + 1,
            ],
        ]
    if i == 3:
        return [
            [
                n[3] + n[1] + n[2] + n[0] + n[4] + n[5],
                h(n[3] + n[1] + n[2] + n[0] + n[4] + n[5], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[2] + n[4] + n[3] + n[5],
                h(n[0] + n[1] + n[2] + n[4] + n[3] + n[5], s),
                level + 1,
            ],
        ]

    if i == 4:
        return [
            [
                n[0] + n[4] + n[2] + n[3] + n[1] + n[5],
                h(n[0] + n[4] + n[2] + n[3] + n[1] + n[5], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[2] + n[4] + n[3] + n[5],
                h(n[0] + n[1] + n[2] + n[4] + n[3] + n[5], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[2] + n[3] + n[5] + n[4],
                h(n[0] + n[1] + n[2] + n[3] + n[5] + n[4], s),
                level + 1,
            ],
        ]

    if i == 5:
        return [
            [
                n[0] + n[1] + n[5] + n[3] + n[4] + n[2],
                h(n[0] + n[1] + n[5] + n[3] + n[4] + n[2], s),
                level + 1,
            ],
            [
                n[0] + n[1] + n[2] + n[3] + n[5] + n[4],
                h(n[0] + n[1] + n[2] + n[3] + n[5] + n[4], s),
                level + 1,
            ],
        ]


def bestfirst(nodo_inicio, nodo_fin, h=None, beam=None):
    print("\nBEST-FIRST")
    lista = [[nodo_inicio, h(nodo_inicio, nodo_fin), 0]]
    visitados = []
    while lista:
        current = lista.pop(0)
        visitados.extend(current)
        print("CURRENT", current)
        if current[0] == nodo_fin:
            print("VISITADOS", len(visitados), "SOLUCION")
            print("NO VISITADOS", len(lista))
            return

        temp = sucesores(current, nodo_fin, h)
        print("SUCESORES", temp)
        if temp:
            if beam and beam > 0:
                temp.sort(key=lambda x: x[1])
                lista.extend(temp[:beam])
            else:
                lista.extend(temp)
            lista.sort(key=lambda x: int(x[1]))
            print("LISTA", len(lista), lista)
    print("NO-SOLUCION")


bestfirst("243105", "123450", h=h_manhattan, beam=1)
