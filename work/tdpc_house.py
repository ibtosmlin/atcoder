# https://atcoder.jp/contests/tdpc/tasks/tdpc_house
def prod(ma, mb, mod=1):
    n_a = len(ma)
    m_a = len(ma[0])
    n_b = len(mb)
    m_b = len(mb[0])
    if n_a*m_a*n_b*m_b == 0: return 0
    if m_a != n_b: return 0

    ret = []
    for i in range(n_a):
        rw = []
        for j in range(m_b):
            c = 0
            for k in range(m_a):
                c += ma[i][k]*mb[k][j]
                c %= mod
            rw.append(c)
        ret.append(rw)
    return ret

def powmat(ma, k, mod = 10**9+7):
    n = len(ma)
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        ret[i][i] = 1
    for _ in range(k):
        if k & 1:
            ret = prod(ret, ma, mod)
        ma = prod(ma, ma, mod)
        k >>= 1
        if k == 0: break
    return ret

mod = 10**9+7

H, R = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(R)]

A = [[0] * R for _ in range(R)]

def dpfnc(st):
    dp = [[0] * R for _ in range(1<<R)]
    dp[1<<st][st] = 1
    for i in range(1<<R):
        for to in range(R):
            if i >> to & 1: continue
            for fm in range(R):
                if i >> fm & 1 == 0: continue
                if G[fm][to] == 0: continue
                dp[i|1<<to][to] += dp[i][fm]
                dp[i|1<<to][to] %= mod
    for i in range(1<<R):
        for now in range(R):
            A[st][now] += dp[i][now]
            A[st][now] % mod

for i in range(R):
    dpfnc(i)

print(powmat(A, H)[0][0])
