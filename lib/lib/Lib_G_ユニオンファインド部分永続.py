#name#
# ユニオンファインド部分永続
#description#
# ユニオンファインド部分永続
#body#
class UnionFindPP:
    def __init__(self,N):
        INF = 10**9
        self.now = 0
        self.N = 0
        self.parent = [-1 for i in range(N)]
        self.time = [INF for i in range(N)]
        self.num = [[(0,1)] for i in range(N)]

    def find(self,t,x):
        '''
        version:tにおけるxの根を見つける
        t (any) : version
        x (int) : 要素
        return : int : 根
        '''
        while self.time[x] <= t:
            x = self.parent[x]
        return x

    def unite(self,x,y):
        '''
        x,yをつなげる
        x (int) : 要素
        y (int) : 要素
        '''
        self.now += 1
        x = self.find(self.now,x)
        y = self.find(self.now,y)

        if x == y:
            return

        if self.parent[x] > self.parent[y]:
            x,y = y,x

        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.time[y] = self.now
        self.num[x].append((self.now,-self.parent[x]))

    def same(self,t,x,y):
        '''
        version:tにおけるx,yが同じかどうかO(logN)
        t (any) : version
        x (int) : 要素
        y (int) : 要素
        return : bool : 同じかどうか
        '''
        return self.find(t,x) == self.find(t,y)

    def size(self,t,x):
        '''
        version:tにおける要素xが含まれる集合の大きさ
        t (any) : version
        x (int) : 要素
        return : int :集合の大きさ
        '''
        x = self.find(t,x)
        numx = self.num[x]
        ok = 0
        ng = len(numx)
        while (ng-ok > 1):
            mid = (ok+ng)>>1
            if numx[mid][0] <= t:
                ok = mid
            else:
                ng = mid

        return numx[ok][1]

    def time_join(self, x, y):
        '''
        x (int) : 要素
        y (int) : 要素
        return : int :同一のグループとなった時
        '''
        upper = self.now
        if not self.same(upper, x, y): return -1
        lower = 0
        while upper - lower > 1:
            mid = (upper+lower)//2
            if self.same(mid, x, y):
                upper = mid
            else:
                lower = mid
        return upper


n, m = map(int, input().split())
uf = UnionFindPP(n)

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    uf.unite(a, b)

q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    print(uf.time_join(a, b))
# https://atcoder.jp/contests/code-thanks-festival-2017/tasks/code_thanks_festival_2017_h

#prefix#
# Lib_G_unionfindPP
#end#
