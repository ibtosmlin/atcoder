# https://atcoder.jp/contests/newjudge-2308-algorithm/tasks/abc309_d
from collections import deque

def _bfs(n, G, root=0):
    _depth = [None] * n
    q = deque()
    q.append(root)
    _depth[root] = 0
    _parent = [None] * n
    last_node = root
    while q:
        cur = q.popleft()
        dep = _depth[cur]
        for nxt in G[cur]:
            if _depth[nxt] != None: continue
            q.append(nxt)
            newdep = dep + 1
            _depth[nxt] = newdep
            _parent[nxt] = cur
            last_node = nxt
    return _depth

n1, n2, m = map(int, input().split())
G = [[] for _ in range(n1+n2)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

d1 = max(i for i in _bfs(n1+n2, G, 0) if i != None)
d2 = max(i for i in _bfs(n1+n2, G, n1+n2-1) if i != None)
print(d1+d2+1)