from collections import deque
import ast
import os
import heapq
from . import utils

# Blind Search
DIRS = {
    'U': (-1, 0), # move upper (row decreases, column unchanged)
    'D': ( 1, 0), # move down
    'L': ( 0,-1), # move left
    'R': ( 0, 1), # move right
}

def parse_board(testcase):
    """
    Input: testcase filename
    Output:
        H: Num of rows
        W: Num of columns
        wall: List of wall
        goals: List of goal
        frozenset: List of box
        player: Coordinate of people
    Symbols:
      '#': wall
      '.': target
      '$': box
      '@': player
      '*': box on target
      '+': player on target
      ' ': free space
    """
    os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
    file_path = os.path.join('SokobanMap', testcase)
    with open(file_path, 'r') as f:
        board = ast.literal_eval(f.read())  

    H = len(board)  # num of rows
    W = len(board[0])  # num of columns

    walls, goals, boxes = set(), set(), set()
    player = None

    for r in range(H):
        for c in range(W):
            ch = board[r][c]
            if ch == '#':
                walls.add((r, c))  # tường
            elif ch == '.':
                goals.add((r, c))  #  đích
            elif ch == '$':
                boxes.add((r, c))  # thùng
            elif ch == '@':
                player = (r, c)  # Ghi nhận vị trí người chơi
            elif ch == '*':  # Thùng trên đích
                goals.add((r, c))
                boxes.add((r, c))
            elif ch == '+':  # Người chơi trên đích
                goals.add((r, c))
                player = (r, c)

    return H, W, walls, goals, frozenset(boxes), player

def is_inside(r, c, H, W):
    '''
    check if coordinate (r,c) is valid in this board (H,W)
    '''
    return 0 <= r < H and 0 <= c < W

def is_free(cell, walls, boxes, H, W):
    '''
    cell: (x, y)
    check if current cell is empty (not wall, not box) and its coordinates are valid
    '''
    return is_inside(*cell, H, W) and (cell not in walls) and (cell not in boxes)

def goal_test(boxes, goals):
    '''
    check if all boxes on targets (finish)
    '''
    for box in boxes:
        if box not in goals:
            return False
    return True

def neighbors(state, walls, goals, H, W):
    """
    Sinh các trạng thái kề: (player, boxes), cùng với ký tự move ('UDLR')
    Quy tắc:
      - Nếu ô trước mặt trống => di chuyển thường.
      - Nếu ô trước mặt có thùng và ô sau thùng trống => đẩy thùng.
    """
    player, boxes = state
    res = []
    for m, (dr, dc) in DIRS.items():
        nr, nc = player[0] + dr, player[1] + dc
        nxt = (nr, nc)

        # Nếu đụng tường -> bỏ
        if not is_inside(nr, nc, H, W) or nxt in walls:
            continue

        if nxt in boxes:
            # Ô sau thùng
            br, bc = nr + dr, nc + dc
            beyond = (br, bc)
            if is_free(beyond, walls, boxes, H, W):
                # Hợp lệ để đẩy
                new_boxes = set(boxes)
                new_boxes.remove(nxt)
                new_boxes.add(beyond)
                res.append(((nxt, frozenset(new_boxes)), m))
        else:
            # Ô trước mặt trống -> bước bình thường
            res.append(((nxt, boxes), m))
    return res

def bfs(testcase):
    """
    return sequence of action, eg: ULLRU
    or None if there is no solution
    """
    H, W, walls, goals, boxes0, player0 = parse_board(testcase)
    start = (player0, boxes0)
    if goal_test(boxes0, goals):
        return ""

    q = deque([start])
    visited = set([(player0, boxes0)])
    parent = {start: (None, None)}  # state -> (prev_state, move_char)

    while q:
        cur = q.popleft()
        player, boxes = cur

        for nxt, move_ch in neighbors(cur, walls, goals, H, W):
            if nxt in visited:
                continue
            visited.add(nxt)
            parent[nxt] = (cur, move_ch)

            _, boxes_n = nxt
            if goal_test(boxes_n, goals):
                # reconstruct path
                path_moves = []
                s = nxt
                while parent[s][0] is not None:
                    prev, ch = parent[s]
                    path_moves.append(ch)
                    s = prev
                return "".join(reversed(path_moves))
            q.append(nxt)

    return None

def build_solutions():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    solutions_dir = os.path.join(current_dir, "solutions")
    os.makedirs(solutions_dir, exist_ok=True)

    for i in range(1, 21):
        tc_file = f"mini_cosmos_{i}.txt"
        
        result_file_path = os.path.join(solutions_dir, f"testcase_{i}.txt")
        
        with open(result_file_path, "w") as file:
            result = bfs(tc_file)  
            file.write(result) 


#Solve the sokoban problem using heuristic search (A* Search)
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
    g_val={start:0} # keep track of g(n) values for each state
    queue=[]
    g_start=0
    f_start=g_start+compute_heuristic(boxes0, goals)
    heapq.heappush(queue, (f_start, g_start, start)) # push the initial state into the priority queue with f(0)=h(0)
    
    while not queue:
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
        # second, get all next possible states
        for state_neighbor, move_char in utils.neighbors(state_current, walls, h, w):
            g_neighbor=g_current+1 # cost from current state to the neighbor state
            if state_neighbor not in g_val or g_neighbor<g_val[state_neighbor]:
                g_val[state_neighbor]=g_neighbor
                parent[state_neighbor]=(state_current, move_char)
            _, boxes_neighbor = state_neighbor
            f_neighbor=g_neighbor+compute_heuristic(boxes_neighbor, goals)
            heapq.heappush(queue, (f_neighbor, g_neighbor, state_neighbor)) # push the next state into the priority queue with f(n)=g(n)+h(n)
    return None