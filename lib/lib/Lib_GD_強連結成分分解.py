#name#
# 強連結成分分解
#description#
# 強連結成分分解(SCC): グラフgに対するSCCを行う
#body#
class SCCGraph:
    def __init__(self, N):
        self.N = N
        self.edges = []
        self.ef, self.er = [[] for _ in range(N)], [[] for _ in range(N)]

    def add_edge(self, v, w):
        self.edges.append((v, w))
        self.ef[v].append(w)
        self.er[w].append(v)

    def scc_group(self):
        N = self.N
        group = [None] * N
        visited = [False] * N
        order = []
        for x in range(N):
            if visited[x]: continue
            stack = [x]
            visited[x] = True
            while stack:
                y = stack.pop()
                movable = False
                for ny in self.ef[y]:
                    if visited[ny]: continue
                    movable = True
                    visited[ny] = True
                    stack.append(y)
                    stack.append(ny)
                    break
                if not movable: order.append(y)
        visited = [False] * N
        count = 0
        for x in order[::-1]:
            if visited[x]: continue
            stack = [x]
            group[x] = count
            while stack:
                y = stack.pop()
                visited[y] = 1
                for ny in self.er[y]:
                    if visited[ny]: continue
                    group[ny] = count
                    stack.append(ny)
            count += 1
        return count, group

    def scc(self):
        count, group = self.scc_group()
        groups = [[] for _ in range(count)]
        for i, x in enumerate(group):
            groups[x].append(i)
        return groups

####################################

n, m = map(int, input().split())
scc = SCCGraph(n)

for i in range(m):
    _a, _b = map(int, input().split())
#    _a -= 1; _b -= 1
    scc.add_edge(_a, _b)

_, gr = scc.scc_group()
for _ in range(int(input())):
    u, v = map(int, input().split())
    print(int(gr[u] == gr[v]))

# print(scc.scc_group())
#(3,_[0,_1,_1,_1,_2])
# print(scc.scc())
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
# Lib_GD_強連結成分分解_SCC
#end#
