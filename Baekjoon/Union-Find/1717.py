import sys
n, m = map(int, sys.stdin.readline().split())
p = [i for i in range(n + 1)]

def find(u):
        if u != p[u]:
                p[u] = find(p[u])
        return p[u]

def union(u, v):
        root1 = find(u)
        root2 = find(v)
        p[root2] = root1

for _ in range(m):
        line = list(map(int, sys.stdin.readline().split()))
        if line[0] == 0:
                union(line[1], line[2])
        elif line[0] == 1:
                if find(line[1]) == find(line[2]):
                        print("YES")
                else:
                        print("NO")