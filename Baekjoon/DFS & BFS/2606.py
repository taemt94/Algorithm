import sys

node_num = int(sys.stdin.readline())
edge_num = int(sys.stdin.readline())

adj_list = [None] + [[] for _ in range(node_num)]
for _ in range(edge_num):
    n1, n2 = map(int, sys.stdin.readline().split())
    
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

st_node = 1
visited = [None] + [False for _ in range(node_num)]
def bfs(node):
    visited[node] = True
    Q = [node]
    while Q:
        node = Q.pop(0)
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                Q.append(neighbor)
bfs(st_node)
visited_num = sum(visited[2:])
print(visited_num)