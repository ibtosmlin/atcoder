# https://atcoder.jp/contests/abc327/tasks/abc327_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
P = list(map(int, input().split()))
pwr = [0]
for i in range(n+1):
    l = pwr[-1] * 0.9
    l += 1
    pwr.append(l)

# dp[i] :i個までみてk個選んだ時の最大値 Σ(0.9)*(k-i) * qi
dp = [[-1] * (n+1) for _ in range(n+1)]
dp[0][0] = 0

for i, p in enumerate(P):
    for j in range(n+1):
        if dp[i][j] == -1: continue
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if j+1 <= n:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]*0.9 + p)

ret = -10**10
for k in range(1, n+1):
    ret = max(ret, dp[-1][k] / pwr[k] - 1200/(k**0.5))

def fstr(x): return f'{x:.15f}'

print(fstr(ret))
