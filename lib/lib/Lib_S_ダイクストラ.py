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
class dijkstra:
    def __init__(self, n, edges):
        self.n = n              # ノード数
        self.edges = edges      # 有向グラフ
        self.prev = [-1] * n    # 前のノード
        self.start = None       # 始点

    def build(self, start):
        self.dist = [INF] * self.n
        self.dist[start] = 0
        next_q = [(0, start)]
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
n, m, t = map(int, input().split())
edges = [[] for _ in range(n)]
edges_R = [[] for _ in range(n)]    #行きと帰りを分けた（有向グラフ）場合
#リストの作成
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    edges[a].append((b,c))
    edges[b].append((a,c))
    edges_R[b].append((a,c))        #行きと帰りを分けた（有向グラフ）場合

dij = dijkstra(n, edges)  #クラスのインスタンス化
dijR = dijkstra(n, edges_R)
dij.build(0)
dijR.build(0)

dij.get(n-1)

#prefix#
# lib_s_最短経路探索_dijkstra
#end#
