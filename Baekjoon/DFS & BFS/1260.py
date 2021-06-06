import sys

nodes = []
for line in sys.stdin:
        line = line.split()
        for i, w in enumerate(line):
                line[i] = int(w)
        nodes.append(line)
node_num, edge_num, start = nodes.pop(0)
visited = [False] * (node_num + 1)

def dfs(v):
        if visited[v]:
                return
        visited[v] = True
        print(v, end=' ')
        neighbors = []
        for a, b in nodes:
                if a == v:
                        neighbors.append(b)
                elif b == v:
                        neighbors.append(a)
        neighbors.sort()
        for n in neighbors:
                dfs(n)

def bfs(v):
        queue = []
        queue.append(v)
        
        while True:
                if len(queue) == 0:
                        break
                n = queue.pop(0)
                if visited[n]:
                        continue

                visited[n] = True
                
                print(n, end=' ')
                neighbors = []
                for a, b in nodes:
                        if a == n:
                                neighbors.append(b)
                        elif b == n:
                                neighbors.append(a)
                neighbors.sort()
                queue.extend(neighbors)
                
dfs(start)
print()
visited = [False] * (node_num + 1)
bfs(start)