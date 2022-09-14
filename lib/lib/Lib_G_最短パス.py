#name#
# Graph最短パス
#description#
# Graph最短パス
#body#

from collections import deque


def bfs(n, G, root=0, cost=1):
    _depth = [None] * n
    q = deque()
    q.append(root)
    _depth[root] = 0
    _parent = [-1] * n
    while q:
        cur = q.popleft()
        dep = _depth[cur]
        for nxt in G[cur]:
            if type(nxt) != int: nxt, cost = nxt
            if _depth[nxt] != None: continue
            q.append(nxt)
            _parend[nxt] = cur
            _depth[nxt] = newdep
            if newdep > farest_dist:
                farest_dist = newdep
                farest_node = nxt
    return farest_node, farest_dist, _depth




##############################


n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1
    G[a].append((b, w))
    G[b].append((a, w))



#prefix#
# Lib_G_最短パス
#end#
