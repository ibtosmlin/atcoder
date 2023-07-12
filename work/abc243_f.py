# https://atcoder.jp/contests/abc243/tasks/abc243_f
mod = 998244353
lim = 100                   # mod素数, 出力の制限
g1, g2 = [[1]*(lim+1) for _ in range(2)]    # ！と逆元tbl
for i in range(2, lim + 1):
    g1[i] = g1[i-1] * i % mod
g2[-1] = pow(g1[-1], mod-2, mod)
for i in range(lim, 0, -1):
    g2[i-1] = g2[i] * i % mod

def fac(n): return g1[n]
def facinv(n): return g2[n]
def nCr(n, r):
    """nCr
    n個のものからr個選ぶ
    """
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return fac(n) * facinv(r) * facinv(n-r) % mod

def modinv(x, mod): return pow(x, mod - 2, mod)

N, M, K = map(int, input().split())
W = [int(input()) for _ in range(N)]
invW = modinv(sum(W), mod)
W = [wi*invW for wi in W]

dp = [[[0] * (K+1) for j in range(M+1)] for i in range(N+1)]
# dp[i][j][k]: i番目の商品まであるとして、j種類の商品を獲得して、k回のくじを引いた場合の数
dp[0][0][0] = 1


for i in range(N):
    for j in range(M+1):
        for k in range(K+1):
            # 使わない場合
            dp[i+1][j][k] += dp[i][j][k]
            dp[i+1][j][k] %= mod
            # 使う場合
            if j == M: continue
            for d in range(1, K+1):
                if k+d <= K:
                    dp[i+1][j+1][k+d] += dp[i][j][k] * pow(W[i], d, mod) * facinv(d)
                    dp[i+1][j+1][k+d] %= mod


print(dp[N][M][K]*fac(K)%mod)
