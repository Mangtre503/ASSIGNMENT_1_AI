""" Utility functions for Sokoban project """
import os
import ast

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
    os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    file_path = os.path.join('SokobanMap', testcase)
    with open(file_path, 'r', encoding='utf-8') as f:
        board = ast.literal_eval(f.read())  

    h = len(board)  # num of rows
    w = len(board[0])  # num of columns

    walls, goals, boxes = set(), set(), set()
    player = None

    for r in range(h):
        for c in range(w):
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
    return h, w, walls, goals, frozenset(boxes), player

def is_inside(r, c, h, w):
    '''
    check if coordinate (r,c) is valid in this board (H,W)
    '''
    return 0 <= r < h and 0 <= c < w

def is_free(cell, walls, boxes, h, w):
    '''
    cell: (x, y)
    check if current cell is empty (not wall, not box) and its coordinates are valid
    '''
    return is_inside(*cell, h, w) and (cell not in walls) and (cell not in boxes)

def goal_test(boxes, goals):
    '''
    check if all boxes on targets (finish)
    '''
    for box in boxes:
        if box not in goals:
            return False
    return True

def neighbors(state, walls, h, w):
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

        # Nếu đụng tường hoặc ra ngoài biên -> loại
        if not is_inside(nr, nc, h, w) or nxt in walls:
            continue

        if nxt in boxes: # Nếu bước kế tiếp là đẩy thùng
            # Nếu ô sau thùng trống -> step hợp lệ, ngược lại bỏ qua
            br, bc = nr + dr, nc + dc
            beyond = (br, bc)
            if is_free(beyond, walls, boxes, h, w):
                new_boxes = set(boxes)
                new_boxes.remove(nxt)
                new_boxes.add(beyond)
                res.append(((nxt, frozenset(new_boxes)), m))
        else:
            # Ô trước mặt trống -> bước bình thường
            res.append(((nxt, boxes), m))
    return res
'''
prioritiy queue sử dụng hàm đánh giá f(n) = g(n) + h(n)
    - g(n): chi phí từ trạng thái bắt đầu đến trạng thái n (số bước đã đi)
    - h(n): hàm heuristic ước lượng chi phí từ trạng thái n đến trạng thái mục tiêu
'''
def compute_heuristic(boxes, goals):
    """
    Heuristic: sum of Manhattan distances from each box to the nearest unmatched goal.
    """
    total_distance = 0
    unused_goals = set(goals)

    for box in boxes:
        nearest_goal = min(unused_goals, key=lambda g: abs(box[0]-g[0]) + abs(box[1]-g[1]))
        dist = abs(box[0] - nearest_goal[0]) + abs(box[1] - nearest_goal[1])
        total_distance += dist
        unused_goals.remove(nearest_goal)

    return total_distance

# def compute_heuristic(boxes, goals):
#     """
#     Approximate heuristic: sum of Manhattan distances from each box
#     to the closest goal (ignoring whether goal is already matched).
#     Faster but may overestimate slightly if multiple boxes share the same goal.
#     """
#     total_distance = 0

#     for box in boxes:
#         # Chọn khoảng cách nhỏ nhất từ box tới tất cả các goals
#         nearest_dist = min(abs(box[0]-g[0]) + abs(box[1]-g[1]) for g in goals)
#         total_distance += nearest_dist

#     return total_distance



def build_solutions(func):
    """ Build solutions for testcases using the provided function: bfs or astar """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if func.__name__ == "bfs":
        solutions_dir = os.path.join(current_dir, 'BlindSearch', "solutions")
    else:
        solutions_dir = os.path.join(current_dir, 'Heuristic', "solutions")
    os.makedirs(solutions_dir, exist_ok=True)

    for i in range(1, 21):
        tc_file = f"mini_cosmos_{i}.txt"
        result_file_path = os.path.join(solutions_dir, f"testcase_{i}.txt")
        with open(result_file_path, "w", encoding='utf-8') as file:
            result = func(tc_file)
            file.write(result)
