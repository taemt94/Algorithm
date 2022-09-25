import sys

N = int(sys.stdin.readline())
home_map = []
for _ in range(N):
    sub_map = list(map(int, sys.stdin.readline().strip()))
    home_map.append(sub_map)

visited = [[False for _ in range(N)] for _ in range(N)]
def dfs(i, j):
    visited[i][j] = True
    
    neighbor_idx = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    for n_i, n_j in neighbor_idx:
        if 0 <= n_i < N and 0 <= n_j < N:
            if home_map[n_i][n_j] and not visited[n_i][n_j]:
                dfs(n_i, n_j)

home_cnt_list = []
for i in range(N):
    for j in range(N):
        if not home_map[i][j]:
            continue
        if not visited[i][j]:
            dfs(i, j)
            home_cnt = sum([sum(v) for v in visited])
            if not home_cnt_list:
                home_cnt_list.append(home_cnt)
            else:
                home_cnt_list.append(home_cnt - sum(home_cnt_list))
home_cnt_list.sort()
print(len(home_cnt_list))
[print(cnt) for cnt in home_cnt_list]