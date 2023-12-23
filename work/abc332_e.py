# https://atcoder.jp/contests/abc332/tasks/abc332_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

import sys
def input(): return sys.stdin.readline().rstrip()

N, D = map(int, input().split())
W = list(map(int, input().split()))
INF = 10**19
AL = 1<<N
bs = [0] * AL
dp = [0] * AL

for s in range(AL):
    c = 0
    for i in range(N):
        if s >> i & 1: c += W[i]
    c **= 2
    dp[s] = bs[s] = c

for i in range(D-1):
    ndp = [INF] * AL
    for s in range(1, AL):
        t = s
        while t:
            t = (t-1) & s
            ndp[s] = min(ndp[s], dp[s^t] + bs[t])
    dp = ndp

ret = (dp[-1] * D - sum(W) ** 2 ) / D ** 2
print(ret)
mat