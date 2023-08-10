# https://atcoder.jp/contests/past202010-open/tasks/past202010_n
from collections import defaultdict
n = 18
m = 6
SS = []
isall = 0
for _ in range(n):
    si = input()
    SS.append(si)
    if all(sii == '?' for sii in si):
        isall += 1
# if isall == n:
#     print(243882696958399859)
#     exit()

SS.append('0'*m)
SS.append('0'*m)


def _check(s, t, u, i):
    cent = t >> i & 1
    cnt = cent
    cnt += s >> i & 1
    cnt += u >> i & 1
    if i >= 1:
        cnt += t >> (i-1) & 1
    if i < n-1:
        cnt += t >> (i+1) & 1
    if cnt < 3 and cent == 0: return True
    if cnt >=3 and cent == 1: return True
    return False

memo = dict()
def canmed(s, t, u):
    if (s, t, u) in memo:
        return memo[(s, t, u)]
    for i in range(m):
        if _check(s, t, u, i): continue
        memo[(s, t, u)] = False
        return False
    memo[(s, t, u)] = True
    return True

def cans(s, b):
    for i in range(m):
        if s[i] == '?': continue
        if b >> i & 1 == int(s[i]): continue
        return False
    return True


dp = [[0] * (1<<m) for _ in range(1<<m)]
dp[0][0] = 1

for s in SS:
    ndp = [[0] * (1<<m) for _ in range(1<<m)]
    for i in range(1<<m):
        for j in range(1<<m):
            for k in range(1<<m):
                if not cans(s, k): continue
                if not canmed(i,j,k): continue
                ndp[j][k] += dp[i][j]
    dp = ndp

print(dp[0][0])

