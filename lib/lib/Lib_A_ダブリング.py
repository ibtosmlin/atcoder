#name#
# ダブリング
#discription#
# ダブリング
#body#
dmx = 30
n, k = map(int, input().split())
# f(i)  [0, n] -> [0, n]
def f(i):
    return i - sum(map(int, list(str(i))))

dp = [[0] * (n+1) for _ in range(dmx+1)]

for i in range(n+1):
    dp[0][i] = f(i)

for d in range(0, dmx):
    for i in range(n+1):
        dp[d+1][i] = dp[d][dp[d][i]]

def fk(i, k):
    for d in range(dmx):
        if k >> d & 1:
            i = dp[d][i]
    return i

for i in range(1, n+1):
    print(fk(i, k))
#prefix#
# Lib_A_ダブリング_doubbling
#end#
