"""Solve the sokoban problem using heuristic search (A* Search)"""

from queue import PriorityQueue
from .. import utils

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
    g_val={start:0} # keep track of g(n) values for each state
    queue=PriorityQueue()
    g_start=0
    f_start=utils.conmpute_cost(g_start, boxes0, goals)
    queue.put((f_start, g_start, start)) # push the initial state into the priority queue with f(0)=h(0)
    
    while not queue.empty():
        _, g_current, state_current = queue.get() # get the state with the lowest f and remove it from the queue
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
        # second, get all next possible states
        for state_neighbor, move_char in utils.neighbors(state_current, walls, h, w):
            g_neighbor=g_current+1 # cost from current state to the neighbor state
            if state_neighbor not in g_val or g_neighbor<g_val[state_neighbor]:
                g_val[state_neighbor]=g_neighbor
                parent[state_neighbor]=(state_current, move_char)
            _, boxes_neighbor = state_neighbor
            f_neighbor=utils.conmpute_cost(g_neighbor, boxes_neighbor, goals)
            
            queue.put((f_neighbor, g_neighbor, state_neighbor)) # push the next state into the priority queue with f(n)=g(n)+h(n)
    return None

utils.build_solutions(astar)
