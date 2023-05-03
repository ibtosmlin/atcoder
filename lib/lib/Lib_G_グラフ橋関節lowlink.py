#name#
# Lib_G_グラフ橋関節_lowlink
#description#
# グラフの橋・関節をO(n)で検出
#body#
#関節 https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A
#橋 https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_B
# グラフの橋・関節をO(n)で検出
import sys
sys.setrecursionlimit(10001000)

class LowLink():
    def __init__(self,G):
        self.N = len(G)
        self.G = G
        self.low = [-1] * self.N
        self.ord = [-1] * self.N

    def _dfs(self,x = 0,time = 0,p = -1):
        self.ord[x] = self.low[x] = time
        time += 1

        isArticulation = False
        cnt = 0 # 子の数
        for nx in self.G[x]:
            if self.low[nx] < 0:
                cnt += 1
                self._dfs(nx,time,x)
                self.low[x] = min(self.low[x],self.low[nx])
                if p != -1 and self.ord[x] <= self.low[nx]: isArticulation = True
                if self.ord[x] < self.low[nx]:
                    self.bridge.append((min(x,nx), max(x,nx)))
            elif nx != p:
                self.low[x] = min(self.low[x],self.ord[nx])

        if p == -1 and cnt >= 2: isArticulation = True
        if isArticulation: self.articulation.append(x)

    def build(self):
        self.articulation = []
        self.bridge = []
        self._dfs()


n, m = map(int,input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

ll = LowLink(G)
ll.build()
ret = ll.bridge
print(len(ret))
#prefix#
# Lib_G_グラフ橋関節_lowlink
#end#
