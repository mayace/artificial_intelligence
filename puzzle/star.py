# star * search
import os
import time
from graphviz import Graph, Digraph

NODES_NUM = 0
dot = Digraph(comment="Star Search", format="png")

# 1,2,3


class Node:
    def __init__(self, state, parent=None, h=None, cost=0, node_num=None):
        self.state: str = state
        self.parent: Node = parent
        self.h = h
        self.level: int = parent.level + 1 if parent else 0
        self.node_num: int = node_num if node_num else get_node_num()
        self.cost: int = cost if cost else self.level
        self.score: int = self.cost + self.h
        self.graph_create_node()

    def graph_get_conent(self):
        return "\n".join(
            self.state[index : index + 3] for index in range(0, len(self.state), 3)
        )

    def graph_create_node(self):
        dot.node(str(self.node_num), self.graph_get_conent(), shape="circle")
        if self.parent:
            dot.edge(str(self.parent.node_num), str(self.node_num))

    def __repr__(self):
        return f"({self.state}, {self.cost})"

    def set_as_solution(self):
        dot.node(str(self.node_num), self.graph_get_conent(), shape="doublecircle")
        # dot.edge(str(self.node_num), str(self.parent.node_num))


def get_successors(node: Node, goal: str):
    index = node.state.index("0")
    i0, i1, i2 = node.state

    if index == 0:
        new_state = i1 + i0 + i2
        return [
            Node(
                new_state,
                parent=node,
                h=get_2h(new_state, goal),
            ),
        ]
    if index == 1:
        return [
            Node(
                i0 + i2 + i1,
                parent=node,
                h=get_2h(i0 + i2 + i1, goal),
            ),
            Node(
                i1 + i0 + i2,
                parent=node,
                h=get_2h(i1 + i0 + i2, goal),
            ),
        ]


def get_5successors(node: Node, goal: str):
    index = node.state.index("0")
    i0, i1, i2, i3, i4, i5 = node.state

    if index == 0:
        return [
            Node(
                i1 + i0 + i2 + i3 + i4 + i5,
                parent=node,
                h=get_5h(i1 + i0 + i2 + i3 + i4 + i5, goal),
            ),
            Node(
                i3 + i1 + i2 + i0 + i4 + i5,
                parent=node,
                h=get_5h(i3 + i1 + i2 + i0 + i4 + i5, goal),
            ),
        ]
    if index == 1:
        return [
            Node(
                i1 + i0 + i2 + i3 + i4 + i5,
                parent=node,
                h=get_5h(i1 + i0 + i2 + i3 + i4 + i5, goal),
            ),
            Node(
                i0 + i2 + i1 + i3 + i4 + i5,
                parent=node,
                h=get_5h(i0 + i2 + i1 + i3 + i4 + i5, goal),
            ),
            Node(
                i0 + i4 + i2 + i3 + i1 + i5,
                parent=node,
                h=get_5h(i0 + i4 + i2 + i3 + i1 + i5, goal),
            ),
        ]
    if index == 2:
        return [
            Node(
                i0 + i2 + i1 + i3 + i4 + i5,
                parent=node,
                h=get_5h(i0 + i2 + i1 + i3 + i4 + i5, goal),
            ),
            Node(
                i0 + i1 + i5 + i3 + i4 + i2,
                parent=node,
                h=get_5h(i0 + i1 + i5 + i3 + i4 + i2, goal),
            ),
        ]
    if index == 3:
        return [
            Node(
                i3 + i1 + i2 + i0 + i4 + i5,
                parent=node,
                h=get_5h(i3 + i1 + i2 + i0 + i4 + i5, goal),
            ),
            Node(
                i0 + i1 + i2 + i4 + i3 + i5,
                parent=node,
                h=get_5h(i0 + i1 + i2 + i4 + i3 + i5, goal),
            ),
        ]

    if index == 4:
        return [
            Node(
                i0 + i1 + i2 + i4 + i3 + i5,
                parent=node,
                h=get_5h(i0 + i1 + i2 + i4 + i3 + i5, goal),
            ),
            Node(
                i0 + i1 + i2 + i3 + i5 + i4,
                parent=node,
                h=get_5h(i0 + i1 + i2 + i3 + i5 + i4, goal),
            ),
            Node(
                i0 + i4 + i2 + i3 + i1 + i5,
                parent=node,
                h=get_5h(i0 + i4 + i2 + i3 + i1 + i5, goal),
            ),
        ]

    if index == 5:
        return [
            Node(
                i0 + i1 + i2 + i3 + i5 + i4,
                parent=node,
                h=get_5h(i0 + i1 + i2 + i3 + i5 + i4, goal),
            ),
            Node(
                i0 + i1 + i5 + i3 + i4 + i2,
                parent=node,
                h=get_5h(i0 + i1 + i5 + i3 + i4 + i2, goal),
            ),
        ]


def get_2h(state, goal):
    total = 0
    for index, item in enumerate(state):
        sol_index = goal.index(item)
        total += abs(index % 3 - sol_index % 3)

    return total


def get_5h(state, goal):
    total = 0
    for index, item in enumerate(state):
        sol_index = goal.index(item)
        total += abs(index % 3 - sol_index % 3) + abs(index // 2 - sol_index // 2)

    return total


def get_node_num():
    global NODES_NUM
    NODES_NUM += 1
    return NODES_NUM


def reset_node_num():
    global NODES_NUM
    NODES_NUM = 0


def reset_dot():
    global dot
    dot = Digraph(comment="Star Search", format="png")


def solve(start, goal, delay=0.1, limit=0):
    reset_node_num()
    reset_dot()
    visited = []
    node_list = [
        Node(
            start,
            h=get_5h(start, goal),
        )
    ]
    while node_list:
        node = node_list.pop(0)
        visited.append(node)
        print(node)
        time.sleep(delay)
        if node.state == goal:
            node.set_as_solution()
            print("found")
            break

        successors = get_5successors(node, goal)
        if successors:
            node_list.extend(successors)
            node_list.sort(key=lambda x: x.cost)

    dot.render("star", os.getcwd() + "/output")
