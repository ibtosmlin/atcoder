# https://atcoder.jp/contests/abc317/tasks/abc317_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1
INF = 10**18

n = int(input())
E = []
N = 0
for _ in range(n):
    x, y, z = map(int, input().split())
    need = max(0, (x+y) - (x+y) // 2 - x)
    E.append((need, z))
    N += z

dp = [INF] * (N+1)
# dp[k] k議席を得るのに必要なコスト
dp[0] = 0

for c, z in E:
    ndp = [INF] * (N+1)
    for i in range(N+1):
        ndp[i] = min(ndp[i], dp[i])
        if i+z <= N:
            ndp[i+z] = min(ndp[i+z], dp[i] + c)
    dp = ndp

ret = INF
for i in range(N//2+1, N+1):
    ret = min(ret, dp[i])
print(ret)



