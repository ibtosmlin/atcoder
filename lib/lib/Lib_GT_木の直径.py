#name#
# Diameter
#description#
# 木の直径
#body#
def tree_diameter(n, G):
    root = None
    lv = n.bit_length()
    _depth = [None] * n

    def _dfs(root):
        _depth = [None] * n
        q = deque()
        q.append(root)
        _depth[root] = 0
        last_node = 0
        while q:
            cur = q.popleft()
            dep = _depth[cur]
            for nxt in G[cur]:
                if type(nxt) != int: nxt, _cost = nxt
                if _depth[nxt] != None: continue
                q.append(nxt)
                _depth[nxt] = dep + 1
                last_node = nxt
        return last_node, _depth

    u, _ = _dfs(n-1)
    v, depth = _dfs(u)
    return u, v, depth

##############################


n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n-1):
    _a, _b = map(int1, input().split())
    edges[_a].append(_b)
    edges[_b].append(_a)

print(tree_diameter(n, edges))


#prefix#
# lib_GT_木の直径
#end#
