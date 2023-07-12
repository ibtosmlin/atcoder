#name#
# 行列演算
#descripiton#
# 行列演算
#body#
# ma: nxm
# mb: mxk
# returns nxk - matrix

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


n, m, k = map(int, input().split())
ma = [list(map(int, input().split())) for _ in range(n)]
mb = [list(map(int, input().split())) for _ in range(m)]

for r in prod(ma, mb):
    print(*r)

#prefix#
# Lib_M_行列演算_matrix
#end#


#name#
# 転置行列
#description#
# 転置行列
#body#
def trans(A):
    return [list(x) for x in zip(*A)]
#prefix#
# transpose_matrix
#end#


#name#
# 行列90度回転
#description#
# 行列90度回転
#body#
def rotate(A, reverse = False):
    if reverse:
        return [list(x) for x in zip(*A)][::-1]
    else:
        return [list(x) for x in zip(*A[::-1])]
#prefix#
# Lib_M_rotate_matrix
#end#
