# https://atcoder.jp/contests/oupc2023-day1/tasks/oupc2023_day1_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

a, t = map(int, input().split())
print((a+(t-1))//t - 1)
