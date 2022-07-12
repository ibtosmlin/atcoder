#name#
# 強連結成分分解
#description#
# 強連結成分分解(SCC): グラフgに対するSCCを行う
#body#
class SCCGraph:
    def __init__(self, n:int) -> None:
        self.n = n                          # 頂点サイズ
        self.size = None                    # 分解後連結成分数
        self.label = [None] * n             # それぞれの頂点がどの連結成分に属しているか
        self.gf = [[] for _ in range(n)]    # 順方向の有向グラフ
        self.gr = [[] for _ in range(n)]    # 逆方向の有向グラフ
        self.edges = None                   # 縮約後の辺(隣接リスト)
        self.groups = None                  # 分解後の成分のトポロジカルソート


    def add_edge(self, fm, to):
        self.gf[fm].append(to)
        self.gr[to].append(fm)


    def build(self):
        order = []
        used = [False] * self.n

        def dfs(s):
            used[s] = True
            for t in self.gf[s]:
                if not used[t]: dfs(t)
            order.append(s)
        def rdfs(s, col):
            self.label[s] = col
            used[s] = True
            for t in self.gr[s]:
                if not used[t]: rdfs(t, col)

        for s in range(n):
            if not used[s]: dfs(s)
        used = [False] * self.n
        self.size = 0
        for s in reversed(order):
            if not used[s]:
                rdfs(s, self.size)
                self.size += 1

        # 縮約後のグラフを構築
        self.edges = [set() for _ in range(self.size)]
        self.groups = [[] for _ in range(self.size)]
        for s in range(n):
            lbs = self.label[s]
            for t in self.gf[s]:
                lbt = self.label[t]
                if lbs == lbt: continue
                self.edges[lbs].add(lbt)
            self.groups[lbs].append(s)


####################################

n, m = map(int, input().split())
scc = SCCGraph(n)

for i in range(m):
    _a, _b = map(int, input().split())
    _a -= 1; _b -= 1
    scc.add_edge(_a, _b)

scc.build()

print(scc.size)
for gi in scc.groups:
    print(len(gi), *gi)

# 強連結成分分解(SCC): グラフgに対するSCCを行う
# https://hkawabata.github.io/technical-note/note/Algorithm/graph/scc.html
# 有向グラフで、互いに行き来できる連結成分を分類する
# 元の有向グラフが DAG でなくとも、そのグラフの SCC は DAG を形成する
# 作り方
# 適当に選んだ頂点から深さ優先（帰りがけ探索）し、1から番号を増やしながらラベリング：
# エッジをすべて逆向きにしたグラフを用意：
# 頂点のうち、ラベル番号が最大のものを選んでグラフ探索 → 通った頂点はすべて1つの SCC に属する：
# 未探索の頂点のうち、ラベル番号が最大のものを選んでグラフ探索 → 通った頂点はすべて1つの SCC に属する：

# https://atcoder.jp/contests/practice2/tasks/practice2_g

#prefix#
# ZZZZZZZZZZ
#end#
