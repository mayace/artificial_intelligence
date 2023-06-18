# star * search
import os
import random
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
        return (
            "\n".join(
                self.state[index : index + 3] for index in range(0, len(self.state), 3)
            )
            + "\nh="
            + str(self.h)
            + "\nscore="
            + str(self.score)
        )

    def graph_create_node(self):
        dot.node(
            str(self.node_num),
            self.graph_get_conent(),
            shape="circle",
        )
        if self.parent:
            dot.edge(
                str(self.parent.node_num),
                str(self.node_num),
                label=str(self.cost),
            )

    def __repr__(self):
        return f"({self.state}, {self.cost}, {self.h})"

    def set_as_visited(self):
        dot.node(str(self.node_num), style="invisible")

    def set_as_solution(self):
        dot.node(
            str(self.node_num),
            self.graph_get_conent(),
            shape="doublecircle",
        )
        temp = self
        while temp:
            dot.node(str(temp.node_num), style="filled", fillcolor="aqua")
            temp = temp.parent
        # dot.edge(str(self.node_num), str(self.parent.node_num))


class Puzzle:
    COLS = 3
    ROWS = 3

    def __init__(self, goal, n=20):
        self.goal = goal
        self.n = n
        self.start = self.get_start()

    def mix(self, state):
        successors = self.get_successors(Node(state, h=self.get_h(state)))
        return random.choice(successors).state

    def get_start(self):
        start = self.goal
        for i in range(self.n):
            start = self.mix(start)

        return start

    def get_h(self, state):
        total = 0
        for index, item in enumerate(state):
            sol_index = self.goal.index(item)
            total += abs(index % self.COLS - sol_index % self.COLS) + abs(
                index // self.ROWS - sol_index // self.ROWS
            )

        return total

    def get_sucesor(self, node, i1, i2):
        state = node.state
        new_state = ""

        for index in range(len(state)):
            if index == i1:
                new_state += state[i2]
            elif index == i2:
                new_state += state[i1]
            else:
                new_state += state[index]

        return Node(new_state, parent=node, h=self.get_h(new_state))

    def get_successors(self, node):
        index = node.state.index("0")
        if index == 0:
            return [
                self.get_sucesor(node, 0, 1),
                self.get_sucesor(node, 0, 3),
            ]

        if index == 1:
            return [
                self.get_sucesor(node, 1, 0),
                self.get_sucesor(node, 1, 2),
                self.get_sucesor(node, 1, 4),
            ]
        if index == 2:
            return [
                self.get_sucesor(node, 2, 1),
                self.get_sucesor(node, 2, 5),
            ]

        if index == 3:
            return [
                self.get_sucesor(node, 3, 0),
                self.get_sucesor(node, 3, 4),
                self.get_sucesor(node, 3, 6),
            ]

        if index == 4:
            return [
                self.get_sucesor(node, 4, 1),
                self.get_sucesor(node, 4, 3),
                self.get_sucesor(node, 4, 5),
                self.get_sucesor(node, 4, 7),
            ]

        if index == 5:
            return [
                self.get_sucesor(node, 5, 2),
                self.get_sucesor(node, 5, 4),
                self.get_sucesor(node, 5, 8),
            ]

        if index == 6:
            return [
                self.get_sucesor(node, 6, 3),
                self.get_sucesor(node, 6, 7),
            ]

        if index == 7:
            return [
                self.get_sucesor(node, 7, 4),
                self.get_sucesor(node, 7, 6),
                self.get_sucesor(node, 7, 8),
            ]

        if index == 8:
            return [
                self.get_sucesor(node, 8, 5),
                self.get_sucesor(node, 8, 7),
            ]

        return None


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


def mix(state, goal):
    successors = get_5successors(Node(state, h=get_5h(state, goal)), goal)
    return random.choice(successors).state


def solve_mix(goal, n=20):
    start = goal
    for i in range(n):
        start = mix(start, goal)

    solve(start, goal)


def not_visted(node, visited):
    result = sum(1 for x in visited if x.state == node.state) == 0

    if not result:
        node.set_as_visited()

    return result


def solve(puzzle: Puzzle, delay=0.1, limit=0):
    reset_node_num()
    reset_dot()
    count = 0
    visited = []
    node_list = [
        Node(
            puzzle.start,
            h=puzzle.get_h(puzzle.start),
        )
    ]
    while node_list:
        count += 1
        node = node_list.pop(0)
        visited.append(node)
        print(node)
        time.sleep(delay)
        if node.state == puzzle.goal:
            node.set_as_solution()
            print("found")
            break

        if not limit or node.level < limit:
            successors = puzzle.get_successors(node)
            if successors:
                node_list.extend(
                    [item for item in successors if not_visted(item, visited)]
                )
                node_list.sort(key=lambda x: x.h)

    dot.render("star", os.getcwd() + "/output")


def solve_by_hill_climbing(puzzle: Puzzle, delay=0.1, limit=0):
    reset_node_num()
    reset_dot()
    count = 0
    visited = []
    node_list = [
        Node(
            puzzle.start,
            h=puzzle.get_h(puzzle.start),
        )
    ]
    while node_list:
        count += 1
        node = node_list.pop(0)
        visited.append(node)
        print(node)
        time.sleep(delay)
        if node.state == puzzle.goal:
            node.set_as_solution()
            print("found")
            break

        if not limit or node.level < limit:
            successors = puzzle.get_successors(node)
            if successors:
                successors = [item for item in successors if not_visted(item, visited)]
                successors.sort(key=lambda x: x.h)
                if successors:
                    while len(successors) > 1:
                        successors.pop().set_as_visited()
                    node_list.extend(successors)

    dot.render("climbing", os.getcwd() + "/output")


def solve_by_beam(
    puzzle: Puzzle, delay=0.1, limit=0, beam_size=2, exclude_visited=True
):
    reset_node_num()
    reset_dot()
    count = 0
    visited = []
    node_list = [
        Node(
            puzzle.start,
            h=puzzle.get_h(puzzle.start),
        )
    ]
    while node_list:
        count += 1
        node = node_list.pop(0)
        visited.append(node)
        print(node)
        time.sleep(delay)
        if node.state == puzzle.goal:
            node.set_as_solution()
            print("found")
            break

        if not limit or node.level < limit:
            successors = puzzle.get_successors(node)
            if successors:
                if exclude_visited:
                    successors = [
                        item for item in successors if not_visted(item, visited)
                    ]
                successors.sort(key=lambda x: x.h)
                node_list.extend(successors[:beam_size])

    dot.render("beam", os.getcwd() + "/output")
