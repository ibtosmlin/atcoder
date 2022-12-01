from heapq import heapify, heappop, heappush

# トポロジカルソート
# 有向非巡回グラフ（DAG）の各ノードを順序付けして、どのノードもその出力辺の先のノードより前にくるように並べることである。
# 有向非巡回グラフは必ずトポロジカルソートすることができる。
class topological_sort:
    def __init__(self, n:int, G) -> None:
        self.n = n
        self.ts = []            # トポロジカルソート
        self.parents = [-1] * n # 親 -1は根
        self.G = G              # 辺
        self.in_cnt = [0] * n   # 入力
        self.node_zero = []     # ゼロ次のノード
        for i, gi in enumerate(G):
            for j in gi:
                self.in_cnt[j] += 1
        self.node_zero = [i for i in range(self.n) if self.in_cnt[i] == 0]


    def _build_sort_by_nodeid(self) -> None:
        q = self.node_zero[:]
        heapify(q)
        while q:
            p = heappop(q)
            self.ts.append(p)
            for nxt in self.G[p]:
                self.in_cnt[nxt] -= 1
                if self.in_cnt[nxt] == 0:
                    heappush(q, nxt)
                    self.parents[nxt] = p


    def build(self, sorttype='nodeid'):
        self.ts = []            # トポロジカルソート
        if sorttype == 'appear':        # 出たとこ順番
            self._build_sort_by_appear()
        elif sorttype == 'nodeid':      # ノードの順番
            self._build_sort_by_nodeid()

    @property
    def is_dag(self) -> bool:
        return len(self.ts)==self.n
        # True 閉路なしDAG
        # False 閉路あり


#########################################
s, t = input().split('iwi')
ls = len(s)
lt = len(t)
n = max(ls, lt)
N = n*n + n
G = [[] for _ in range(N)]
isok = ['ii', 'ww', '()', ')(', '{}', '}{', '[]', '][']
nodes = []
t = t[::-1]
for j in range(t):
    for i in range(ls):
        if s[i] + s[j] in isok:
            nodes.append((i, j))

for i, j in nodes:
    for u, v in nodes:
        if i < u and v < j:
            G[n*i+j].append(n*u+v)

ts = topological_sort(N, G)

ret = [0] * N
seen = [False] * N
ts.build()
for u in ts.ts:
    seen[u] = True
    for v in G[u]:
        if seen[v]: continue
        x, y = divmod(v, n)
        if x == y:
            add = 1
        else:
            add = 2
        ret[v] = max(ret[v], ret[u] + add)

print(max(ret)+2)
