import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

def non_colorblind_mapper(color):
    if color == 'R':
        return 0
    elif color == 'G':
        return 1
    else:
        return 2

def colorblind_mapper(color):
    if color == 'R' or color == 'G':
        return 0
    else:
        return 1

non_cb_map = []
cb_map = []
for _ in range(N):
    colors = sys.stdin.readline().strip()
    non_cb_map.append(list(map(non_colorblind_mapper, colors)))
    cb_map.append(list(map(colorblind_mapper, colors)))

non_cb_visited = [[False for _ in range(N)] for _ in range(N)]
cb_visited = [[False for _ in range(N)] for _ in range(N)]

def dfs(i, j, non_cb=True):
    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    if non_cb:
        non_cb_visited[i][j] = True
        for n_i, n_j in neighbors:
            if 0 <= n_i < N and 0 <= n_j < N:
                if non_cb_map[n_i][n_j] == non_cb_map[i][j] and not non_cb_visited[n_i][n_j]:
                    dfs(n_i, n_j, non_cb)
    else:
        cb_visited[i][j] = True
        for n_i, n_j in neighbors:
            if 0 <= n_i < N and 0 <= n_j < N:
                if cb_map[n_i][n_j] == cb_map[i][j] and not cb_visited[n_i][n_j]:
                    dfs(n_i, n_j, non_cb)        

non_cb_cnt = 0
cb_cnt = 0
for i in range(N):
    for j in range(N):
        if not non_cb_visited[i][j]:
            dfs(i, j, True)
            non_cb_cnt += 1
        if not cb_visited[i][j]:
            dfs(i, j, False)
            cb_cnt += 1

print(non_cb_cnt, cb_cnt)