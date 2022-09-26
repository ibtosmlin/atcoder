# https://atcoder.jp/contests/abc270/tasks/abc270_d
import sys
from collections import defaultdict, Counter, deque
sys.setrecursionlimit(10001000)
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

memo = defaultdict(int)
def dfs(m, turn):
    if (m, turn) in memo:
        ret = memo[(m, turn)]
    elif m == 0:
        memo[(m, 0)] = 0
        memo[(m, 1)] = 0
        ret = 0
    elif turn == 0:
        nw = -100000
        for ai in a:
            if ai > m:
                break
            r = dfs(m - ai, 1 - turn) + ai
            if nw < r:
                nw = r
        memo[(m, turn)] = nw
        ret = nw
    else:
        nw = 100000
        for ai in a:
            if ai > m:
                break
            r = dfs(m - ai, 1 - turn) - ai
            if nw > r:
                nw = r
        memo[(m, turn)] = nw
        ret =nw
    return ret

ret = (dfs(n, 0) + n)//2

print(ret)
