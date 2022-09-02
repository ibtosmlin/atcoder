#name#
# 強連結成分分解
#description#
# 強連結成分分解(SCC): グラフgに対するSCCを行う
#body#
class SCCGraph:
    def __init__(self, N):
        self.N = N
        self.edges = []
        self.ef = [[] for _ in range(N)]
        self.er = [[] for _ in range(N)]

    def csr(self):
        self.start = [0]*(self.N+1)
        self.elist = [0]*len(self.edges)
        for e in self.edges:
            self.start[e[0]+1] += 1
        for i in range(1, self.N+1):
            self.start[i] += self.start[i-1]
        counter = self.start[:]
        for e in self.edges:
            self.elist[counter[e[0]]] = e[1]
            counter[e[0]] += 1

    def add_edge(self, v, w):
        self.edges.append((v, w))
        self.ef[v].append(w)
        self.er[w].append(v)

    def scc_ids(self):
        self.csr()
        N = self.N
        now_ord = group_num = 0
        visited = []
        low = [0]*N
        order = [-1]*N
        ids = [0]*N
        parent = [-1]*N
        stack = []
        for i in range(N):
            if order[i] == -1:
                stack.append(i)
                stack.append(i)
                while stack:
                    v = stack.pop()
                    if order[v] == -1:
                        low[v] = order[v] = now_ord
                        now_ord += 1
                        visited.append(v)
                        for i in range(self.start[v], self.start[v+1]):
                            to = self.elist[i]
                            if order[to] == -1:
                                stack.append(to)
                                stack.append(to)
                                parent[to] = v
                            else:
                                low[v] = min(low[v], order[to])
                    else:
                        if low[v] == order[v]:
                            while True:
                                u = visited.pop()
                                order[u] = N
                                ids[u] = group_num
                                if u == v:
                                    break
                            group_num += 1
                        if parent[v] != -1:
                            low[parent[v]] = min(low[parent[v]], low[v])
        for i, x in enumerate(ids):
            ids[i] = group_num-1-x

        return group_num, ids

    def scc(self):
        group_num, ids = self.scc_ids()
        groups = [[] for _ in range(group_num)]
        for i, x in enumerate(ids):
            groups[x].append(i)
        return groups

####################################

n, m = map(int, input().split())
scc = SCCGraph(n)

for i in range(m):
    _a, _b = map(int, input().split())
    _a -= 1; _b -= 1
    scc.add_edge(_a, _b)

#print(scc.scc_ids())
#(3,_[0,_1,_1,_1,_2])
#print(scc.scc())
#[[0],_[1,_2,_3],_[4]]

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
# lib_G_強連結成分分解_SCC
#end#
