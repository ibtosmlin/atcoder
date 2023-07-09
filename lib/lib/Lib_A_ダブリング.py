#name#
# ダブリング
#discription#
# ダブリング
#body#

# https://atcoder.jp/contests/abc167/tasks/abc167_d

maxdeg = 100
n, k = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))

def f(i):
    # 1回の遷移
    return A[i]

dp = [[0] * n for _ in range(maxdeg)]
for i in range(n):
    dp[0][i] = f(i)

for t in range(1, maxdeg):
    for i in range(n):
        dp[t][i] = dp[t-1][dp[t-1][i]]

def fk(i, k):
    for d in range(maxdeg):
        if k >> d & 1: i = dp[d][i]
    return i

print(fk(0, k)+1)

#prefix#
# Lib_A_ダブリング_doubbling
#end#
