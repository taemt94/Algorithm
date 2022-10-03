N, M = map(int, input().split())
cctv_type_num = 5
office_map = []
cctv_idxes = [None] + [[] for _ in range(cctv_type_num)]
for i in range(N):
    office_line = list(map(int, input().split()))
    office_map.append(office_line)
    for j in range(M):
        if office_line[j] != 0 and office_line[j] != 6:
            cctv_idxes[office_line[j]].append((i, j))

cctv_dxdy = [None] + [[[(-1, 0)], [(0, 1)], [(1, 0)], [(0, -1)]],
                      [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]],
                      [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(0, -1), (1, 0)], [(-1, 0), (0, -1)]],
                      [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
                      [[(-1, 0), (0, 1), (1, 0), (0, -1)]]]

def make_dxdy_pointers(cctv_num, dxdy_len):
    if cctv_num:
        pointers = []
        for i in range(dxdy_len**cctv_num):
            if i == 0:
                pointer = '0' * cctv_num        
            else:
                tmp = ''
                origin = i
                while i:
                    if origin % dxdy_len == 0:
                        tmp = str(i % dxdy_len) + tmp
                    else:
                        tmp += str(i % dxdy_len)
                    i = i // dxdy_len            
                pointer = '0' * (cctv_num - len(tmp)) + tmp
            pointers.append(tuple(map(int, pointer)))
        return pointers
    else:
        return [None]
cctv_pointers = [None] + [make_dxdy_pointers(len(cctv_idxes[i]), len(cctv_dxdy[i])) for i in range(1, cctv_type_num + 1)]

def empty_exists(i, j, dx, dy):
    if dx == 1:
        for n_i in range(i + 1, N):
            if office_map[n_i][j] == 0:
                return True
        return False
    elif dx == -1:
        for n_i in range(0, i):
            if office_map[n_i][j] == 0:
                return True
        return False
    elif dy == 1:
        if 0 in office_map[i][j+1:]:
            return True
        return False
    elif dy == -1:
        if 0 in office_map[i][:j]:
            return True
        return False
    
visited = [[False for _ in range(M)] for _ in range(N)]
def bfs(i, j, cctv, pointer):
    visited[i][j] = True    
    dxdy = cctv_dxdy[cctv][pointer]
    for dx,dy in dxdy:
        n_i, n_j = i + dx, j + dy
        if 0 <= n_i < N and 0 <= n_j < M:
            if empty_exists(i, j, dx, dy):
                while 0 <= n_i < N and 0 <= n_j < M:
                    if not visited[n_i][n_j] and office_map[n_i][n_j] != 6:
                        visited[n_i][n_j] = True
                        if office_map[n_i][n_j] == 0:
                            office_map[n_i][n_j] = '#'
                    elif office_map[n_i][n_j] == 6:
                        break
                    n_i += dx
                    n_j += dy

min_empty_num = N * M
for cctv_5 in cctv_pointers[5]:
    for cctv_4 in cctv_pointers[4]:
        for cctv_3 in cctv_pointers[3]:
            for cctv_2 in cctv_pointers[2]:
                for cctv_1 in cctv_pointers[1]:
                    if cctv_5 is not None:
                        for i, ptr in enumerate(cctv_5):
                            bfs(*cctv_idxes[5][i], 5, ptr)
                    if cctv_4 is not None:
                        for i, ptr in enumerate(cctv_4):
                            bfs(*cctv_idxes[4][i], 4, ptr)
                    if cctv_3 is not None:
                        for i, ptr in enumerate(cctv_3):
                            bfs(*cctv_idxes[3][i], 3, ptr)
                    if cctv_2 is not None:
                        for i, ptr in enumerate(cctv_2):
                            bfs(*cctv_idxes[2][i], 2, ptr)
                    if cctv_1 is not None:
                        for i, ptr in enumerate(cctv_1):
                            bfs(*cctv_idxes[1][i], 1, ptr)
                    empty_num = sum([1 for office_line in office_map
                                        for office in office_line if office == 0])
                    if empty_num < min_empty_num:
                        min_empty_num = empty_num
                    office_map = [[office_map[i][j] if office_map[i][j] != '#' else 0 for j in range(M)] for i in range(N)]
                    visited = [[False for _ in range(M)] for _ in range(N)]
print(min_empty_num)