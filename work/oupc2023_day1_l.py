# https://atcoder.jp/contests/oupc2023-day1/tasks/oupc2023_day1_l
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

mod = 998244353
t = int(input())
# (3^t - 1)) / ((3 - 1) * 3^(t-1))
# (3 - 3^-(t-1))) / (3 - 1)

y = pow(2, -1, mod)
x = (3 - pow(pow(3, -1, mod), t-1, mod))%mod
print(0, x*y%mod)
