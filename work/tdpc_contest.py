# https://atcoder.jp/contests/tdpc/tasks/tdpc_contest
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n = int(input())
A = list(map(int, input().split()))

from sympy import fps

u = [1] + [0]*100
for ai in A:
    f = [1] + [0]*100
    f[ai] = 1
    u = convolve(u, f)

ret = 0
for ai in u:
    if ai: ret += 1

print(ret)
