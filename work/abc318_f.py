# https://atcoder.jp/contests/abc318/tasks/abc318_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1: lambda x: int(x) - 1
from collections import defaultdict

#############
n = int(input())
x = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort()

def isok(k):
    nx = sorted([abs(xi - k) for xi in x])
    for nxi, li in zip(nx, l):
        if nxi > li: return False
    return True

res = set()
for i in range(n):
    for j in range(n):
        res.add(x[i]-l[j]-1)
        res.add(x[i]-l[j])
        res.add(x[i]+l[j])
        res.add(x[i]+l[j]+1)

res = sorted(res)

ret = 0
for i in range(len(res)-1):
    if isok(res[i+1]):
        ret += res[i+1] - res[i]

print(ret)
# for rs in res: print(rs)


