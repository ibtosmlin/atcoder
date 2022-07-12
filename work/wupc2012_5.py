#name#
# ダイクストラ法
#description#
# ダイクストラ法
# 辺の重みが小さいものから、決めていく

#body#
# ダイクストラ法
# 重み付きグラフ関係により最短経路のリストを作る
# 有向グラフで優先度付きキューで探索
# https://atcoder.jp/contests/abc035/tasks/abc035_d
# O((E+V)logV)
from heapq import *
class dijkstra:
    def __init__(self, n, edges):
        self.n = n              # ノード数
        self.edges = edges      # 有向グラフ
        self.prev = [-1] * n    # 前のノード
        self.start = None       # 始点

    def build(self, start):
        self.dist = [INF] * self.n
        next_q = []
        if type(start) is int:
            start = [start]
        for st in start:
            self.dist[st] = 0
            next_q.append((0, st))
        heapify(next_q)
        while next_q:
            cd, cn = heappop(next_q)
            if self.dist[cn] < cd: continue
            for nn, nd in self.edges[cn]:
                # 変則的な距離の場合はここを調整 ##
                nd_ = self.dist[cn] + nd
                ############################
                if self.dist[nn] <= nd_: continue
                self.dist[nn] = nd_
                self.prev[nn] = cn
                if nn // 28 == n-1: continue
                heappush(next_q, (nd_, nn))


    def get_dist(self, goal):
        return self.dist[goal]


    def get_path(self, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]


##########################################

INF = float('inf')
n, m = map(int, input().split())
mxstatus = 28
edges = [[] for _ in range(n * mxstatus)]

#リストの作成
for _ in range(m):
    u, v, c = map(int, input().split())
    for i in range(mxstatus):
        fm = u*mxstatus + i
        to = v*mxstatus + ((i+c) % mxstatus)
        edges[fm].append((to, c))
        fm = v*mxstatus + i
        to = u*mxstatus + ((i+c) % mxstatus)
        edges[fm].append((to, c))
dij = dijkstra(n*mxstatus, edges)  #クラスのインスタンス化

dij.build(0)
ret = INF
for i in range(mxstatus):
    if i%4==0 or i%7==0:
        ret = min(ret, dij.get_dist((n-1)*mxstatus + i))
print(ret)