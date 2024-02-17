#name#
# reverse=True
#description#
# ソートでのリバース
#body#
reverse=True
#prefix#
# reverse=True
#end#

#name#
# sort(key=itemgetter
#description#
# itemgetterソート
#body#
sort(key=lambda x: x[1])
#prefix#
# sort(key=l
#end#

#name#
# 順列・組み合わせ
#description#
# 順列・組み合わせ
#body#
from itertools import *
P = list(permutations(range(n), r))   # 順列(nPr)
C = list(combinations(range(n), r))   # 組み合わせ(nCr)
CR = list(combinations_with_replacement(range(n), r))  # 重複も許容した組み合わせ(nHr=n+r-1Cr)
PN = list(product(range(n), repeat=r)) # 重複順列(n**r)
T = [[1, 2],[3, 4, 5, 6],[7, 8, 9]]
PT = list(product(*T))
#prefix#
# itertools
# Lib_順列・組み合わせ
#end#

#name#
# 区間カウント
#description#
# 区間カウント
# A=[0, 0, 1, 1, 1, 1, 0, 1, 1, 1]
# x=1 の区間がいくつあるか ans = 2
#body#
def count_intervals(a:list, x)->int:
    dm = a + [float('inf')]
    ret = 0
    is_yes = False
    for ai in dm:
        if ai == x:
            if is_yes: continue
            is_yes = True
        else:
            if not is_yes: continue
            is_yes = False
            ret += 1

    return ret
# A=[0, 0, 1, 1, 1, 1, 0, 1, 1, 1]
# x=1 の区間がいくつあるか ans = 2
#prefix#
# Lib_区間カウント
#end#

#name#
# direc
#description#
# direc
#body#
direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # RULD
direc = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def canmove(i, j, H, W, A=None):
    if A:
        return (0 <= i < H) and (0 <= j < W) and A[i][j] == "."
    else:
        return (0 <= i < H) and (0 <= j < W)

#prefix#
# direc_canmove
#end#
