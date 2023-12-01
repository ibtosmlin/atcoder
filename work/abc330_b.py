# https://atcoder.jp/contests/abc330/tasks/abc330_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n,l,r = map(int, input().split())
A = list(map(int, input().split()))

for ai in A:
    if l <= ai <= r:
        print(ai)
    else:
        u = min(abs(l-ai), abs(ai-r))
        print(max(ai-u, l))
