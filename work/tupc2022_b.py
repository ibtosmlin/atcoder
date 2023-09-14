# https://atcoder.jp/contests/tupc2022/tasks/tupc2022_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, m ,k = map(int, input().split())
pt = 0
h = 0
for _ in range(m):
    nt, ah = map(int, input().split())
    nh = min(h, nt-pt)







