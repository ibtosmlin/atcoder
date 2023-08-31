# https://atcoder.jp/contests/arc152/tasks/arc152_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1: lambda x: int(x) - 1
from bisect import bisect_left, bisect_right

INF = float('inf')
n, L = map(int, input().split())
A = [-INF] + list(map(int, input().split())) + [INF]

def f(a, b):
    if abs(a) == INF or abs(b) == INF: return INF
    return max(a+b, 2*L-a-b)

ret = INF
for x in A[1:-1]:
    y = L - x
    i = bisect_left(A, y)
    ret = min(ret, 2*f(x, A[i]))
    ret = min(ret, 2*f(x, A[i-1]))

print(ret)