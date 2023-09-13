# https://atcoder.jp/contests/abc319/tasks/abc319_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')

n, m = map(int, input().split())
L = list(map(int, input().split()))

def isok(x):
    x += 1
    row = 1
    now = x
    for l in L:
        l += 1
        if l <= now:
            now -= l
        else:
            row += 1
            now = x - l
            if now < 0: return False
    return row <= m


ok = sum(L) + n*2
ng = max(L) - 2

while ok-ng > 1:
    mid = (ok+ng)//2
    if isok(mid):
        ok = mid
    else:
        ng = mid
print(ok)