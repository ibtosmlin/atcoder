# https://atcoder.jp/contests/utpc2013/tasks/utpc2013_01
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

x = ["CEFGHIJKLMNSTUVWXYZ",
"CEFGHIJKLMNSTUVWXYZ",
"ADOPQR",
"CEFGHIJKLMNSTUVWXYZ"]

s = input()

for si, xi in zip(s, x):
    if not si in xi:
        exit(print('no'))
print('yes')

