# https://atcoder.jp/contests/abc317/tasks/abc317_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1

n = int(input())
a = list(map(int, input().split()))
a.sort()
a0 = a[0]
for i in range(n):
    if a0 + i != a[i]:
        print(a0+i)
        exit()