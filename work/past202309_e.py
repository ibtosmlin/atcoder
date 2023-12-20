# https://atcoder.jp/contests/past16-open/tasks/past202309_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)

x = input()
if x[0] == '1' and x[1:] == '0' * (len(x) - 1):
    print(len(x)-1)
else:
    print(len(x))
