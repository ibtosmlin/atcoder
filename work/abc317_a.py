# https://atcoder.jp/contests/abc317/tasks/abc317_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1

n, h, x = map(int, input().split())
p = list(map(int, input().split()))
for i, pi in enumerate(p):
    if pi + h >= x:
        print(i+1)
        exit()