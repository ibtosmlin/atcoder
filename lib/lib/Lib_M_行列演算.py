#title#
# 行列演算
#subtitle#
# prod: (ma*mb, mod)行列の掛け算(modで)
# powmat: 正方行列のべき乗計算
# trans: 転置行列を返す
# rotate: 90度回転 reverse = True時計 False反時計
# gauss_jordan: F2(二進数)での上三角行列
# solve_linear_equation: F2(二進数)でAx=bとなるxを求める

#name#
# 行列演算
#descripiton#
# 行列演算
#body#
# ma: nxm
# mb: mxk
# returns nxk - matrix

def prod(ma, mb, mod=1):
    h_a = len(ma)
    w_a = len(ma[0])
    h_b = len(mb)
    w_b = len(mb[0])
    if h_a*w_a*h_b*w_b == 0: return 0
    if w_a != h_b: return 0
    ret = [[0] * h_a for _ in range(w_b)]
    for i in range(h_a):
        for j in range(w_b):
            for k in range(w_a):
                c += ma[i][k]*mb[k][j]
                c %= mod
            ret[i][j] = c
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


#name#
# F2(2進数)での上三角行列生成
#description#
# F2(2進数)での上三角行列生成
#body#
def gauss_jordan(ma):
    n, m = len(ma), len(ma[0])
    rank = 0
    for col in range(m):
        if rank>=n: break
        if ma[rank][col] == 0:
            for row in range(rank+1, n):
                if ma[row][col]:
                    ma[rank], ma[row] = ma[row], ma[rank]
                    break
        if ma[rank][col] == 1:
            for row in range(rank+1, n):
                if ma[row][col]:
                    for _col in range(col, m):
                        ma[row][_col] ^= ma[rank][_col]
            rank += 1
    return ma, rank

#prefix#
# Lib_M_上三角行列
#end#

#name#
# F2(2進数)でのA・x = b となるxを見つける
#description#
# F2(2進数)でのA・x = b となるxを見つける
#body#
def solve_linear_equation(A, b):
    """A・x = b となるxを見つける"""
    h, w = len(A), len(A[0])
    """extend"""
    _A = []
    for Ai, bi in zip(A, b):
        _A.append(Ai + [bi])
    rank = 0
    for col in range(w):
        for row in range(rank, h):
            if _A[row][col]:
                _A[row], _A[rank] = _A[rank], _A[row]
                break
        else: continue
        for row in range(h):
            if row != rank and _A[row][col]:
                for _col in range(w + 1):
                    _A[row][_col] ^= _A[rank][_col]
        rank += 1
    # for ai in A: print(ai)
    # print("---")
    # for ai in _A: print(ai)
    # print(rank)
    return _A, rank

#prefix#
# Lib_M_線形方程式
#end#
