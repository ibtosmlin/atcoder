# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_at
mod = 10 ** 9
n = int(input())
n -= 1

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


ma = [[1, 1], [1, 0]]

print(sum(powmat(ma, n-1, mod)[0])%mod)
