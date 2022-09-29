import sys

R, C = map(int, sys.stdin.readline().split())

board = []
alphabet_set = set()
for _ in range(R):
    alphabets = list(map(str, sys.stdin.readline().strip()))
    board.append(alphabets)
    alphabet_set.update(alphabets)

alphabet_map = {alphabet: i for i, alphabet in enumerate(alphabet_set)}
def mapper(alphabet_list):
    return [alphabet_map[alphabet] for alphabet in alphabet_list]
board = list(map(mapper, board))

visited_max_len = 0
visited = [False for _ in range(len(alphabet_set))]
def dfs(i, j):
    global visited, visited_max_len
    visited[board[i][j]] = True
    
    neighbor_idxes = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]
    visit_fail_cnt = 0
    for n_i, n_j in neighbor_idxes:
        if 0 <= n_i < R and 0 <= n_j < C:
            if not visited[board[n_i][n_j]]:
                dfs(n_i, n_j)
            else:
                visit_fail_cnt += 1
        else:
            visit_fail_cnt += 1
    
    if visit_fail_cnt == len(neighbor_idxes):
        if sum(visited) > visited_max_len:
            visited_max_len = sum(visited)
    visited[board[i][j]] = False

dfs(0, 0)
print(visited_max_len)


# ### 공부해놓으면 좋을 코드
# import sys

# input = sys.stdin.readline
# r, c = map(int, input().split())
# graph = [list(input().rstrip()) for _ in range(r)]
# result = 0

# visited = [False] * 26
# start_char = ord(graph[0][0]) - ord('A')
# visited[start_char] = True

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def dfs(x, y, depth):
#     global result
#     if result < depth:
#         result = depth
#     for d in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]
#         if 0 <= nx < r and 0 <= ny < c:
#             next_char = ord(graph[nx][ny]) - ord('A')
#             if not visited[next_char]:
#                 visited[next_char] = True
#                 dfs(nx, ny, depth + 1)
#                 visited[next_char] = False

# dfs(0, 0, 1)
# print(result)