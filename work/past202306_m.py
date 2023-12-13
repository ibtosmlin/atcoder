# https://atcoder.jp/contests/past15-open/tasks/past202306_m
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n = int(input())
d = sorted(map(int, input().split()))
t = sum(d)
dp = set([0])
for di in d:
    ndp = set()
    for u in sorted(dp):
        ndp.add(u)
        if u+di <= t//2:
            ndp.add(u+di)
    dp = ndp
print(t - 2 * max(ndp))