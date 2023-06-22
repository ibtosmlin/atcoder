# https://atcoder.jp/contests/abc231/tasks/abc231_e

n, x = map(int, input().split())
a = list(map(int, input().split()))
from functools import lru_cache

@lru_cache(100000)
def dfs(x, i, cost):
    if i + 1 == n: return cost + x//a[i]
    nx = (x // a[i+1]) * a[i+1]
    ret1 = dfs(nx, i+1, cost + (x - nx) // a[i])
    nx = ((x + a[i+1] - 1) // a[i+1]) * a[i+1]
    ret2 = dfs(nx, i+1, cost + (nx - x) // a[i])
    return min(ret1, ret2)

print(dfs(x, 0, 0))

