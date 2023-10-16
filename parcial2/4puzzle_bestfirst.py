# Autor: Luis Espino 2016

import time


def heuristic(nodo_actual, nodo_fin):
    # return [x != y for (x, y) in zip(nodo_actual, nodo_fin)].count(True)
    total = 0
    for index, item in enumerate(nodo_actual):
        total += abs(index - nodo_fin.index(item))
    return total


def sucesores(n, s, nivel):
    return [
        [n[1] + n[0] + n[2] + n[3], heuristic(n[1] + n[0] + n[2] + n[3], s), nivel + 1],
        [n[0] + n[2] + n[1] + n[3], heuristic(n[0] + n[2] + n[1] + n[3], s), nivel + 1],
        [n[0] + n[1] + n[3] + n[2], heuristic(n[0] + n[1] + n[3] + n[2], s), nivel + 1],
    ]



def bestfirst(nodo_inicio, nodo_fin):
    print("\nBEST-FIRST")
    lista = [[nodo_inicio, heuristic(nodo_inicio, nodo_fin), 0]]
    visited = []
    while lista:
        nodo_actual = lista.pop(0)
        visited.append(nodo_actual[0])
        print(nodo_actual)
        time.sleep(0.1)
        if nodo_actual[0] == nodo_fin:
            return print("SOLUCION",len(lista), len(visited))
        temp = sucesores(nodo_actual[0], nodo_fin, nodo_actual[2])
        print(temp)
        if temp:
            lista.extend(temp)
            # lista.extend(item for item in temp if item[0] not in visited)
            # lista.sort(key=lambda x: int(x[2] +x[1])) #star
            lista.sort(key=lambda x: int(x[1])) #best first
            # lista = lista[:2]
            print(lista)
    print("NO-SOLUCION")


# bestfirst("dcba", "abcd")
bestfirst("1234", "4321")
