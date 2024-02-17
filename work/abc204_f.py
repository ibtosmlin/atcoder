# https://atcoder.jp/contests/abc204/tasks/abc204_f
import sys; input: lambda _: sys.stdin.readline().rstrip()

def matprod(ma, mb, mod = 10**9+7):
    h_a = len(ma)
    w_a = len(ma[0])
    h_b = len(mb)
    w_b = len(mb[0])
    if h_a*w_a*h_b*w_b == 0: return 0
    if w_a != h_b: return 0
    ret = [[0] * h_a for _ in range(w_b)]
    for i, reti in enumerate(ret):
        for k, aik in enumerate(ma[i]):
            for j, bkj in enumerate(mb[k]):
                reti[j] += aik * bkj
                reti[j] %= mod
    return ret


def matpow(ma, k, mod = 10**9+7):
    n = len(ma)
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        ret[i][i] = 1
    for _ in range(k):
        if k & 1:
            ret = matprod(ret, ma, mod)
        ma = matprod(ma, ma, mod)
        k >>= 1
        if k == 0: break
    return ret


H, W = map(int, input().split())
N = 1 << H
A = [[0] * N for _ in range(N)]

cnt = [0] * N
for i in range(N):
    dp = [0] * (H+1)
    dp[0] = 1
    for j in range(H):
        dp[j+1] += dp[j]
        if j < H-1 and i >> j & 1 == 0 and i >> (j+1) & 1 == 0:
            dp[j+2] += dp[j]
    cnt[i] = dp[-1]

for i in range(N):
    for j in range(N):
        if i & j: continue
        A[i][j] = cnt[i|j]

print(matpow(A, W, 998244353)[0][0])