# https://atcoder.jp/contests/abc314/tasks/abc314_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1 = lambda x: int(x)-1

INF = 10**10
n, m = map(int, input().split())

r = []
for _ in range(n):
    c, p, *s = map(int, input().split())
    s = [si for si in s if si != 0]
    c = c * p / len(s)
    p = len(s)
    r.append((c, p, s))

dp = [INF] * (m+1)
dp[0] = 0

for i in range(m+1):
    for c, p, s in r:
        now = c
        for si in s:
            j = max(0, i - si)
            now += dp[j] / p
        dp[i] = min(dp[i], now)

print(dp[-1])
