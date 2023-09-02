# https://atcoder.jp/contests/abc318/tasks/abc318_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1: lambda x: int(x) - 1

n, d, p = map(int, input().split())
F = list(map(int, input().split()))
F.sort()
RF = [0]
for fi in F:
    RF.append(RF[-1]+fi)

mx = (n + (d-1)) // d
ret = RF[-1]
for i in range(mx+1):
    if n-i*d < 0:
        ret = min(ret, i*p)
    else:
        ret = min(ret, RF[n-i*d] + i * p)
print(ret)

