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
from heapq import heapify, heappop, heappush
class dijkstra:
    def __init__(self, n, G):
        self.INF = 10**18
        self.n = n                  # ノード数
        self.G = G                  # 有向グラフ
        self.start = None           # 始点
        self.G_used = [None] * n    # 最短経路木の親
        self.dist = [self.INF] * n  # 始点からの距離
        self.count = [0] * n        # 始点からの最短到達パス数

    def build(self, start):
        self.start = start
        self.G_used = [None] * self.n
        self.dist = [self.INF] * self.n
        self.count = [0] * self.n
        next_q = []
        if type(start) is int:
            start = [start]
        for st in start:
            self.dist[st] = 0
            self.count[st] = 1
            next_q.append((0, st))
        heapify(next_q)
        while next_q:
            d, x = heappop(next_q)
            if self.dist[x] < d: continue
            for nx, d_nx_x in self.G[x]:
                # 変則的な距離の場合はここを調整 ##
                nd = self.dist[x] + d_nx_x
                ############################
                if self.dist[nx] <= nd: continue
                self.dist[nx] = nd
                self.G_used[nx] = x
                heappush(next_q, (nd, nx))


    def get_dist(self, goal):
        # 各ノードへの最短距離
        return self.dist[goal]


    def get_count(self, goal):
        # 各ノードへの最短距離のパス数
        return self.count[goal]


    def get_path(self, goal):
        # 各ノードへの最短パス
        path = []
        node = goal
        while node != None:
            path.append(node)
            node = self.G_used[node]
        return path[::-1]

##########################################

##########################################

n, m = map(int, input().split())
A = list(map(int, input().split()))
G = [[] for _ in range(n+1)]

for i in range(n):
    G[i].append((i+1, A[i]))
    G[i+1].append((i, 0))

for _ in range(m):
    b, l, r = map(int, input().split())
    G[l-1].append((r,b))

dij = dijkstra(n+1, G)  #クラスのインスタンス化
dij.build(0)

# for i in range(n+1):
#     print(i, G[i])
print(dij.dist[-1])