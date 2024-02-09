# https://atcoder.jp/contests/abc337/tasks/abc337_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n = int(input())
t = 0
a = 0
for _ in range(n):
    x, y = map(int, input().split())
    t += x
    a += y

if t > a:
    print('Takahashi')
elif t < a:
    print('Aoki')
else:
    print('Draw')
