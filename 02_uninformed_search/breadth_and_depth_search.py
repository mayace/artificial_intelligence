# Luis Espino 2017
# Búsqueda por anchura y profundidad
# Problema matriz de 3x3
#
# 1 2 3
# 4 5 6
# 7 8 9


import time


class Node:
    def __init__(self, value, parent=None, cost=None):
        self.value = value
        self.parent = parent
        self.level = parent.level + 1 if parent else 0
        self.cost = cost if (cost + (parent.cost if parent else 0)) else self.level

    def __str__(self) -> str:
        return f"({self.value},level={self.level})"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other):
        return self.value == other.value


def sucesores(n: Node):
    if n.value == 1:
        return [Node(2, parent=n), Node(4, parent=n), Node(5, parent=n)]
    elif n.value == 2:
        return [
            Node(1, parent=n),
            Node(3, parent=n),
            Node(4, parent=n),
            Node(5, parent=n),
            Node(6, parent=n),
        ]
    elif n.value == 3:
        return [Node(2, parent=n), Node(5, parent=n), Node(6, parent=n)]
    elif n.value == 4:
        return [
            Node(1, parent=n),
            Node(2, parent=n),
            Node(5, parent=n),
            Node(7, parent=n),
            Node(8, parent=n),
        ]
    elif n.value == 5:
        return [
            Node(1, parent=n),
            Node(2, parent=n),
            Node(3, parent=n),
            Node(4, parent=n),
            Node(6, parent=n),
            Node(7, parent=n),
            Node(8, parent=n),
            Node(9, parent=n),
        ]
    elif n.value == 6:
        return [
            Node(2, parent=n),
            Node(3, parent=n),
            Node(5, parent=n),
            Node(8, parent=n),
            Node(9, parent=n),
        ]
    elif n.value == 7:
        return [Node(4, parent=n), Node(5, parent=n), Node(8, parent=n)]
    elif n.value == 8:
        return [
            Node(4, parent=n),
            Node(5, parent=n),
            Node(6, parent=n),
            Node(7, parent=n),
            Node(9, parent=n),
        ]
    elif n.value == 9:
        return [Node(5, parent=n), Node(6, parent=n), Node(8, parent=n)]
    else:
        return None


def anchura(nodo_inicio, nodo_fin, desc=False, limit=None):
    lista = [Node(nodo_inicio)]
    visitados = []
    while lista:
        nodo_actual = lista.pop(0)  # visitar nodo
        visitados.append(nodo_actual)
        print("actual=" + str(nodo_actual))
        time.sleep(0.1)
        if nodo_actual == Node(nodo_fin):
            print("visitados=", len(visitados))
            print("no visitados=", len(lista))
            return print("SOLUCIÓN")

        if not limit or nodo_actual.level < limit:
            temp = sucesores(nodo_actual)
            if desc:
                temp.reverse()  # make it desc
            if temp:
                lista.extend(temp)
    print("NO-SOLUCIÓN")


def profundidad(nodo_inicio, nodo_fin):
    lista = [nodo_inicio]
    while lista:
        nodo_actual = lista.pop(0)
        print(nodo_actual)
        if nodo_actual == nodo_fin:
            # print(len(lista))
            return print("SOLUCIÓN")
        temp = sucesores(nodo_actual)
        temp.reverse()
        print(temp)
        if temp:
            temp.extend(lista)
            lista = temp
            print(lista)
    print("NO-SOLUCIÓN")


def bidireccional(nodo_inicio, nodo_fin):
    front = [Node(nodo_inicio)]
    back = [Node(nodo_fin)]
    while front or back:
        nfront = front.pop(0)
        nback = back.pop(0)
        print("nfront=", nfront, "nback=", nback)
        time.sleep(0.2)
        if nfront in back and nback in front:
            if back.index(nfront) < front.index(nback):
                return print("both=", nfront)
            else:
                return print("both=", nback)
        elif nfront in back:
            return print("comun-front=", nfront)
        elif nback in front:
            return print("comun-back=", nback)

        temp = sucesores(nfront)
        if temp:
            front.extend(temp)
            print("front-list=", front)
        temp = sucesores(nback)
        if temp:
            back.extend(temp)
            print("back-list=", back)

    print("NO-SOLUCIÓN")


def costo_uniforme(nodo_inicio, nodo_fin, sucesores=Node):
    lista = [Node(nodo_inicio)]
    while lista:
        nodo_actual = lista.pop(0)
        print(nodo_actual)
        if nodo_actual == Node(nodo_fin):
            return print("SOLUCIÓN")

        if sucesores(nodo_actual):
            temp = sucesores(nodo_actual)

            print(temp)
            if temp:
                lista.extend(temp)
                lista.sort(key=lambda x: x.cost)
                print(lista)
    print("NO-SOLUCIÓN")


# anchura(1, 9)
bidireccional(1, 9)
# profundidad (1,9)
