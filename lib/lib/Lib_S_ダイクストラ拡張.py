#!/usr/bin python3
# -*- coding: utf-8 -*-

# 拡張ダイクストラ法
# 重み付きグラフ関係により最短経路のリストを作る
# 有向グラフで優先度付きキューで探索
# https://atcoder.jp/contests/abc164/tasks/abc164_e
# O((E+V)logV)

from heapq import heapify, heappop, heappush, heappushpop

INF = float('inf')

class dijkstra:
    def __init__(self, n, edges):
        self.n = n              # ノード数
        self.edges = edges      # 有向グラフ
        self.prev = [-1] * n    # 前のノード

    def build(self, start):
        self.dist = [INF] * self.n
        self.dist[start] = 0
        next_q = [(0, start)]
        heapify(next_q)
        while next_q:
            cd, cn = heappop(next_q)
            pos, coin = divmod(cn, mxstatus)
            chc, chd = chcost[pos]
            # コイン換金のパス
            if coin+chc<mxstatus:
                nn = cn+chc
                nd_ = self.dist[cn] + chd
                if self.dist[nn] > nd_:
                    self.dist[nn] = nd_
                    self.prev[nn] = cn
                    heappush(next_q, (nd_, nn))
            # 移動のパス
            if self.dist[cn] < cd: continue
            for np, na, nb in self.edges[pos]:
            # 変則的な距離の場合はここを調整 ##
                if coin - na < 0: continue
                nd_ = self.dist[cn] + nb
                nn = np*mxstatus + coin - na
            ############################
                if self.dist[nn] > nd_:
                    self.dist[nn] = nd_
                    self.prev[nn] = cn
                    heappush(next_q, (nd_, nn))
        return self.dist

    def shortest_distance(self, goal):
        return self.dist[goal]

    def shortest_path(self, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]


##########################################

n, m, s = map(int, input().split())
mxstatus = 3000
s = min(s, mxstatus-1)
edges_F = [[] for _ in range(n)]
#リストの作成
for _ in range(m):
    u, v, a, b = map(int, input().split())
    u, v = u-1, v-1

    edges_F[u].append((v,a,b))
    edges_F[v].append((u,a,b))


chcost = [tuple(map(int, input().split())) for _ in range(n)]


dijF = dijkstra(n*mxstatus, edges_F)  #クラスのインスタンス化
F = dijF.build(s)

for pos in range(1, n):
    ret = INF
    for coin in range(mxstatus):
        ret = min(ret, F[coin+mxstatus*pos])
    print(ret)