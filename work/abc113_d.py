# https://atcoder.jp/contests/abc113/tasks/abc113_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1
mod = 1000000007

h, w, k = map(int, input().split())
state = set()
for i in range(1<<(w-1)):
    isok = True
    for j in range(w-2):
        if i >> j & 1 and i >> (j+1) & 1:
            isok = False
            break
    if isok: state.add(i)

dp = [[0] * w for _ in range(h+1)]
dp[0][0] = 1
for i in range(h):
    for s in state:
        for x in range(w):
            # x -> x+1
            if x < w and s >> x & 1:
                dp[i+1][x+1] += dp[i][x]
                dp[i+1][x+1] %= mod
            # x -> x-1
            elif x > 0 and s >> (x-1) & 1:
                dp[i+1][x-1] += dp[i][x]
                dp[i+1][x-1] %= mod
            else:
                dp[i+1][x] += dp[i][x]
                dp[i+1][x] %= mod

print(dp[i+1][k-1])