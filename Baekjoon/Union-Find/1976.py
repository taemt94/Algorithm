import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
p = [i for i in range(N + 1)]

def find(u):
        if u != p[u]:
                p[u] = find(p[u])
        return p[u]
def union(u, v):
        root1 = find(u)
        root2 = find(v)
        p[root2] = root1

for i in range(1, N + 1):
        line = list(map(int, sys.stdin.readline().split()))
        for j, l in enumerate(line):
                if l == 1:
                        union(i, j + 1)
plan = list(map(int, sys.stdin.readline().split()))
s = True
for i in range(len(plan)):
        try:
                if find(plan[i]) != find(plan[i + 1]):
                        s = False
        except:
                pass
if s:
        print("YES")
else:
        print("NO")