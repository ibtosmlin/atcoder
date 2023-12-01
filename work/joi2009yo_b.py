# https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
def p(x):
    x.sort()
    return sum(x[-3:])

W = [int(input()) for _ in range(10)]
w = p(W)
K = [int(input()) for _ in range(10)]
k = p(K)
print(w, k)
