#name#
# Diameter
#description#
# 木の直径
#body#

from collections import deque


def _dfs(n, G, root=0, cost=1):
    _depth = [None] * n
    q = deque()
    q.append(root)
    _depth[root] = 0
    farest_dist = 0
    farest_node = 0
    while q:
        cur = q.popleft()
        dep = _depth[cur]
        for nxt in G[cur]:
            if type(nxt) != int: nxt, cost = nxt
            if _depth[nxt] != None: continue
            q.append(nxt)
            newdep = dep + cost
            _depth[nxt] = newdep
            if newdep > farest_dist:
                farest_dist = newdep
                farest_node = nxt
    return farest_node, farest_dist, _depth


def tree_diameter(n, G, cost=1):
    u, _, __ = _dfs(n, G, 0)
    v, diam, depth = _dfs(n, G, u)
    return u, v, diam, depth


def tree_heights(n, G, cost=1):
    u, _, __ = _dfs(n, G, 0)
    v, _, depthu = _dfs(n, G, u)
    _, __, depthv = _dfs(n, G, v)
    return [max(x, y) for x, y in zip(depthu, depthv)]


##############################


n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1
    G[a].append((b, w))
    G[b].append((a, w))

print(tree_diameter(n, G))
print(tree_heights(n, G))


#prefix#
# lib_GT_木の直径
#end#
