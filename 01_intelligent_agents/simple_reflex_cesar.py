# Luis Espino 2017

import time


def reflex_agent(location, state):
    if state == "DIRTY":
        return "CLEAN"
    elif location == "A":
        return "RIGHT"
    elif location == "B":
        return "LEFT"

def dirting(states):
    import random
    r = random.randrange(0,10)
    if r in range(0,2):
        states[1] = "DIRTY"
    elif r in range(2,4):
        states[2] = "DIRTY"
    elif r in range(4,6):
        states[1] = "DIRTY"
        states[2] = "DIRTY"
        

VISITED = set()

def test(states):
    while len(VISITED) < 8:
        location = states[0]
        state = (states[2], states[1])[states[0] == "A"]
        action = reflex_agent(location, state)
        VISITED.add(tuple(states))
        # print(len(VISITED))
        print("Location: " + location + " | Action: " + action, " | visitados: " + str(len(VISITED)))
        if action == "CLEAN":
            if location == "A":
                states[1] = "CLEAN"
            elif location == "B":
                states[2] = "CLEAN"
        elif action == "RIGHT":
            states[0] = "B"
        elif action == "LEFT":
            states[0] = "A"
        time.sleep(0.5)
        dirting(states)


STATES = ["A", "DIRTY", "DIRTY"]

test(STATES)
