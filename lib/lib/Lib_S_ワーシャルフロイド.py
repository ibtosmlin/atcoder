#name#
# ワーシャルフロイド法
#discription#
# 全頂点間最短路
# d[i][j]は2頂点間i, j間の移動コストを格納, Mは頂点数
# O(N^3)
#body#
import copy

class warshall_floyd:
    def __init__(self, n:int) -> None:
        self.INF = float("inf")
        self.n = n
        self.d = [[self.INF] * n for _ in range(n)]
        #d[u][v] : 辺uvのコスト(存在しないときはinf)
        for i in range(n):
            self.d[i][i] = 0 #自身のところに行くコストは０



    def build(self):
        n = self.n
        wf = copy.deepcopy(self.d)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    wf[i][j] = min(wf[i][j], wf[i][k] + wf[k][j])

        self.wf = wf #wf[i][j]に頂点i, j間の最短距離を格納


    def add_edge(self, fm, to, cost):
        self.d[fm][to] = cost


    # 負値閉路検索
    @property
    def is_neg_cycle(self) -> bool:
        for i in range(self.n):
            if self.wf[i][i] < 0:
                return True
        return False


    # 経路復元
    def path(self, s, g):
        ret = []
        if s == g or self.wf[s][g] == self.INF:
            return ret
        cur = s
        while cur!=g:
            for nxt in range(self.n):
                if nxt==cur or nxt==s: continue
                if self.d[cur][nxt] + self.wf[nxt][g] == self.wf[cur][g]:
                    ret.append((cur, nxt))
    #                ret.append((nxt, cur))
                    cur = nxt
                    break
        return ret

##############################

n, m = map(int,input().split()) #N:頂点数 m:辺の数

WF = warshall_floyd(n)

for _ in range(m):
    _u, _v, _w = map(int,input().split())
    _u -= 1; _v -= 1
    WF.add_edge(_u, _v, _w)
    WF.add_edge(_v, _u, _w)

WF.build()

print(WF.path(0, n-1))

#prefix#
# Lib_S_最短経路探索_warshall
#end#
