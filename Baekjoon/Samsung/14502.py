N, M = map(int, input().split())

virus_map = []
empty_idxes = []
virus_idxes = []
for i in range(N):
    sub_map = list(map(int, input().split()))
    virus_map.append(sub_map)

    empty_idx = [(i, j) for j in range(M) if sub_map[j] == 0]
    empty_idxes.extend(empty_idx)
    virus_idx = [(i, j) for j in range(M) if sub_map[j] == 2]
    virus_idxes.extend(virus_idx)
    
wall_idxes = []
i, j, k = 0, 1, 2
while i + 2 < len(empty_idxes):
    if k < len(empty_idxes):
        wall_idxes.append([empty_idxes[i], empty_idxes[j], empty_idxes[k]])
        k += 1
    elif j < len(empty_idxes) - 1:
        j += 1
        k = j + 1
    else:
        i += 1
        j = i + 1
        k = j + 1

dx_dy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def bfs(i, j):
    Q = [(i, j)]
    while Q:
        i, j = Q.pop(0)
        for dx, dy in dx_dy:
            n_i, n_j = i + dx, j + dy
            if 0 <= n_i < N and 0 <= n_j < M:
                if virus_map[n_i][n_j] == 0:
                    virus_map[n_i][n_j] = 2
                    Q.append((n_i, n_j))

empty_max = 0
for wall_idx in wall_idxes:
    for i, j in wall_idx:
        virus_map[i][j] = 1

    for i, j in virus_idxes:
        bfs(i, j)

    empty_cnt = sum([sub_map.count(0) for sub_map in virus_map])
    if empty_cnt > empty_max:
        empty_max = empty_cnt

    for i, j in wall_idx:
        virus_map[i][j] = 0
    for i in range(N):
        for j in range(M):
            if (i, j) not in virus_idxes and virus_map[i][j] == 2:
                virus_map[i][j] = 0
print(empty_max)