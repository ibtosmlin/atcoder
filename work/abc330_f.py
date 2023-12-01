# https://atcoder.jp/contests/abc330/tasks/abc330_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
from bisect import bisect_right
class points_diffs:
    def __init__(self, A:list):
        self.X = sorted(A)
        self.RX = [0]
        self.N = len(A)
        for ai in self.X:
            self.RX.append(self.RX[-1] + ai)

    def cost_left(self, x):
        """
        xの左側の点をxに持ってくるコスト
        """
        u = bisect_right(self.X, x)
        return u*x - self.RX[u]

    def cost_right(self, x):
        """
        xの右側の点をxに持ってくるコスト
        """
        u = bisect_right(self.X, x)

        return self.RX[-1] - self.RX[u] - (self.N-u) * x

    def cost(self, x):
        return self.cost_left(x) + self.cost_right(x+self.d)

    def mincost(self, f):
        """xコストに関する最小値"""
        l = min(self.X)
        r = max(self.X)
        while r - l > 2:
            _l = l + (r-l)//3
            _r = r - (r-l)//3
            if f(_l) > f(_r):
                l = _l
            else:
                r = _r
        return min(f(l), f(r))

N, K = map(int, input().split())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

xc = points_diffs(X)
yc = points_diffs(Y)
xc.d = 2

def isok(d):
    xcost = xc.mincost(lambda x: xc.cost_left(x)+xc.cost_right(x+d))
    ycost = yc.mincost(lambda x: yc.cost_left(x)+yc.cost_right(x+d))
    return xcost+ycost <= K

ng = -1
ok = 10**18
while ok-ng>1:
    mid = (ok+ng)//2
    if isok(mid):
        ok = mid
    else:
        ng = mid
print(ok)
