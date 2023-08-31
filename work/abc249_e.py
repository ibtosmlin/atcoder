# https://atcoder.jp/contests/abc249/tasks/abc249_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1

def f(x):
    ret = 1
    while x:
        x //= 10
        ret += 1
    return ret

n, p = map(int, input().split())
lbs = [0, 1, 10, 100, 1000, 10000]

# dp[i][j]:ブロックごとにi文字目まで決めて、j文字で書ける場合の数
dp = [[0] * (n+1) for _ in range(n+1)]
for w in range(1, n+1):
    if f(w) <= n:
        dp[w][f(w)] = 26
rdp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        # for w in range(1, i):
        #     pj = j-f(w)
        #     if pj < 0: continue
        #     dp[i][j] += dp[i-w][j-f(w)] * 25
        #     dp[i][j] %= p
        for k in range(1, 5):
            fk = k + 1
            pj = j - fk
            if pj < 0: continue
            lb = lbs[k]
            ub = min(lb * 10, i)
            if lb >= ub: continue
            # for w in range(lb, ub):
            #     dp[i][j] += dp[i-w][pj] * 25
            dp[i][j] += (rdp[i-lb][pj] - rdp[i-ub][pj]) * 25
            dp[i][j] %= p

        rdp[i][j] = rdp[i-1][j] + dp[i][j]
        rdp[i][j] %= p

print(sum(dp[-1][:-1])%p)
#for dpi in dp: print(dpi[:10])
