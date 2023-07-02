# https://atcoder.jp/contests/abc249/tasks/abc249_e
from collections import defaultdict

def diff(k):
    return k - len(str(k)) - 1

n, p = map(int, input().split())

dp = [defaultdict(int) for _ in range(n+1)]
# dp[i][j]  i文字まで決めて、T-Sの差がjの場合の数
dp[0][0] = 1

# i文字まで決まっていて残りn-i文字が全て-1として
# jがn-i+1 以上だったら計算する必要なし

for i in range(n):
    for j, c in dp[i].items():
        for k in range(1, n-i+1):
        # kは1文字からn-i文字まで
            ni = i+k
            nj = j+diff(k)
            # nj = min(j+diff(k), n-i+1)
            dp[ni][nj] += c * (26 if i == 0 else 25) % p
            dp[ni][nj] %= p

ret = 0
for k, v in dp[-1].items():
    if k > 0:
        ret += v
        ret % p
print(ret)
print(dp)

