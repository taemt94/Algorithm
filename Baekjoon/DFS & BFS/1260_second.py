import sys

N, M, V = map(int, sys.stdin.readline().split())

adj_list = [None] + [[] for _ in range(N)]

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())

    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

for i in range(len(adj_list)):
    if i == 0:
        continue
    adj_list[i].sort()

visited = [None] + [False for _ in range(N)]
def dfs(V):
    visited[V] = True
    print(V, end=' ')

    for W in adj_list[V]:
        if not visited[W]:
            dfs(W)
dfs(V)
print()

visited = [None] + [False for _ in range(N)]
def bfs(V):
    Q = [V]
    visited[V] = True
    while Q:
        V = Q.pop(0)
        print(V, end=' ')
        for W in adj_list[V]:
            if not visited[W]:
                visited[W] = True
                Q.append(W)
bfs(V)