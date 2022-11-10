# https://atcoder.jp/contests/code-thanks-festival-2018/tasks/code_thanks_festival_2018_e
import sys
INF = float('inf')
mod = 1000000007; mod1 = 998244353
def input(): return sys.stdin.readline().rstrip()
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def end(r=-1): print(r); exit()

t = int(input())
a = list(map(int, input().split()))
a = a + [0] * (330-t)
dp = [[0] * 610 for _ in range(332)]

# dp[i][j]: iまで全て消した時にj個残っている場合の数
for i, ai in enumerate(a):
    ndp = [0] * 610
    ndp[0] = 1
    for j in range(2, 610, 2):
        ndp[j//2] = dp[i][j]
    for j in range(610):
        for k in range(ai+1):
            if j+k < 610:
                dp[i+1][j+k] += ndp[j]
                dp[i+1][j+k] %= mod

ret = 0
for d in dp:
    ret += d[1]
    ret %= mod
print(ret)
