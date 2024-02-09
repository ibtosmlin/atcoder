# https://atcoder.jp/contests/abc200/tasks/abc200_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n, k = map(int, input().split())

# dp[i][s] : 1以上n以下の数をi個使って和がsになる組み合わせ
dp = [[0] * (3*n+5) for _ in range(4)]
rdp = [0] * (3*n+5)

dp[0][0] = 1
for i in range(1, 3*n+1):
    rdp[i] = rdp[i-1] + dp[0][i-1]

for i in range(3):
    for j in range(3*n+1):
        dp[i+1][j] = rdp[j] - rdp[max(j-n, 0)]
        # for u in range(1, n+1):
        #     dp[i+1][j] += dp[i][j-u]
    rdp = [0] * (3*n+5)
    for j in range(1, 3*n+1):
        rdp[j] = rdp[j-1] + dp[i+1][j-1]
# for dpi in dp: print(dpi)

t = 3
while k > dp[3][t]:
    k -= dp[3][t]
    t += 1

# print(t) # tは合計の数

# 綺麗さがxの数 = おいしさ＋人気度が t-xの数  C(t-x+1, 1)
x = 1
while k > dp[2][t-x]:
    k -= dp[2][t-x]
    x += 1

# 綺麗さがxの数 = おいしさ＋人気度が t-xの数  C(t-x+1, 1)
y = 1
while k > dp[1][t-x-y]:
    k -= dp[1][t-x-y]
    y += 1

print(x, y, t-x-y)
# print(t, x, k)