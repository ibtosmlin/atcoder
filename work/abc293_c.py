# https://atcoder.jp/contests/abc293/tasks/abc293_c
import sys
sys.setrecursionlimit(10**8)

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

def dfs(u, v, visit):
    if u == h-1 and v == w-1 and len(visit) == h+w-1:
        return 1
    ret = 0
    if u+1<h:
        ret += dfs(u+1, v, visit|{a[u+1][v]})
    if v+1<w:
        ret += dfs(u, v+1, visit|{a[u][v+1]})
    return ret

print(dfs(0,0, {a[0][0]}))