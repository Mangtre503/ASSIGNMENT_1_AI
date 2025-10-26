from collections import deque
import ast
import os


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