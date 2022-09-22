# https://atcoder.jp/contests/mujin-pc-2018/tasks/mujin_pc_2018_e
from heapq import *
from bisect import bisect_left
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)
def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])
h, w ,k = map(int, input().split())
d = input()
g = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if g[i][j] == 'S':
            st = [i, j]
        if g[i][j] == 'G':
            go = [i, j]

direc = ((1, 0), (-1, 0), (0, 1), (0, -1))
# D,U,R,L
direcs = 'DURL'
INF = float('inf')
D = [[] for _ in range(4)]
for i, si in enumerate(d):
    D[direcs.index(si)].append(i)
for di in D:
    if di:
        di.append(di[0] + k)

memo = dict()
def directime(t):
    t = t%k
    if t in memo:
        return memo[t]
    ret = []
    for i, di in enumerate(D):
        if len(di) == 0:
            ret.append(-1)
        else:
            dt = di[bisect_left(di, t)] - t
            ret.append(dt)
    memo[t] = ret
    return ret


def dfs(h, w, s, t):
    seen = [[INF] * w for _ in range(h)]
    que = [(0, s[0], s[1])]

    seen[s[0]][s[1]] = 0
    while que:
        now, u, v = heappop(que)
        direct = directime(now)
        for i in range(4):
            du, dv = direc[i]
            dt = direct[i]
            nu = u + du
            nv = v + dv
            nt = now + dt + 1
            if dt == -1: continue
            if not isinhw(nu, nv, h, w): continue
            if g[nu][nv] == '#' or seen[nu][nv] <= nt: continue
            heappush(que, (nt, nu, nv))
            seen[nu][nv] = nt

    return seen[t[0]][t[1]]


ret = dfs(h, w, st, go)

print(-1 if ret == INF else ret)
