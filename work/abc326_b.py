# https://atcoder.jp/contests/abc326/tasks/abc326_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1



n = int(input())
for i in range(n, 1000):
    f = i
    z = i%10
    i //= 10
    y = i%10
    i //= 10
    x = i
    if x * y == z:
        print(f)
        exit()
