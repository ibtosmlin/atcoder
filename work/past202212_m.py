# https://atcoder.jp/contests/past202212-open/tasks/past202212_m
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1
from collections import deque
INF = 10 ** 9

n = int(input())
G = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int1, input().split())
    G[a].append((b, i))
    G[b].append((a, i))

dp = [-1] * n
que = deque([])
dp[0] = (INF, 0)
que.append(0)
ret = n * (n-1) // 2
while que:
    x = que.popleft()
    m, M = dp[x]
    for nx, i in G[x]:
        if dp[nx] != -1: continue
        _m = min(m, i)
        _M = max(M, i)
        dp[nx] = (_m, _M)
        que.append(nx)
        ret += (_m + 1) * (n - 1 - _M)

print(ret)
