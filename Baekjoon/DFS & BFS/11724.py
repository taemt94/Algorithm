import sys

node_num, edge_num = map(int, sys.stdin.readline().split())

visited = [False] * (node_num + 1)
graph = [[] for _ in range(node_num + 1)]
for _ in range(edge_num):
        a, b = map(int, sys.stdin.readline().split())
        graph[int(a)].append(int(b))
        graph[int(b)].append(int(a))
count = 0
def dfs(v):
        visited[v] = True
        for w in graph[v]:
                if not visited[w]:
                        dfs(w)

for i in range(1, node_num + 1):
        if not visited[i]:
                dfs(i)
                count += 1
print(count)