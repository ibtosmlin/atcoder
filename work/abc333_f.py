# https://atcoder.jp/contests/abc333/tasks/abc333_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
mod = 998244353
invh = pow(2, -1, mod)
invhseq = [1]
for i in range(3010):
    invhseq.append(invhseq[-1]*invh%mod)

divseq = [0]
for i in range(1, 3010):
    divseq.append(pow(1 - invhseq[i], -1, mod))

def calc(n):
    # n = int(input())
    dp = [[0]*n for _ in range(n+1)]
    dp[1][0] = 1
    dp[1][1] = 0
    for i in range(2, n+1):
        u = 0
        for j in range(i):
            u += dp[i-1][j] * invhseq[i-j-1]
            u %= mod
        u = ((u * invh) % mod) * divseq[i] % mod
        dp[i][0] = u
        for j in range(1, i):
            dp[i][j] = (dp[i-1][j-1] + dp[i][j-1]) * invh % mod

    print(*dp[-1])

calc(int(input()))