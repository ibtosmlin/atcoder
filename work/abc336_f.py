# https://atcoder.jp/contests/abc336/tasks/abc336_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
from collections import deque

n, m = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(n)]
X = tuple(X[i][j] for i in range(n) for j in range(m))
Y = tuple(i for i in range(1, n*m+1))

def trans(Z, x, y):
    ret = list(Z)
    for i in range(n-1):
        for j in range(m-1):
            f = (i+x)*m+(j+y)
            g = (n-2-i+x)*m+(m-2-j+y)
            ret[g] = Z[f]
    return tuple(ret)

def bfs(Z):
    ret = dict()
    que = deque()
    ret[Z] = 0
    que.append((Z, 0))
    while que:
        U, d = que.popleft()
        for x in range(2):
            for y in range(2):
                V = trans(U, x, y)
                if V in ret: continue
                ret[V] = d + 1
                if d+1 < 10:
                    que.append((V, d+1))
    return ret

ret = 100
dx = bfs(X)
dy = bfs(Y)
for k, v in dx.items():
    if not k in dy: continue
    ret = min(ret, v+dy[k])
if ret == 100:
    ret = -1
print(ret)