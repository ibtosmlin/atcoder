import sys
sys.setrecursionlimit(10**6)
n = int(input())
G = [[] for _ in range(n)]
edges = []
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
    edges.append((a, b))

for x in range(n):
    if len(G[x]) == 1:
        leaf = x
        break

parent = [-1] * n
order = []

def dfs(x, p=-1):
    global parent
    parent[x] = p
    order.append(x)
    for nx in G[x]:
        if nx == p: continue
        dfs(nx, x)
    return 
dfs(leaf)

ret = [0] * n
q = int(input())
for _ in range(q):
    t, e, x = map(int, input().split())
    e -= 1
    a, b = edges[e]

    if t == 2:
        a, b = b, a
    if b == parent[a]:
        ret[a] += x
    if b != parent[a]:
        ret[leaf] += x
        ret[b] -= x

for x in order[1:]:
    ret[x] += ret[parent[x]]

print('\n'.join(map(str, ret)))

