# https://atcoder.jp/contests/discovery2016-final/tasks/discovery_2016_final_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

d = {1:100000, 2:50000, 3:30000, 4:20000, 5:10000}
n = int(input())
ret = []
for i in range(1, n+1):
    p = int(input())
    if i not in d:
        g = 0
    else:
        g = d[i]
    ret.append((p, g))
ret.sort()
for _, g in ret:
    print(g)