#name#
# 最長増加部分列
#description#
# 最長増加部分列
#body#
# 最長増加部分列 dp[k]
# 今まで見た来たものの中で、単調増加(非減少)な部分列であって、
# 長さ k であるようなもののうち、その最後の要素の最小値
# rem: kに対して単調増加
from bisect import bisect, bisect_left

def LIS(x:list):
    n = len(x)
    res = [0] * n
    dp = []
    for i, xi in enumerate(x):
    # 非減少
        pos = bisect(dp, xi)
    # 増加
#        pos = bisect_left(dp, xi)
        res[i] = pos + 1
        if len(dp) <= pos:
            dp.append(xi)
        else:
            dp[pos] = xi
    return dp, res

####################################

#n = int(input())
#a = list(map(int, input().split()))
n = 5
a = [3, 1, 4, 2, 5, 9, 3]

lis, res = LIS(a)
print(len(lis))
print(lis, res)

# n = 5
# a = [3, 8, 4, 1, 9]
# lis = [1, 2, 3, 9]
# res = [1, 1, 2, 2, 3, 4, 3]

#prefix#
# Lib_最長増加部分列_LIS
#end#