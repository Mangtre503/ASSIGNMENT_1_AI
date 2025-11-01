"""Solve the sokoban problem using heuristic search (A* Search)"""

import heapq
from .. import utils

heuristic_cache = {}
def compute_heuristic(boxes, goals):
    key =tuple(sorted(boxes))
    if key not in heuristic_cache:
        heuristic_cache[key] = utils.compute_heuristic(boxes, goals)
    return heuristic_cache[key]
        

def astar(testcase):
    '''
        A* Search
        Final function for the heuristic solution
        input:
            Testcase file name, eg: "mini_cosmos_1.txt"
        output:
            solutions: The sequence of movements, eg: UULR
                        or None if there is no solution
    '''
    h, w, walls, goals, boxes0, player0 = utils.parse_board(testcase)
    # If the initial state is already the goal state
    if utils.goal_test(boxes0, goals):
        return ""
    start = (player0, boxes0)
    parent = {start: (None, None)}  # state -> (prev_state, move_char)
    g_val = {start: 0}            
    closed = set()                  # avoid re-expanding same state
    queue = []

    f_start = compute_heuristic(boxes0, goals)
    heapq.heappush(queue, (f_start, 0, start))  # (f, g, state)

    while queue:
        _, g_current, state_current = heapq.heappop(queue) # get the state with the lowest f and remove it from the queue
        if g_current>g_val[state_current]:
            continue # if this state has a higher f(n) value than the one in the open list, skip it
        # If the current state is the goal state
        _, boxes_current = state_current
        if utils.goal_test(boxes_current, goals):
            # reconstruct path
            path_moves = []
            s = state_current
            while parent[s][0] is not None:
                prev, ch = parent[s]
                path_moves.append(ch)
                s = prev
            return "".join(reversed(path_moves))

        for state_neighbor, move_char in utils.neighbors(state_current, walls, h, w):
            g_neighbor = g_current + 1
            if state_neighbor not in g_val or g_neighbor < g_val[state_neighbor]:
                g_val[state_neighbor] = g_neighbor
                parent[state_neighbor] = (state_current, move_char)

                _, boxes_neighbor = state_neighbor
                f_neighbor = g_neighbor + compute_heuristic(boxes_neighbor, goals)
                heapq.heappush(queue, (f_neighbor, g_neighbor, state_neighbor))

    return None