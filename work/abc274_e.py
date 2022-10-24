# https://atcoder.jp/contests/abc274/tasks/abc274_e
INF = float('inf')
def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])

n, m = map(int, input().split())
nm = n + m + 1
c = [[0, 0]]
for _ in range(n):
    x, y = map(int, input().split())
    c.append((x, y))
for _ in range(m):
    x, y = map(int, input().split())
    c.append((x, y))

d = [[0] * nm for _ in range(nm)]
for i in range(nm):
    for j in range(i):
        d[j][i] = d[i][j] = dist2(c[i], c[j]) ** 0.5

dp = [[(INF, 0)] * nm for _ in range(1<<nm)]
for to in range(nm):
    dp[1<<to][to] = (d[0][to], -1 if to > n else 0)

spp = [1]
for i in range(30):
    spp.append(spp[-1] * 2)

for s in range(1, 1<<nm):
    for fm in range(nm):
        if s >> fm & 1 == 0: continue
        if dp[s][fm][0] == INF: continue
        for to in range(nm):
            if s >> to & 1: continue
            ds, sp = dp[s][fm]
            nds = ds + d[fm][to] / spp[-sp]
            nsp = sp - (to > n)
            nxt = s | 1 << to
            dp[nxt][to] = min(dp[nxt][to], (nds, nsp))

mask = (1<<(n+1)) - 1
ret = INF
for s in range(1<<nm):
    if s & mask == mask:
        ret = min(ret, dp[s][0][0])
print(ret)
