from collections import deque


def is_blocked(board, cell):
    x = cell[0]
    y = cell[1]

    if board[x][y] == '#':
        return True

    return False


def solve_puzzle(board, source, destination):
    m = len(board)
    n = len(board[0])

    if is_blocked(board, source) or is_blocked(board, destination):
        return None

    # initialize queue and visited set
    queue = deque()
    queue.append((source, [source], ''))
    visited = {source}

    # list of legal moves
    moves = {(-1, 0): 'U', (1, 0): 'D', (0, -1): 'L', (0, 1): 'R'}

    while len(queue) > 0:
        curr_cell, path, directions = queue.popleft()

        if curr_cell == destination:
            return path, directions

        for dx, dy in moves:
            new_x = curr_cell[0] + dx
            new_y = curr_cell[1] + dy
            if 0 <= new_x < m and 0 <= new_y < n:
                neighbor = (new_x, new_y)
                if board[new_x][new_y] != '#' and neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    new_directions = directions + moves[(dx, dy)]
                    queue.append((neighbor, new_path, new_directions))

    return None


example_board = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]
print(solve_puzzle(example_board, (0, 2), (2, 2)))
