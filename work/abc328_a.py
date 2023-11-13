# https://atcoder.jp/contests/abc328/tasks/abc328_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, x = map(int, input().split())
S = list(map(int, input().split()))
ret = 0
for si in S:
    if si <= x:
        ret += si
print(ret)
