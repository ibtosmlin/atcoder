#name#
# Graph二部グラフ
#description#
# Graph二部グラフ
#body#

import sys
sys.setrecursionlimit(10**9)

######################################
# 二部グラフ(bipartite graph)
# 頂点集合を2つに分割して各部分の頂点は互いに隣接しないようにできるグラフ
# ノード2色を塗って、辺の両端は異なるようにできるか
######################################


######################################
# 再帰版
######################################
def is_bipartite(g):
    # 深さ優先探索
    def dfs(g,v,c):
        color[v] = c    # 色を塗る
        for nv in g[v]: # 次のノードの探索
            # すでに隣接の色が確定していて同じ色となっている場合終了
            if color[nv] == c: return False
            # 未確定の倍は反転させた色を塗って探索した結果を受け取る
            if color[nv] == 0 and not dfs(g,nv,1-c): return False
        return True

    color = [0] * n     # 0:未確定 1:黒 -1:白
    ret = dfs(g, 0, 1)
    return ret, color

#######################################

######################################
# 非再帰版
######################################
def is_bipartite(g):
    # 深さ優先探索
    color = [0] * n     # 0:未確定 1:黒 -1:白
    q = [(0, 1)]
    while q:
        v, c = q.pop()
        color[v] = c    # 色を塗る
        for nv in g[v]: # 次のノードの探索
            # すでに隣接の色が確定していて同じ色となっている場合終了
            if color[nv] == c: return False, color
            # 未確定の倍は反転させた色でキューに入れる
            if color[nv] == 0:
                q.append((nv, 1-c))
    return True, color


#######################################



n, m = map(int, input().split())
graph = [[] for _ in range(n)]

# 隣接リストの作成
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

print(is_bipartite(graph))

#prefix#
# Lib_G_二部グラフ_bipartite
#end#
