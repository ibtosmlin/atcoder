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
sort(key=itemgetter($index))
#prefix#
# sort(key=itemgetter
#end#

#name#
# defaultdict
#description#
# デフォルトディクショナリ
#body#
d = defaultdict($int)
#prefix#
# defaultdict
# d=defaultdict
#end#

#name#
# sort_by_function
#description#
# 比較関数使って並べ替え
#body#
from functools import cmp_to_key
def sort_by_function(x):
    """比較関数を設定してソート
    """
    def compare(item1, item2):
        """ "小さい" -> -1
            "等しい" -> 0
            "大きい" -> 1
        """
        # 以下はx, yが与えられてy/xで比較する例
        # y1/x1 < y2/x2
        # -> y1*x2 < y2*x1
        x1, y1 = item1
        x2, y2 = item2

        if y1*x2 < y2*x1:
            return -1
        elif y1*x2 > y2*x1:
            return 1
        else:
            return 0
    x.sort(key=cmp_to_key(compare))
    return x
########################################
a = [[1, 2], [2, 6] , [3, 6], [4, 5], [5, 7]]
print(a)
a = sort_by_function(a)
print(a)
# [[4, 5], [5, 7], [1, 2], [3, 6], [2, 6]]
#   1.25    0.714    0.5     0.5    0.333
#prefix#
# sort_by_function
#end#

#name#
# 順列・組み合わせ
#description#
# 順列・組み合わせ
#body#
P = list(permutations(range(n), r))   # 順列(nPr)
C = list(combinations(range(n), r))   # 組み合わせ(nCr)
CR = list(combinations_with_replacement(range(n), r))  # 重複も許容した組み合わせ(nHr=n+r-1Cr)
PN = list(product(range(n), repeat=r)) # 重複順列(n**r)
T = [[1, 2],[3, 4, 5, 6],[7, 8, 9]]
PT = list(product(*T))
#prefix#
# itertools
# lib_順列・組み合わせ
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
# lib_区間カウント
#end#

