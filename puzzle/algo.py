import time, random

SOLUTION = (1, 2, 3, 4, 5, 6, 7, 8, None)
# 1,2,3
# 4,5,6
# 7,8,None


def get_sucesor(l, i1, i2):
    inicio, final = l
    newl = [
        inicio[i1] if index == i2 else inicio[i2] if index == i1 else inicio[index]
        for index in range(len(inicio))
    ]

    return getnode([newl, final])


def sucesores(n):
    l, s, index = n

    if index == 0:
        return [
            get_sucesor(l, 0, 1),
            get_sucesor(l, 0, 3),
        ]

    if index == 1:
        return [
            get_sucesor(l, 1, 0),
            get_sucesor(l, 1, 2),
            get_sucesor(l, 1, 4),
        ]
    if index == 2:
        return [
            get_sucesor(l, 2, 1),
            get_sucesor(l, 2, 5),
        ]

    if index == 3:
        return [
            get_sucesor(l, 3, 0),
            get_sucesor(l, 3, 4),
            get_sucesor(l, 3, 6),
        ]

    if index == 4:
        return [
            get_sucesor(l, 4, 1),
            get_sucesor(l, 4, 3),
            get_sucesor(l, 4, 5),
            get_sucesor(l, 4, 7),
        ]

    if index == 5:
        return [
            get_sucesor(l, 5, 2),
            get_sucesor(l, 5, 4),
            get_sucesor(l, 5, 8),
        ]

    if index == 6:
        return [
            get_sucesor(l, 6, 3),
            get_sucesor(l, 6, 7),
        ]

    if index == 7:
        return [
            get_sucesor(l, 7, 4),
            get_sucesor(l, 7, 6),
            get_sucesor(l, 7, 8),
        ]

    if index == 8:
        return [
            get_sucesor(l, 8, 5),
            get_sucesor(l, 8, 7),
        ]

    return None


def poplist(lista):
    # if len(lista) > 1:
    #     index = round(random.random())
    #     return lista.pop(index)
    return lista.pop(0)


def is_goal(nodo_actual):
    return nodo_actual[1] == 0


def get_manthattan_value(index):
    # x, y
    return index % 3, index // 3


def get_manthattan_distance(nodo):
    total = 0
    for index, item in enumerate(nodo[0]):
        if item:
            man = get_manthattan_value(index)
            solution_man = get_manthattan_value(item - 1)
            total += abs(man[0] - solution_man[0]) + abs(man[1] - solution_man[1])
        # print(index, item, man,solution_man, total)

    return total


def get_casilla_weight(nodo):
    return sum(1 for i, j in zip(nodo[0], nodo[1]) if i != j)


def getweight(nodo):
    return get_manthattan_distance(nodo)


def getnode(nodo):
    return [nodo, getweight(nodo), nodo[0].index(None)]


def solve(nodo_inicio, node_final, delay=1):
    lista = [getnode([nodo_inicio, node_final])]
    visited = []
    while lista:
        nodo_actual = poplist(lista)
        if nodo_actual[0] in visited:
            continue
        visited.append(nodo_actual[0])
        print(nodo_actual, len(lista))
        time.sleep(delay)
        if is_goal(nodo_actual):
            return print("SOLUCIÓN")

        temp = sucesores(nodo_actual)
        # temp.reverse()
        # print(temp)
        if temp:
            lista.extend(temp)
            lista.sort(key=lambda x: x[1])
            # print(lista)
    print("NO-SOLUCIÓN")
