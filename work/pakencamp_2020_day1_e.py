# https://atcoder.jp/contests/pakencamp-2020-day1/tasks/pakencamp_2020_day1_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

x, y = map(int, input().split())

if x == y:
    if x == 0:
        exit(print(1, 1))
    else:
        exit(print(-1))
elif x > y:
    if y == 0:
        exit(print(x, 2*x))
    else:
        exit(print(x, x+y))
else:
    if x == 0:
        exit(print(2*y, y))
    else:
        exit(print(x+y, y))




